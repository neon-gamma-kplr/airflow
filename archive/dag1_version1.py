from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def hello_world():
    print("#############################################")
    print("  Hello, AIRFLOW!")
    print((datetime.now()+timedelta(hours=2)).strftime("%y-%m-%d %H:%M:%S"))
    print("#############################################")

# Define the DAG
dag = DAG(
    # 'hello_world_dag',
    # 'hello_world_dag_minute',
    'hello_world_dag_minute_time',
    description='A simple DAG that prints Hello, World!',
    # start_date=datetime(2023, 5, 1),
    # start_date=datetime(2023, 6, 19),
    start_date=datetime(2023, 6, 19, 12, 4, 0),
    # schedule_interval='@once'
    schedule_interval='* * * * *'
)

# Define the task
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag
)

# Set the task dependencies
hello_task