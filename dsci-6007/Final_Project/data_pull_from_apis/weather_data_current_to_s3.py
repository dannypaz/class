#! usr/bin/env python
__author__='Jonathan Hilgart'
import requests
import yaml
import os
import boto3


def weather_data_to_s3():
    """Get the current weather in SF every five minutes and push to s3."""
    client = boto3.client('firehose', region_name='us-east-1')
    credentials = yaml.load(open(os.path.expanduser(
        '~/data_engineering_final_credentials.yml')))
    # SF city id 5391997
    weather_key = credentials['open_weather'].get('key')
    # units:imperial returns temp in fahrenheit
    payload = {'id': '5391997', 'units': 'imperial', 'APPID': weather_key}
    # This is the id for San Francisco
    r = requests.get('http://api.openweathermap.org/data/2.5/weather',
        params=payload)
    content = str(r.content)
    # send content to S3 every 5 minutels
    client.put_record(
                DeliveryStreamName='current-sf-weather',
                Record={'Data': content+"\n"})


if __name__ == "__main__":
    weather_data_to_s3()
