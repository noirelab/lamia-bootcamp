from airflow import DAG
from functions.helpers import first_task, second_task, third_task
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

# argumentos padrão para o DAG
default_args = {
    'start_date': datetime(2024, 11, 27),
    'owner': 'Airflow'
}

with DAG(dag_id='packaged_dag', schedule_interval="0 0 * * *", default_args=default_args) as dag:

    # Task 1: tem o id de python_task_1 e vai chamar a função first_task
    python_task_1 = PythonOperator(task_id='python_task_1', python_callable=first_task)

    # Task 2: tem o id de python_task_2 e vai chamar a função second_task
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_task)

    # Task 3: tem o id de python_task_3 e vai chamar a função third_task
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_task)

    python_task_1 >> python_task_2 >> python_task_3
