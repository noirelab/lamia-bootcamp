from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.bash_operator import BashOperator

from datetime import datetime

default_args = { # define os argumentos padrão
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
    'email': 'owner@test.com'
}

with DAG(dag_id='pool_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:

    # pega as taxas da parte do forex do euro e coloca no XCOM
    get_forex_rate_EUR = SimpleHttpOperator(
        task_id='get_forex_rate_EUR', # id
        method='GET', # função
        priority_weight=1, # prioridade
        pool='forex_api_pool', # pool
        http_conn_id='forex_api', # conexão
        endpoint='/latest?base=EUR', # endpoint
        xcom_push=True # comunicação entre tarefas
    )

    # pega as taxas da parte do forex do dólar e coloca no XCOM
    get_forex_rate_USD = SimpleHttpOperator(
        task_id='get_forex_rate_USD',
        method='GET',
        priority_weight=2,
        pool='forex_api_pool',
        http_conn_id='forex_api',
        endpoint='/latest?base=USD',
        xcom_push=True
    )

    # pega as taxas da parte do forex do iene e coloca no XCOM
    get_forex_rate_JPY = SimpleHttpOperator(
        task_id='get_forex_rate_JPY',
        method='GET',
        priority_weight=3,
        pool='forex_api_pool',
        http_conn_id='forex_api',
        endpoint='/latest?base=JPY',
        xcom_push=True
    )

    # mostra as taxas na tela
    bash_command="""
        {% for task in dag.task_ids %}
            echo "{{ task }}"
            echo "{{ ti.xcom_pull(task) }}"
        {% endfor %}
    """

    # mostra os resultados no bash
    show_data = BashOperator(
        task_id='show_result',
        bash_command=bash_command
    )

    [get_forex_rate_EUR, get_forex_rate_USD, get_forex_rate_JPY] >> show_data
