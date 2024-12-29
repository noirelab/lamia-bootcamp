from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

# alterei o id pra condizer com o nome do arquivo
# alterei o catchup para True pra diferenciar do outro arquivo
# troquei a ordem das tarefas ssd e cpu alternadamente
with DAG(dag_id='queue_dag_pratica', schedule_interval='0 0 * * *', default_args=default_args, catchup=True) as dag:

    # processamento do ssd
    t_1_ssd = BashOperator(task_id='t_1_ssd', bash_command='echo "I/O intensive task"', queue='worker_cpu')
    t_2_ssd = BashOperator(task_id='t_2_ssd', bash_command='echo "I/O intensive task"', queue='worker_ssd')
    t_3_ssd = BashOperator(task_id='t_3_ssd', bash_command='echo "I/O intensive task"', queue='worker_cpu')

    # processamento cpu
    t_4_cpu = BashOperator(task_id='t_4_cpu', bash_command='echo "CPU instensive task"', queue='worker_ssd')
    t_5_cpu = BashOperator(task_id='t_5_cpu', bash_command='echo "CPU instensive task"', queue='worker_cpu')

    # depende dos workers do spark
    t_6_spark = BashOperator(task_id='t_6_spark', bash_command='echo "Spark dependency task"', queue='worker_spark')

    # tarefa pra teste
    task_7 = DummyOperator(task_id='task_7')

    # ordem das tarefas
    [t_1_ssd, t_2_ssd, t_3_ssd, t_4_cpu, t_5_cpu, t_6_spark] >> task_7
