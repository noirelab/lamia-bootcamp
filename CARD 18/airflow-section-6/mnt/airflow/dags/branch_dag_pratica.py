import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.bash_operator import BashOperator

# argumentos padrão para a DAG
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

# função para verificar quais APIs estão ativas
# retorna uma lista com os nomes das APIs disponíveis ou 'none' caso nenhuma esteja funcional
def check_api():
    apis = []
    for api, link in IP_GEOLOCATION_APIS.items():
        r = requests.get(link)
        try:
            data = r.json()
            # verifica se a resposta contém o campo 'country'
            if data and 'country' in data and len(data['country']):
                apis.append(api)
        except ValueError:
            pass
    return apis if len(apis) > 0 else 'none'

# criação da DAG
with DAG(dag_id='branch_dag',
    default_args=default_args,
    schedule_interval="@once") as dag:

    check_api = BranchPythonOperator(
        task_id='check_api',
        python_callable=check_api
    )

    none = DummyOperator(
        task_id='none'
    )

    save = DummyOperator(task_id='save', trigger_rule='one_success')

    # dorme por 30 segundos
    t2 = BashOperator(
            task_id="t2",
            bash_command="sleep 30"
        )

    # operador bash para imprimir a conclusão
    complete = BashOperator(
        task_id="complete",
        bash_command="echo 'Fluxo concluído!'"
    )

    # define a ordem das tarefas
    check_api >> none >> save
    save >> complete

    # cria dinamicamente operadores dummy para cada API no dicionário
    for api in IP_GEOLOCATION_APIS:
        process = DummyOperator(
            task_id=api
        )

        # define a ordem das tarefas para APIs funcionais
        check_api >> process >> save
