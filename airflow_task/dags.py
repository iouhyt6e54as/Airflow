from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import random

def print_welcome():
    print("welcome l'm shahd farghaly")

def generate_random_number():
    num = random.randint(1, 100)
    with open('/tmp/random.txt', 'w') as f:
        f.write(str(num))
    print(f"Random number {num}")

with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 10, 1),
    schedule_interval=None,
    catchup=False,
    description="A simple DAG for DEPI Airflow task",
) as dag:

    print_date = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    welcome_message = PythonOperator(
        task_id="welcome_message",
        python_callable=print_welcome,
    )

    generate_random = PythonOperator(
        task_id="generate_random_number",
        python_callable=generate_random_number,
    )

    print_date >> welcome_message >> generate_random