import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.bash_operator import BashOperator

import numpy as np
import pandas as pd
from random import randint, sample
import datetime
import time
import calendar

# argumentos padrão para a dag
args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

# função para gerar datas aleatórias entre duas datas
def generate_random_dates(start, end, n):
    dates = pd.Series(np.zeros(n))
    for i in range(n):
        dates[i] = start + datetime.timedelta(seconds=randint(0, int((end - start).total_seconds())))
    return(dates)

# função para gerar o dataframe e retorná-lo via XCom
def push_xcom_with_return():
    # gera um dataframe de exemplo
    n = 1000000

    df = pd.DataFrame({'user_id': sample(range(90000000, 99999999), n),
                    'order_id': np.random.choice(range(1000000, 2000000), n, replace=False),
                    'order_date': generate_random_dates(datetime.date(2015, 1, 1),
                                                        datetime.date(2017, 12, 31),
                                                        n),
                    'number_of_products': np.random.choice(range(20), n, replace=True),
                    'total_amount': np.round(np.random.uniform(1, 5000, n), 2)})

    # adiciona variável dia da semana
    df = df.assign(day_of_week = df.order_date.apply(lambda x: calendar.day_name[x.weekday()]))

    # muda tipo dos ids para string
    df.user_id = df.user_id.astype('str')
    df.order_id = df.order_id.astype('str')

    return df

# função para pegar o dataframe gerado via xcom
def get_pushed_xcom_with_return(**context):
    # puxa o dataframe da tarefa t0
    print(context['ti'].xcom_pull(task_ids='t0'))

# definição da dag
with DAG(dag_id='xcom_dag_big', default_args=args, schedule_interval="@once") as dag:

    # tarefa que gera o dataframe e o empurra via xcom
    t0 = PythonOperator(
        task_id='t0',
        python_callable=push_xcom_with_return
    )

    # tarefa que pega o dataframe empurrado e o imprime
    t1 = PythonOperator(
        task_id='t1',
        provide_context=True,
        python_callable=get_pushed_xcom_with_return
    )

    # sequência das tarefas
    t0 >> t1
