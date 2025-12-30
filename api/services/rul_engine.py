from ml.rul_engine import RULEngine
from sqlalchemy import text

engine = RULEngine()

def estimate_rul(db, asset_id):
    q = db.execute(text("""
        SELECT EXTRACT(EPOCH FROM ts), corrosion_index
        FROM inspections WHERE asset_id=:a ORDER BY ts
    """),{"a":asset_id}).fetchall()

    if len(q)<3:
        return None

    t = [x[0] for x in q]
    c = [x[1] for x in q]

    rul, v = engine.estimate(t,c)
    return {"rul_days":rul/86400,"growth_velocity":v}
