from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2024, 12, 2),
    'owner': 'Airflow'
}

def teste():
    return 'testado'

# dag_id: nome do dag
# schedule_interval: frequência com que o dag vai rodar
# default_args: argumentos padrões
# catchup: se o dag vai rodar tarefas que não foram executadas enquanto o dag estava desligado

with DAG(dag_id='dags_pratica', schedule_interval="0 0 * * *", default_args=default_args, catchup=True) as dag:

    # task1 pra mandar um echo de "Hello, World!"
    task1 = BashOperator(task_id='task1', bash_command="echo 'Hello, World!'")

    # task2 pra mandar um echo de "Bye, World!"
    task2 = BashOperator(task_id='task2', bash_command="echo 'Bye, World!'")

    # task3 pra mandar um echo de "testado"
    task3 = PythonOperator(task_id='task3', python_callable=teste)

    task1 >> task2 >> task3
