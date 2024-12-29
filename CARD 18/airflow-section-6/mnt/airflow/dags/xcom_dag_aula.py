import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.bash_operator import BashOperator

# argumentos padrão para a dag
args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

# função para empurrar valor via xcom
def push_xcom_with_return():
    return 'my_returned_xcom'

# função para pegar o valor empurrado via xcom
def get_pushed_xcom_with_return(**context):
    print(context['ti'].xcom_pull(task_ids='t0'))

# função para empurrar o próximo task para ser executado
def push_next_task(**context):
    context['ti'].xcom_push(key='next_task', value='t3')

# função para pegar o próximo task
def get_next_task(**context):
    return context['ti'].xcom_pull(key='next_task')

# função para pegar múltiplos valores do xcom
def get_multiple_xcoms(**context):
    print(context['ti'].xcom_pull(key=None, task_ids=['t0', 't2']))

# definição da dag
with DAG(dag_id='xcom_dag', default_args=args, schedule_interval="@once") as dag:

    # tarefa 0: empurra valor para o xcom
    t0 = PythonOperator(
        task_id='t0',
        python_callable=push_xcom_with_return
    )

    # tarefa 1: pega o valor empurrado e imprime
    t1 = PythonOperator(
        task_id='t1',
        provide_context=True,
        python_callable=get_pushed_xcom_with_return
    )

    # tarefa 2: empurra próximo task para xcom
    t2 = PythonOperator(
        task_id='t2',
        provide_context=True,
        python_callable=push_next_task
    )

    # branching: escolhe qual tarefa será executada
    branching = BranchPythonOperator(
        task_id='branching',
        provide_context=True,
        python_callable=get_next_task,
    )

    # tarefas dummy para simular execuções
    t3 = DummyOperator(task_id='t3')
    t4 = DummyOperator(task_id='t4')

    # tarefa 5: pega múltiplos valores do xcom
    t5 = PythonOperator(
        task_id='t5',
        trigger_rule='one_success',
        provide_context=True,
        python_callable=get_multiple_xcoms
    )

    # tarefa 6: executa comando bash com valor de xcom
    t6 = BashOperator(
        task_id='t6',
        bash_command="echo value from xcom: {{ ti.xcom_pull(key='next_task') }}"
    )

    # sequência das tarefas
    t0 >> t1
    t1 >> t2 >> branching
    branching >> t3 >> t5 >> t6
    branching >> t4 >> t5 >> t6
