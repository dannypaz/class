#! usr/bin/env python
import os
import yaml
from pymongo import MongoClient
from boto3 import client
import pytz
import datetime
import time
import boto
import boto.s3
import sys
from boto.s3.key import Key
import json
import csv
__author__ = 'Jonathan Hilgart'

def get_key_names(bucket_s3, sf_year_yes, sf_month_yes, sf_day_yes):
    """get all of the data from s3 for yesterday's normalized data.
    Use part for the prefix to ensure we only get the only file for each
    days data normalization"""
    bart_arrival_key = bucket.get_all_keys(
        prefix="bart_arrival_0_csv{}/{}/{}/part".format(
         sf_year_yes, sf_month_yes, sf_day_yes))

    bart_arrival_key_name = ''
    for k in bart_arrival_key:
        bart_arrival_key_name = k.name

    bart_physical_key = bucket.get_all_keys(
        prefix="bart_physical_0_csv{}/{}/{}/part".format(
        sf_year_yes, sf_month_yes, sf_day_yes))

    #print(bart_physical_key,' first key')
    bart_physical_key_name = ''
    for k in bart_physical_key:
        bart_physical_key_name = k.name

    weather_main_temp_key = bucket.get_all_keys(
        prefix="main-temp-csv-{}/{}/{}/part".format(
        sf_year_yes, sf_month_yes, sf_day_yes))

    weather_main_temp_key_name = ''
    for k in weather_main_temp_key:
        bweather_main_temp_key_name = k.name

    weather_wind_key = bucket.get_all_keys(
        prefix="wind_df-csv{}/{}/{}/part".format(
        sf_year_yes, sf_month_yes, sf_day_yes))

    weather_wind_key_name = ''
    for k in weather_wind_key:
        weather_wind_key_name = k.name

    return bart_arrival_key_name, bart_physical_key, \
        weather_main_temp_key_name, weather_wind_key_name


def insert_into_mongo(bart_arr_key,bart_phy_key,weather_main_t_key,
                      weather_wind_key,bucket_s3):
    """Insert the csv files from s3 into mongo db"""
    # insert into mongo db
    client = MongoClient()
    db_weather_bart = client.weather_bart_db   # name of the database

    bart_arr_key_object = bucket_s3.get_key(
        bart_arr_key)
    bart_arrival_info = \
        (bart_arr_key_object).get_contents_as_string()

    db_weather_bart.bart_arrival.insert(
        {'bart_arrival': bart_arrival_info})

    try:
        bart_physical_key_object = bucket_s3.get_key(
            bart_phy_key[0])
        bart_physical_info = bart_physical_key_object.get_contents_as_string()
        db_weather_bart.bart_physical.insert(
            {'bart_physical': bart_physical_info})
    except (IndexError or AttributeError):
        #print(bart_phy_key, 'bart phy key')
        bart_physical_key_object = bucket_s3.get_key(
            bart_phy_key)
        #print(bart_physical_key_object)
        bart_physical_info = bart_physical_key_object.get_contents_as_string()
        db_weather_bart.bart_physical.insert(
            {'bart_physical': bart_physical_info})

    weather_main_temp_key_object = bucket_s3.get_key(
        weather_main_t_key)
    weather_main_info = weather_main_temp_key_object.get_contents_as_string()
    db_weather_bart.weather_main_temp.insert(
        {'weather_main': weather_main_info})

    weather_wind_key_object = bucket_s3.get_key(
        weather_wind_key)
    weather_wind_info = weather_wind_key_object.get_contents_as_string()
    db_weather_bart.weather_wind.insert(
        {'weather_wind': weather_wind_info})

    print('Everything pushed to mongo')


if __name__ == '__main__':
    # get the time for saving and uploading files
    SF_time = pytz.timezone('US/Pacific')
    yesterday = datetime.datetime.now(SF_time)-datetime.timedelta(1)
    today = datetime.datetime.now(SF_time)

    date_sf, raw_time_sf = time.strftime('{}'.format(today)).split(' ')
    sf_hour, sf_minute = int(raw_time_sf[:2]), int(raw_time_sf[3:5])

    sf_year_yesterday = yesterday.year
    sf_month_yesterday = yesterday.month
    sf_day_yesterday = yesterday.day   # compute yesterday's files

    if len(str(sf_month_yesterday)) < 2:
        sf_month_yesterday = '0'+str(sf_month_yesterday)
    if len(str(sf_day_yesterday)) < 2:
        sf_day_yesterday = '0'+str(sf_day_yesterday)
    # compute today's time
    sf_year_today = today.year
    sf_month_today = today.month
    sf_day_today = today.day   # compute yesterday's files
    # to make the naming convention of kinesis
    if len(str(sf_month_today)) < 2:
        sf_month_today = '0'+str(sf_month_today)
    if len(str(sf_day_today)) < 2:
        sf_day_today = '0'+str(sf_day_today)

    # connect to s3 via boto
    s3_connection = boto.connect_s3()
    bucket = s3_connection.get_bucket('normalized-data-weather-bart')
    # get keynames
    bart_arr_key, bart_phy_key, weather_main_key, weather_wind_key = \
        get_key_names( \
        bucket, sf_year_yesterday, sf_month_yesterday, sf_day_yesterday)
    # insert into mongo
    insert_into_mongo(bart_arr_key,
                    bart_phy_key,
                     weather_main_key,
                      weather_wind_key,
                      bucket)
