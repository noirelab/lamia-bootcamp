import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

IP_GEOLOCATION_APIS = {
    'ip-api': 'http://ip-api.com/json/',
    'ipstack': 'https://api.ipstack.com/',
    'ipinfo': 'https://ipinfo.io/json'
}

# função para verificar se a API está funcionando
def check_api():
    apis = []
    for api, link in IP_GEOLOCATION_APIS.items():
        r = requests.get(link)
        try:
            data = r.json()
            if data and 'country' in data and len(data['country']):
                apis.append(api)
        except ValueError:
            pass
    return apis if len(apis) > 0 else 'none'

# com a dag certa, cria as tarefas
with DAG(dag_id='branch_dag',
    default_args=default_args,
    schedule_interval="@once") as dag:

    # depdendendo do resultado da função, escolhe o caminho
    check_api = BranchPythonOperator(
        task_id='check_api',
        python_callable=check_api
    )

    # tarefa de teste
    none = DummyOperator(
        task_id='none'
    )

    # tarefa de teste
    save = DummyOperator(task_id='save', trigger_rule='one_success')

    # ordem das tarefas
    check_api >> none >> save

    # cria dinamicamente as tasks de acordo com a api
    for api in IP_GEOLOCATION_APIS:
        process = DummyOperator(
            task_id=api
        )

        # ordem das tasks
        check_api >> process >> save
