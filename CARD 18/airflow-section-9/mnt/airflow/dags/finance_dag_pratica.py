# --- Mudança: T3 adicionada
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

# cria a dag com o nome 'finance_dag' e agendamento diário
with DAG(dag_id="finance_dag", default_args=default_args, schedule_interval="@daily") as dag:

    # tarefa dummy que inicia o fluxo de execução
    t1 = DummyOperator(task_id="t1")

    # tarefa bash que imprime uma mensagem de sucesso
    t2 = BashOperator(
            task_id="t2",
            bash_command="echo 'It works'"
        )

    # tarefa bash que imprime uma mensagem final
    t3 = BashOperator(
            task_id="t3",
            bash_command="echo 'Processo terminado'"
        )

    # define a sequência de execução das tarefas
    t1 >> t2 >> t3
