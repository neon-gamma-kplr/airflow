# Version 2 : Code DAG avec 2 tâches :
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def greetings(message):
    print("#############################################")
    print(f"{message}, AIRFLOW!")
    print((datetime.now()+timedelta(hours=2)).strftime("%y-%m-%d %H:%M:%S"))
    print("#############################################")

# Define the DAG
dag = DAG(
    'hello_world_dag_double',
    description='A simple DAG that prints Hello, World!',
    start_date=datetime(2023, 6, 19, 12, 36),
    schedule_interval='@once'
)

# Define the task
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=greetings,
    op_kwargs={'message': 'Hello'},
    dag=dag
)

# Define the task
hello_task2 = PythonOperator(
    task_id='hello_task2',
    python_callable=greetings,
    op_kwargs={'message': 'Hello'},
    dag=dag
)

# Define the task
goodbye_task = PythonOperator(
    task_id='goodbye_task',
    python_callable=greetings,
    op_kwargs={'message': 'Goodbye'},
    dag=dag
)

# Set the task dependencies
# hello_task >> hello_task2
[hello_task, hello_task2] >> goodbye_task