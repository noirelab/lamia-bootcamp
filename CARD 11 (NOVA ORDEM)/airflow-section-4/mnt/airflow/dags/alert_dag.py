from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

# callback de sucesso
def on_success_task(dict):
    print('on_success_task')
    print(dict)

# callback de falha
def on_failure_task(dict):
    print('on_failure_task')
    print(dict)

default_args = {
    'start_date': datetime(2024, 11, 26),
    'owner': 'Airflow',
    'retries': 3,
    'retry_delay': timedelta(seconds=60),
    'emails': ['owner@test.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'on_failure_callback': on_failure_task,
    'on_success_callback': on_success_task,
    'execution_timeout': timedelta(seconds=60) # nao é recomendao pois cada task tem seu tempo dif
}

# callback de sucesso
def on_succes_dag(dict):
    print('on_success_dag')
    print(dict)

# callback de falha
def on_failure_dag(dict):
    print('on_failure_dag')
    print(dict)


with DAG(dag_id='alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=True, dagrun_timeout = timedelta(seconds = 25), on_success_callback=on_succes_dag, on_failure_callback=on_failure_dag) as dag:

    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="exit 1")

    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="echo 'second task'")

    t1 >> t2
