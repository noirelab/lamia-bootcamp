# --- Mudança: Adição do operador log_message para imprimir uma mensagem após todas as subdags serem concluídas

import airflow
from subdags.subdag import factory_subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.executors.celery_executor import CeleryExecutor
from airflow.operators.bash_operator import BashOperator

# nome da dag principal
DAG_NAME = "deadlock_subdag"

# argumentos padrão para a dag
default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

# criação da dag principal
with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag:

    # operador dummy inicial
    start = DummyOperator(
        task_id='start'
    )

    # subdag operador para a primeira subdag
    subdag_1 = SubDagOperator(
        task_id='subdag-1',
        subdag=factory_subdag(DAG_NAME, 'subdag-1', default_args),
        executor=CeleryExecutor()
    )

    # subdag operador para a segunda subdag
    subdag_2 = SubDagOperator(
        task_id='subdag-2',
        subdag=factory_subdag(DAG_NAME, 'subdag-2', default_args),
        executor=CeleryExecutor()
    )

    # subdag operador para a terceira subdag
    subdag_3 = SubDagOperator(
        task_id='subdag-3',
        subdag=factory_subdag(DAG_NAME, 'subdag-3', default_args),
        executor=CeleryExecutor()
    )

    # subdag operador para a quarta subdag
    subdag_4 = SubDagOperator(
        task_id='subdag-4',
        subdag=factory_subdag(DAG_NAME, 'subdag-4', default_args),
        executor=CeleryExecutor()
    )

    # operador bash para imprimir uma mensagem após todas as subdags serem concluídas
    log_message = BashOperator(
        task_id='log_message',
        bash_command="echo 'Todas as subdags foram concluídas!'"
    )

    # operador dummy final
    final = DummyOperator(
        task_id='final'
    )

    # define a sequência das tarefas
    start >> [subdag_1, subdag_2, subdag_3, subdag_4] >> log_message >> final
