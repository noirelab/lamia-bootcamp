import pprint as pp
import airflow.utils.dates
from airflow import DAG, macros
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# define os argumentos padrão para a dag
default_args = {
        "owner": "airflow",
        "start_date": airflow.utils.dates.days_ago(10),
    }

# cria a dag
with DAG(dag_id="data_dag", default_args=default_args, schedule_interval="@daily") as dag:

    # tarefa dummy que simula o envio de dados
    upload = DummyOperator(task_id="upload")

    # tarefa bash para simular o processamento de dados
    process = BashOperator(
            task_id="process",
            bash_command="echo 'processing'"  # imprime 'processing' no log
        )

    # tarefa bash que falha dependendo do dia da execução
    fail = BashOperator(
            task_id="fail",
            bash_command="""
                valid={{macros.ds_format(ds, "%Y-%m-%d", "%d")}}  # extrai o dia da execução
                if [ $(($valid % 2)) == 1 ]; then  # se o dia for ímpar, falha
                        exit 1
                else  # se o dia for par, sucesso
                        exit 0
                fi
            """
        )

    # define a sequência de execução das tarefas
    upload >> process >> fail
