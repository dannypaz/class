# coding: utf-8
from pyspark.sql.functions import explode, from_unixtime, from_json
from pyspark.sql import SQLContext, column
from pyspark.sql import DataFrame
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import DateType
from pyspark import SparkConf, SparkContext  # for running spark-submit job
import time
import pytz
import datetime
__author__="__Jonathan Hilgart__"
# when running spark-submit, need to create the spark context
sc = SparkContext()
spark = SparkSession(sc)
sqlContext = SQLContext(sc)
# get the time for saving and uploading files
yesterday = datetime.date.today()-datetime.timedelta(1)
SF_time = pytz.timezone('US/Pacific')
current_sf_time = datetime.datetime.now(SF_time)
date_sf, raw_time_sf = time.strftime('{}'.format(current_sf_time)).split(' ')
sf_hour, sf_minute = int(raw_time_sf[:2]), int(raw_time_sf[3:5])
sf_year = yesterday.year
sf_month = yesterday.month
sf_day = yesterday.day   # compute yesterday's files
if len(str(sf_month)) < 2:
    sf_month = '0'+str(sf_month)
if len(str(sf_day)) < 2:
    sf_day = '0'+str(sf_day)
# this is for the batch jobs to save the file location
KeyFileName = "{}/{}/{}".format(sf_year, sf_month, sf_day)
weather_path = "s3a://current-weather-data/{}/{}/{}/*/*".format(sf_year,
                                                    sf_month, sf_day)
weather_df = spark.read.json(weather_path)
weather_description_df = weather_df.select(hour(from_unixtime("dt")
    ).alias('hour'), date_format(from_unixtime('dt'), 'MM/dd/yyy').alias(
        'date'), explode("weather.main"))
# weather data
main_temp_df = weather_df.select(hour(from_unixtime("dt")
    ).alias('hour'), date_format(from_unixtime('dt'),'MM/dd/yyy').alias('date'),
    "main.humidity", "main.pressure", "main.temp", "main.temp_max",
    "main.temp_min")
wind_df = weather_df .select(
    hour(from_unixtime("dt")).alias('hour'),
    date_format(from_unixtime('dt'),'MM/dd/yyy').alias('date'),
    "wind.speed", "wind.deg")
location_df = weather_df .select(
    hour(from_unixtime("dt")).alias('hour'),
    date_format(from_unixtime('dt'), 'MM/dd/yyy').alias('date'), "name")
# save the weather data
# The try except blocks are checking to see if the file already exists on s3
try:
    weather_description_df.write.parquet(
        "s3a://normalized-data-weather-bart/weather-description{}".format(
            KeyFileName))
except:  # file already exists
    pass
try:
    main_temp_df.write.parquet(
        "s3a://normalized-data-weather-bart/main-temp{}".format(KeyFileName))
except:
    pass
try:
    wind_df.write.parquet("s3a://normalized-data-weather-bart/wind_df{}".format(
        KeyFileName))
except:
    pass
try:
    location_df.write.parquet("s3a://normalized-data-weather-bart/location{}".format(
        KeyFileName))
except:
    pass
    # save the weather data as a one csv
try:
    main_temp_df.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/main-temp-csv-{}".format(KeyFileName),
        format='csv')
except:
    pass
try:
    wind_df.coalesce(1).write.save("s3a://normalized-data-weather-bart/wind_df-csv{}".format(
        KeyFileName), format = 'csv')
except:
    pass
try:
    location_df.coalesce(1).write.save("s3a://normalized-data-weather-bart/location-csv{}".format(
        KeyFileName), format = 'csv')
except:
    pass
try:
    weather_description_df.coalesce(1).write.csv(
        "s3a://normalized-data-weather-bart/weather-description-csv{}".format(
            KeyFileName), format = 'csv')
except:
    pass
# onto bart data
bart_path = "s3a://bart-data-collection/{}/{}/{}/*/*".format(sf_year,
                                                             sf_month, sf_day)
bart_df = spark.read.json(bart_path)
bart_arrival_0 = bart_df.select(
    col("origin_station.0").alias("origin_station_0"),
    col("time.0").alias('sf_time_0'),
    col("date.0").alias("date_0"),
    col("direction.0").alias("direction_0"),
    col("destination.0").alias("destination_0"),
    hour(from_unixtime("unix_time.0")).alias("hour_0"),
    col("minutes.0").alias('minutes_til_arrival_0'))
