import requests
from datetime import datetime, timedelta

def send_work_order(cmms_url, asset_id, rul, ci, velocity):
    priority = "HIGH" if rul < 30 else "MEDIUM"
    payload = {
        "asset_id": asset_id,
        "priority": priority,
        "predicted_failure_date": (datetime.utcnow()+timedelta(days=rul)).isoformat(),
        "rul_days": rul,
        "recommended_action": "Inspect & patch corrosion",
        "evidence": {
            "corrosion_index": ci,
            "growth_velocity": velocity
        }
    }
    requests.post(cmms_url+"/workorders", json=payload)
