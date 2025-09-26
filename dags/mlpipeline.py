from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

## Define Task1

def preprocess_data():
    print("Preprocessing data ...")


### task 2
def train_model():
    print("training model ...")


## task 3

def evaluate_model():
    print("evaluate model ...")


## Define Dag

with DAG(
    'ml_pipelines',
    start_date=datetime(2024, 1, 1),
    schedule='@weekly'
) as dag:
    # Define the task
    preprocess = PythonOperator(task_id='preprocess_task', python_callable=preprocess_data)
    train=PythonOperator(task_id='train_task', python_callable=train_model)
    evaluate=PythonOperator(task_id='evaluate_task', python_callable=evaluate_model)

    # set dependencies (the order)
    preprocess >> train >> evaluate