bart_arrival_1 = bart_df.select(
    col("origin_station.1").alias("origin_station_1"),
    col("time.1").alias('sf_time_1'),
    col("date.1").alias("date_1"),
    col("direction.1").alias("direction_1"),
    col("destination.1").alias("destination_1"),
    hour(from_unixtime("unix_time.1")).alias("hour_1"),
    col("minutes.1").alias('minutes_til_arrival_1'))
bart_arrival_2 = bart_df.select(
    col("origin_station.2").alias("origin_station_2"),
    col("time.2").alias('sf_time_2'),
    col("date.2").alias("date_2"),
    col("direction.2").alias("direction_2"),
    col("destination.2").alias("destination_2"),
    hour(from_unixtime("unix_time.2")).alias("hour_2"),
    col("minutes.2").alias('minutes_til_arrival_2'))
bart_physical_0 = bart_df.select(
    col("origin_station.0").alias("origin_station_0"),
    col("time.0").alias('sf_time_0'),
    col("date.0").alias("date_0"), col("direction.0").alias("direction_0"),
    col("destination.0").alias("destination_0"),
    hour(from_unixtime("unix_time.0")).alias("hour_0"),
    col("color.0").alias("color_0"), col("bike_flag.0").alias("bike_flag_0"),
    col("train_size.0").alias("train_size_0"),
    col("capacity.0").alias("capacity_0"))
bart_physical_1 = bart_df.select(
    col("origin_station.1").alias("origin_station_1"),
    col("time.1").alias('sf_time_1'), col("date.1").alias("date_1"),
    col("direction.1").alias("direction_1"),
    col("destination.1").alias("destination_1"),
    hour(from_unixtime("unix_time.1")).alias("hour_1"),
    col("color.1").alias("color_1"), col("bike_flag.1").alias("bike_flag_1"),
    col("train_size.1").alias("train_size_1"),
    col("capacity.1").alias("capacity_1"))
bart_physical_2 = bart_df.select(
    col("origin_station.2").alias("origin_station_2"),
    col("time.2").alias('sf_time_2'),
    col("date.2").alias("date_2"),
    col("direction.2").alias("direction_2"),
    col("destination.2").alias("destination_2"),
    hour(from_unixtime("unix_time.2")).alias("hour_2"),
    col("color.2").alias("color_2"), col("bike_flag.2").alias("bike_flag_2"),
    col("train_size.2").alias("train_size_2"),
    col("capacity.2").alias("capacity_2"))
# write to parquet for bart data
try:
    bart_arrival_0.write.parquet(
        "s3a://normalized-data-weather-bart/bart_arrival_0_{}".format(
            KeyFileName))
except:
    pass
try:
    bart_arrival_1.write.parquet(
        "s3a://normalized-data-weather-bart/bart_arrival_1_{}".format(
            KeyFileName))
except:
    pass
try:
    bart_arrival_2.write.parquet(
        "s3a://normalized-data-weather-bart/bart_arrival_2_{}".format(
            KeyFileName))
except:
    pass
try:
    bart_physical_0.write.parquet(
        "s3a://normalized-data-weather-bart/bart_physical_0_{}".format(
            KeyFileName))
except:
    pass
try:
    bart_physical_1.write.parquet(
        "s3a://normalized-data-weather-bart/bart_physical_1_{}".format(
            KeyFileName))
except:
    pass
try:
    bart_physical_2.write.parquet(
        "s3a://normalized-data-weather-bart/bart_physical_2_{}".format(
            KeyFileName))
except:
    pass
    # write to csv for bart data
try:
    bart_arrival_0.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/bart_arrival_0_csv{}".format(
            KeyFileName), format='csv')
except:
    pass
try:

    bart_arrival_1.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/bart_arrival_1_csv{}".format(
            KeyFileName), format='csv')
except:
    pass
try:
    bart_arrival_2.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/bart_arrival_2_csv{}".format(
            KeyFileName), format="csv")
except:
    pass
try:
    bart_physical_0.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/bart_physical_0_csv{}".format(
            KeyFileName), format="csv")
except:
    pass
try:
    bart_physical_1.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/bart_physical_1_csv{}".format(
            KeyFileName), format="csv")
except:
    pass
try:
    bart_physical_2.coalesce(1).write.save(
        "s3a://normalized-data-weather-bart/bart_physical_2_csv{}".format(
            KeyFileName), format="csv")
except:
    pass
