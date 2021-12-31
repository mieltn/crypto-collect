# when running airflow locally place this file in airflow/dags

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

with DAG(
    dag_id = 'crypto_update',
    start_date = datetime(2021, 12, 1),
    schedule_interval = timedelta(seconds=60),
    catchup = False
) as dag:

    add_crypto = BashOperator(
        task_id = 'add_crypto',
        # path to your crypto_main.py
        bash_command = 'python /Users/mieltn/Documents/projects/crypto_collect/crypto_main.py'
    )
