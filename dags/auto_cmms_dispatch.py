from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from api.services.auto_cmms import auto_dispatch

with DAG("cmms_auto_dispatch", start_date=datetime(2025,1,1), schedule_interval="@daily") as dag:
    PythonOperator(
        task_id="dispatch",
        python_callable=auto_dispatch
    )
