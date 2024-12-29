import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# argumentos padrão para a dag
default_args = {
    "start_date": airflow.utils.dates.days_ago(1),
    "owner": "Airflow"
}

# função para imprimir o valor recebido da dag controladora
def remote_value(**context):
    print("Value {} for key=message received from the controller DAG".format(context["dag_run"].conf["message"]))

# definição da dag
with DAG(dag_id="triggerdagop_target_dag", default_args=default_args, schedule_interval=None) as dag:

    # tarefa 1: executa função python
    t1 = PythonOperator(
            task_id="t1",
            provide_context=True,
            python_callable=remote_value,
        )

    # tarefa 2: executa comando bash com valor recebido da dag controladora
    t2 = BashOperator(
        task_id="t2",
        bash_command='echo Message: {{ dag_run.conf["message"] if dag_run else "" }}')

    # tarefa 3: espera 30 segundos
    t3 = BashOperator(
        task_id="t3",
        bash_command="sleep 30"
    )
