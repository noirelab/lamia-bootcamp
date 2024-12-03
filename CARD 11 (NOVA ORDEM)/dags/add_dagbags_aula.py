# script para adicionar dags de diferentes diretórios ao airflow

import os
from airflow.models import DagBag
dags_dirs = [
                '/usr/local/airflow/project_a',
                '/usr/local/airflow/project_b'
            ]

# passa o loop para cada diretório
for dir in dags_dirs:
   dag_bag = DagBag(os.path.expanduser(dir))

   if dag_bag:
      for dag_id, dag in dag_bag.dags.items():
         globals()[dag_id] = dag
