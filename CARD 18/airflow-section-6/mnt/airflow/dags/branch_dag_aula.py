# ------- Adicionado um sleep e mensagem de conclusão ao final da execução

import airflow
import requests
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator

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

    # operador de branch que define o fluxo baseado no retorno da função check_api
    check_api = BranchPythonOperator(
        task_id='check_api',
        python_callable=check_api
    )

    # operador dummy para o caso em que nenhuma API está funcional
    none = DummyOperator(
        task_id='none'
    )

    # operador dummy final, acionado se qualquer API for funcional
    save = DummyOperator(task_id='save', trigger_rule='one_success')

    # define a ordem das tarefas
    check_api >> none >> save

    # cria dinamicamente operadores dummy para cada API no dicionário
    for api in IP_GEOLOCATION_APIS:
        process = DummyOperator(
            task_id=api
        )

        # define a ordem das tarefas para APIs funcionais
        check_api >> process >> save
