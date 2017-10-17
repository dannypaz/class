#! usr/bin/env python
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta
__author__ = "Jonathan Hilgart"

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2017, 3, 1),
        'email': ['jonathan.hilgart@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
      }

dag = DAG('weather_forecast-s3', default_args=default_args, schedule_interval='@hourly')
# run once a day
t1 = BashOperator(
    task_id='weather-forecast',
    bash_command='python ~/./weather_data_forecast_to_s3.py',
    retries=3,
    dag=dag)
