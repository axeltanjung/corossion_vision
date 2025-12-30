from services.rul_engine import estimate_rul

def build_budget_table(db):
    rows=[]
    for (a,) in db.execute("SELECT DISTINCT asset_id FROM inspections"):
        r=estimate_rul(db,a)
        if not r: continue

        # derive failure probability from Weibull
        P = r["hazard"]
        L = 100000   # business defined loss
        C = 5000     # maintenance cost
        rows.append((a,C,P,L))
    return rows
