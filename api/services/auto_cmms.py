from sqlalchemy import text
from services.cmms_connector import send_work_order
from services.rul_engine import estimate_rul

CMMS_URL = "http://cmms-system/api"

def auto_dispatch(db):
    assets = db.execute(text("SELECT DISTINCT asset_id FROM inspections")).fetchall()

    for (a,) in assets:
        r = estimate_rul(db,a)
        if not r: continue

        if r["rul_days"] < 45:   # auto threshold
            send_work_order(CMMS_URL, a, r["rul_days"], r["current_ci"], r["growth_velocity"])
