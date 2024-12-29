import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator

# argumentos padrão para a dag
default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

# funções para simulação de download
def download_website_a():
    print("download_website_a")
    raise ValueError("error")

def download_website_b():
    print("download_website_b")
    raise ValueError("error")

def download_failed():
    print("download_failed")
    raise ValueError("error")

def download_succeed():
    print("download_succeed")
    raise ValueError("error")

def process():
    print("process")
    raise ValueError("error")

def notif_a():
    print("notif_a")
    raise ValueError("error")

def notif_b():
    print("notif_b")
    raise ValueError("error")

# definição da dag
with DAG(dag_id='trigger_rule_dag',
    default_args=default_args,
    schedule_interval="@daily") as dag:

    # definição das tarefas com regras de trigger
    download_website_a_task = PythonOperator(
        task_id='download_website_a',
        python_callable=download_website_a,
        trigger_rule="all_success"
    )

    download_website_b_task = PythonOperator(
        task_id='download_website_b',
        python_callable=download_website_b,
        trigger_rule="all_success"
    )

    download_failed_task = PythonOperator(
        task_id='download_failed',
        python_callable=download_failed,
        trigger_rule="all_failed"
    )

    download_succeed_task = PythonOperator(
        task_id='download_succeed',
        python_callable=download_succeed,
        trigger_rule="all_success"
    )

    process_task = PythonOperator(
        task_id='process',
        python_callable=process,
        trigger_rule="one_success"
    )

    notif_a_task = PythonOperator(
        task_id='notif_a',
        python_callable=notif_a,
        trigger_rule="none_failed"
    )

    notif_b_task = PythonOperator(
        task_id='notif_b',
        python_callable=notif_b,
        trigger_rule="one_failed"
    )

    # definição das dependências das tarefas
    [download_failed_task, download_succeed_task] >> process_task
    [download_website_a_task, download_website_b_task] >> download_failed_task
    [download_website_a_task, download_website_b_task] >> download_succeed_task
    process_task >> [notif_a_task, notif_b_task]
