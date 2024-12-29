import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# define os argumentos padrão para a dag
default_args = {
        "owner": "airflow",
        "start_date": airflow.utils.dates.days_ago(1)
    }

# cria a dag
with DAG(dag_id="logger_dag", default_args=default_args, schedule_interval="@daily") as dag:

    # tarefa dummy para iniciar o fluxo
    t1 = DummyOperator(task_id="t1")

    # tarefa bash para exibir mensagem de sucesso no log
    t2 = BashOperator(
            task_id="t2",
            bash_command="echo 'It works'"  # imprime 'It works' no log
        )

    # define a sequência de execução das tarefas
    t1 >> t2
