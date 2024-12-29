import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator

# argumentos padrão para a dag
default_args = {
        "owner": "airflow",
        "start_date": airflow.utils.dates.days_ago(1)
    }

# função para condicionalmente disparar outro dag
def conditionally_trigger(context, dag_run_obj):
    # verifica a condição e define a payload
    if context['params']['condition_param']:
        dag_run_obj.payload = {
                'message': context['params']['message']
            }
        pp.pprint(dag_run_obj.payload)
        return dag_run_obj

# definição da dag principal
with DAG(dag_id="triggerdagop_controller_dag", default_args=default_args, schedule_interval="@once") as dag:

    # operador para disparar outro dag
    trigger = TriggerDagRunOperator(
        task_id="trigger_dag",
        trigger_dag_id="triggerdagop_target_dag",
        provide_context=True,
        python_callable=conditionally_trigger,
        params={
            'condition_param': True,
            'message': 'Hi from the controller'
        },
    )

    # tarefa final
    last_task = DummyOperator(task_id="last_task")

    # sequência das tarefas
    trigger >> last_task
