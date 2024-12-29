import sys
import airflow
from airflow import DAG, macros
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta
from process_logs import process_logs_func

# coloca um novo caminho no sistema
sys.path.insert(1, '/usr/local/airflow/dags/scripts')

# template da pasta dos logs
TEMPLATED_LOG_DIR = """{{ var.value.source_path }}/data/{{ macros.ds_format(ts_nodash, "%Y%m%dT%H%M%S", "%Y-%m-%d-%H-%M") }}/"""

# argumentos padrão
default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "youremail@host.com",
            "retries": 1
        }

# enquanto a DAG estiver rodando, cria as tarefas diariamente
with DAG(dag_id="template_dag", schedule_interval="@daily", default_args=default_args) as dag:

    # printa o horário atual
    t0 = BashOperator(
            task_id="t0",
            bash_command="echo {{ ts_nodash }} - {{ macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M') }}")

    # cria um novo log
    t1 = BashOperator(
            task_id="generate_new_logs",
            bash_command="./scripts/generate_new_logs.sh",
            params={'filename': 'log.csv'})

    # verifica se o log existe
    t2 = BashOperator(
            task_id="logs_exist",
            bash_command="test -f " + TEMPLATED_LOG_DIR + "log.csv",
            )

    # processa o log
    t3 = PythonOperator(
            task_id="process_logs",
            python_callable=process_logs_func,
            provide_context=True,
            templates_dict={'log_dir': TEMPLATED_LOG_DIR},
            params={'filename': 'log.csv'}
            )

    # ordem das tarefas
    t0 >> t1 >> t2 >> t3
