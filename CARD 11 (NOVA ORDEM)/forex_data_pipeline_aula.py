from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor   # importei de um jeito diferente ao do vídeo pois estava deprecated
from airflow.operators.python import PythonOperator # importei de um jeito diferente ao do vídeo pois estava deprecated
from airflow.operators.bash import BashOperator     # importei de um jeito diferente ao do vídeo pois estava deprecated

# from airflow.operators.hive_operator import HiveOperator ---- está dando muito conflito
# from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.email import EmailOperator
#from airflow.operators.slack_operator import SlackAPIPostOperator

import requests
import json
import csv

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 24),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'email': 'meuemail@host.com', # email usado para notificações
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# função para baixar taxas forex das moedas desejadas
def download_rates():
    with open('/usr/local/airflow/dags/files/forex_currencies.csv') as forex_currencies:
        reader = csv.DictReader(forex_currencies, delimiter=';')
        for row in reader:
            base = row['base']
            with_pairs = row['with_pairs'].split(' ')
            indata = requests.get('https://api.exchangeratesapi.io/latest?base=' + base).json()
            outdata = {'base': base, 'rates': {}, 'last_update': indata['date']}
            for pair in with_pairs:
                outdata['rates'][pair] = indata['rates'][pair]
            with open('/usr/local/airflow/dags/files/forex_rates.json', 'a') as outfile:
                json.dump(outdata, outfile)
                outfile.write('\n')

# definição da dag
with DAG(dag_id='forex_data_pipeline',
         schedule='@daily',
         default_args=default_args,
         catchup=False) as dag:

    # verifica se o endpoint forex está disponível
    is_forex_rates_available = HttpSensor(
        task_id='is_forex_rates_available',
        method='GET',
        http_conn_id='forex_api',
        endpoint='latest',
        response_check=lambda response: 'rates' in response.text, # verifica a presença de "rates"
        poke_interval=5,
        timeout=20
    )

    # verifica se o arquivo de moedas está disponível
    is_forex_currencies_file_available = FileSensor(
        task_id='is_forex_currencies_file_available',
        fs_conn_id='forex_path',
        filepath='forex_currencies.csv',
        poke_interval=5,
        timeout=20
    )

    # baixa as taxas forex
    downloading_rates = PythonOperator(
        task_id='downloading_rates',
        python_callable=download_rates
    )

    # salva as taxas no hdfs
    saving_rates = BashOperator(
        task_id='saving_rates',
        bash_command="""
                    hdfs dfs -mkdir -p /forex && \
                        hdfs dfs -put -f $AIRFLOW_HOME/dags/files/forex_rates.json /forex
                    """
    )


    # está dando muito conflito por ser uma versão mais antiga do airflow
    # creating_forex_rates_table = HiveOperator(
    #     task_id="creating_forex_rates_table",
    #     hive_cli_conn_id="hive_conn",
    #     hql="""
    #         CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
    #             base STRING,
    #             last_update DATE,
    #             eur DOUBLE,
    #             usd DOUBLE,
    #             nzd DOUBLE,
    #             gbp DOUBLE,
    #             jpy DOUBLE,
    #             cad DOUBLE
    #             )
    #         ROW FORMAT DELIMITED
    #         FIELDS TERMINATED BY ','
    #         STORED AS TEXTFILE
    #     """
    # )

    # forex_processing = SparkSubmitOperator(
    #     task_id="forex_processing",
    #     conn_id="spark_conn",
    #     application="/usr/local/airflow/dags/scripts/forex_processing.py",
    #     verbose=False
    # )

    # envia email de notificação de sucesso
    sending_email_notification = EmailOperator(
            task_id="sending_email",
            to="airflow_course@yopmail.com",
            subject="forex_data_pipeline",
            html_content="""
                <h3>forex_data_pipeline succeeded</h3>
            """

            )
    # sending_slack_notification = SlackAPIPostOperator(
    #     task_id="sending_slack",
    #     slack_conn_id="slack_conn",
    #     username="airflow",
    #     text="DAG forex_data_pipeline: DONE",
    #     channel="#airflow-exploit"
    # )
