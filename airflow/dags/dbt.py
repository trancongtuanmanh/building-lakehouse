import os

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def set_env():
    print("Hello World")
    os.environ["DBT_PROFILES_DIR"] = os.getcwd() + "/restaurant_analytis/"
    os.environ["DBT_PROJECT_DIR"] = os.getcwd() + "/restaurant_analytis/"

with DAG(dag_id="run_dbt", start_date=datetime(2020, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    set_environment = PythonOperator(task_id="hello_world", python_callable=set_env)
    run_dbt = BashOperator( 
        task_id="run_dbt",
        bash_command="dbt run",
        env={"SPARK_HOME": "/usr/local/airflow/jars"}
    )

    set_environment >> run_dbt 

