from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 28, 11)
}

# só pra marcar
def process():
    return 'process'

with DAG(dag_id='tst_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:

    # o dummy operator é um operador que não faz nada
    task_1 = DummyOperator(task_id='task_1')

    # o python operator é um operador que roda uma função python
    task_2 = PythonOperator(task_id='task_2', python_callable=process)

    # tasks geradas dinamicamente
    tasks = [DummyOperator(task_id='task_{0}'.format(t)) for t in range(3, 6)]

    task_6 = DummyOperator(task_id='task_6')

    task_1 >> task_2 >> tasks >> task_6
