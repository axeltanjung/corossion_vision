from sqlalchemy import text
from rul_engine import RULEngine

def build_schedule(db, capacity=10):
    assets = db.execute(text("""
      SELECT DISTINCT asset_id FROM inspections
    """)).fetchall()

    engine = RULEngine()
    scored = []

    for (a,) in assets:
        rul = engine.estimate_asset(db,a)
        if not rul: continue

        hazard = rul["hazard"]
        ci = rul["current_ci"]
        criticality = 1  # configurable later

        risk = hazard * ci * criticality
        scored.append((a,risk))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:capacity]
