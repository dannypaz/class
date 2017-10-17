#! usr/bin/env python
import requests
import yaml
import os
import json
import boto3
import pytz
import datetime
import time


def weather_data_forecast_to_s3():
    """This function returns a forecast of the weather in SF for 14 days.
    Note - the dt parameter is the time of the forecast in Unix epoch time.
    Run once a day."""
    client = boto3.client('s3')
    credentials = yaml.load(open(os.path.expanduser(
        '~/data_engineering_final_credentials.yml')))
    # SF city id 5391997
    weather_key = credentials['open_weather'].get('key')
    # units:imperial returns temp in fahrenheit
    payload = {'id': '5391997', 'units': 'imperial', \
               'cnt': '14', 'APPID': weather_key}
    # This is the id for San Francisco
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily',
        params=payload)
    content = json.loads(r.content)
    print(content)
    # get the hour for our s3 filesystem
    SF_time = pytz.timezone('US/Pacific')
    current_sf_time = datetime.datetime.now(SF_time)
    date_sf, raw_time_sf = \
        time.strftime('{}'.format(current_sf_time)).split(' ')
    sf_hour, sf_minute = int(raw_time_sf[:2]), int(raw_time_sf[3:5])
    now = datetime.datetime.now()
    sf_year = now.year
    sf_month = now.month
    sf_day = now.day
    KeyFileName = "{}/{}/{}/{}-{}".format(sf_year, sf_month, sf_day, sf_hour,
                                          sf_minute)
    print(KeyFileName)
    client.put_object(ACL='public-read-write', Body=str(content),
                      Bucket='sf-weather-forecast', Key = KeyFileName)


if __name__ == "__main__":
    weather_data_forecast_to_s3()
