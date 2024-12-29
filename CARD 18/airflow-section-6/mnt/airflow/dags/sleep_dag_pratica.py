import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# argumentos padrão para a dag
default_args = {
        "owner": "airflow",
        "start_date": airflow.utils.dates.days_ago(1)
    }

# criação da dag
# removi a ordem das tarefas pois não considerei necessário nesse específico caso
with DAG(dag_id="sleep_dag", default_args=default_args, schedule_interval="@daily") as dag:

    # operador dummy inicial
    t1 = DummyOperator(task_id="t1")

    # operador bash que executa um comando para pausar por 30 segundos
    t2 = BashOperator(
            task_id="t2",
            bash_command="sleep 30"
        )
