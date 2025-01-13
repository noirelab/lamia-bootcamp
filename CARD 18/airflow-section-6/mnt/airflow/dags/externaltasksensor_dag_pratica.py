# --- Mudança: Adicionado o bashoperator que imprime no final do fluxo

import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# argumentos padrão para a dag
default_args = {
    "owner": "airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

# criação da dag
with DAG(dag_id="externaltasksensor_dag", default_args=default_args, schedule_interval="@daily") as dag:

    # sensor para monitorar a conclusão de uma tarefa em outra dag
    sensor = ExternalTaskSensor(
        task_id='sensor',
        external_dag_id='sleep_dag',
        external_task_id='t2'
    )

    # operador dummy final
    last_task = DummyOperator(task_id="last_task")

    # operador bash para imprimir uma mensagem
    final_message = BashOperator(
        task_id="final_message",
        bash_command="echo 'Fluxo concluído com sucesso!'"
    )

    # define a sequência das tarefas
    sensor >> last_task >> final_message
