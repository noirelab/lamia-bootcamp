import airflow
from subdags.subdag import factory_subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.executors.sequential_executor import SequentialExecutor
from airflow.executors.celery_executor import CeleryExecutor

# nome da dag principal
DAG_NAME="test_subdag"

# argumentos padrão para a dag
default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

# definição da dag principal
with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag:

    # tarefa inicial
    start = DummyOperator(
        task_id='start'
    )

    # subdag 1 com executor celery
    subdag_1 = SubDagOperator(
        task_id='subdag-1',
        subdag=factory_subdag(DAG_NAME, 'subdag-1', default_args),
        executor=CeleryExecutor()
    )

    # outra tarefa
    some_other_task = DummyOperator(
        task_id='check'
    )

    # subdag 2 com executor celery
    subdag_2 = SubDagOperator(
        task_id='subdag-2',
        subdag=factory_subdag(DAG_NAME, 'subdag-2', default_args),
        executor=CeleryExecutor()
    )

    # tarefa final
    end = DummyOperator(
        task_id='final'
    )

    # sequência das tarefas
    start >> subdag_1 >> some_other_task >> subdag_2 >> end