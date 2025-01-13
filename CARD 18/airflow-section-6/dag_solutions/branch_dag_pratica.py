import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator

# argumentos padrão para a dag
default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

# dicionário contendo os links das APIs de geolocalização
IP_GEOLOCATION_APIS = {
    'ip-api': 'http://ip-api.com/json/',
    'ipstack': 'https://api.ipstack.com/',
    'ipinfo': 'https://ipinfo.io/json'
}

# função para verificar se as APIs estão funcionando
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

# função para imprimir uma mensagem de conclusão
def log_completion():
    print("Verificação das APIs concluída com sucesso.")

# criação da DAG
with DAG(dag_id='branch_dag',
         default_args=default_args,
         schedule_interval="@once") as dag:

    # branch para verificar as APIs
    check_api = BranchPythonOperator(
        task_id='check_api',
        python_callable=check_api
    )

    # operador Python para logar a conclusão
    log_task = PythonOperator(
        task_id='log_completion',
        python_callable=log_completion
    )

    # tarefas de teste
    none = DummyOperator(task_id='none')
    save = DummyOperator(task_id='save', trigger_rule='one_success')

    # define a sequência das tarefas
    check_api >> none >> save
    check_api >> log_task

    # cria dinamicamente tarefas dummy para cada API
    for api in IP_GEOLOCATION_APIS:
        process = DummyOperator(
            task_id=api
        )

        # ordem das tasks para APIs funcionais
        check_api >> process >> save
