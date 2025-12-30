from fastapi import FastAPI, UploadFile
from sqlalchemy import create_engine, text
import requests, numpy as np

app = FastAPI()
engine = create_engine("postgresql://postgres:postgres@db:5432/corrosion")

@app.post("/predict")
async def predict(asset_id: str, image: UploadFile):
    r = requests.post("http://vision:8001/infer", files={"file": image.file})
    rust, entropy = r.json().values()
    CI = 0.55*rust + 0.30*entropy + 0.15*growth_velocity(asset_id,rust)

    with engine.begin() as c:
        c.execute(text("""
        INSERT INTO inspections(asset_id,rust_area,entropy,corrosion_index)
        VALUES(:a,:r,:e,:ci)
        """), dict(a=asset_id,r=rust,e=entropy,ci=CI))

    return {"corrosion_index":CI}

@app.get("/asset/{asset_id}/rul")
def asset_rul(asset_id: str, db=Depends(get_db)):
    return estimate_rul(db,asset_id)

@app.get("/schedule/today")
def today_schedule(db=Depends(get_db)):
    return build_schedule(db, capacity=10)

@app.get("/optimize/budget")
def optimize_budget(budget:int, db=Depends(get_db)):
    assets = build_budget_table(db)
    return optimize(assets,budget)

@app.post("/simulate/{asset_id}")
def simulate_asset(asset_id:str, plan:dict, days:int=180, db=Depends(get_db)):
    ci0, v = load_current_state(db,asset_id)
    traj = simulate(ci0,v,days,plan)
    return {"trajectory":traj}

from stable_baselines3 import PPO
policy = PPO.load("policy_corrosion")

def recommend_action(ci,H,T,S):
    a,_ = policy.predict([ci,H,T,S])
    return ["NO_ACTION","LIGHT_REPAIR","HEAVY_REPAIR"][a]

@app.get("/assets")
def all_assets(db=Depends(get_db)):
    return db.execute(text("""
      SELECT a.asset_id, a.location, 
             MAX(i.corrosion_index) as corrosion_index,
             0 as lat, 0 as lon,
             30 as rul_days
      FROM assets a JOIN inspections i ON a.asset_id=i.asset_id
      GROUP BY a.asset_id,a.location
    """)).fetchall()

