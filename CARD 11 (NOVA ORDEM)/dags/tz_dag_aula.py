import pendulum
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy_operator import DummyOperator

from datetime import timedelta, datetime

# usa o timezone de paris
local_tz = pendulum.timezone("Europe/Paris")

default_args = {
    'start_date': datetime(2024, 11, 25, 2, tzinfo=local_tz),
    'owner': 'Airflow'
}

# 0 1 * * * - todo dia 1h localtime
with DAG(dag_id='tz_dag', schedule_interval="0 2 * * *", default_args=default_args) as dag:
    dummy_task = DummyOperator(task_id='dummy_task')

    # calcula as datas de execução da dag com base no 'start_date'
    run_dates = dag.get_run_dates(start_date=dag.start_date)
    # define a próxima data de execução se existir
    next_execution_date = run_dates[-1] if len(run_dates) != 0 else None

    # os logs ajudam a entender o que está acontecendo e quando estão acontecendo
    print('datetime from Python is Naive: {0}'.format(timezone.is_naive(datetime(2019, 9, 19))))
    print('datetime from Airflow is Aware: {0}'.format(timezone.is_naive(timezone.datetime(2019, 9, 19)) == False))
    print('[DAG:tz_dag] timezone: {0} - start_date: {1} - schedule_interval: {2} - Last execution_date: {3} - next execution_date {4} in UTC - next execution_date {5} in local time'.format(
        dag.timezone,
        dag.default_args['start_date'],
        dag._schedule_interval,
        dag.latest_execution_date,
        next_execution_date,
        local_tz.convert(next_execution_date) if next_execution_date is not None else None
        ))
