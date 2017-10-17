#! usr/bin/env python
from airflow import DAG
from airflow.operators import BashOperator, PythonOperator
from datetime import datetime, timedelta
__author__ = "Jonathan Hilgart"


default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2016, 1, 1),
        'email': ['jonathan.hilgart@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
      }

dag = DAG('weather-bart_data_s3', default_args=default_args, schedule_interval=timedelta(seconds=300))
# run every 5 mins
t1 = BashOperator(
    task_id='weather_current_to_s3',
    bash_command='python ~/./weather_data_current_to_s3.py',
    retries=3,
    dag=dag)
t2= BashOperator(
    task_id='bart_data_to_s3',
    bash_command='python ~/./bart_to_s3.py',
    retries=3,
    dag=dag)
