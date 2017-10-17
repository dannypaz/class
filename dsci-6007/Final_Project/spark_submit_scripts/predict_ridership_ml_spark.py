from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import explode, from_unixtime, from_json
from pyspark.sql import SQLContext, column, SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.types import DateType
from pyspark import SparkConf, SparkContext  # for running spark-submit job
import time
import pytz
import datetime
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.feature import VectorIndexer, StringIndexer, VectorAssembler
from pyspark.ml.evaluation import RegressionEvaluator
import os
__author__ = 'Jonathan Hilgart'


# convert string into datetime format
def change_time_format(time):
    """Take in a month, day, year format and return year, month,
    day format as DateType"""
    month = time[:2]
    day = time[3:5]
    year = time[6:]
    date_time = datetime.datetime(int(year), int(month), int(day))
    return date_time


def live_bart_station_map(col):
    """Change the mapping for the livr bart predictions to match the
    index numbers used in the ml model."""
    live_bart_station_mapping = \
        {"North Concord/Martinez": 0, 'Powell St.': 1,
         'Civic Center/UN Plaza': 2,
        '16th St. Mission': 3, 'Union City': 4, 'Downtown Berkeley': 5,
        'El Cerrito Plaza': 6, 'Castro Valley': 7, 'Glen Park (SF)': 8,
        'Embarcadero': 9, 'San Leandro': 10, 'Rockridge': 11, 'South Hayward': 12,
        'Fruitvale': 13, 'Lake Merritt': 14, 'Daly City': 15, 'Walnut Creek': 16,
        'Fremont': 17, 'Ashby': 18, "Oakland Int'l Airport": 19, 'Concord': 20,
        "San Francisco Int'l Airport": 21, 'Pittsburg/Bay Point': 22,
        'El Cerrito del Norte': 23, 'West Dublin/Pleasanton': 24,
        '19th St. Oakland': 25, 'South San Francisco': 26, 'San Bruno': 27,
        "North Berkeley": 28, "Pleasant Hill/Contra Costa Centre": 29,
        "Montgomery St.": 30, "Colma": 31, "Dublin/Pleasanton": 32,
        "West Oakland": 33, "Millbrae": 34, "Orinda": 35, "MacArthur":36,
        "Hayward": 37, "Lafayette": 38, "Coliseum": 39, "Richmond": 40,
        "Bay Fair": 41, "Balboa Park": 42, "24th St. Mission": 43,
        '12th St. Oakland City Center': 44}
    try:
        return live_bart_station_mapping[col]
    except:
        return -1  # don't have this station but a null will break the ML model

def bart_station_map(col):
    """Change the station names from BART historical data into an index"""
    historic_station_map = {'NCON':0, 'POWL':1, 'CIVC':2, '16TH': 3,
                            'UCTY': 4, 'DBRK': 5,
    'PLZA': 6, 'CAST': 7, 'GLEN': 8, 'EMBR': 9, 'SANL':  10, 'ROCK': 11,
    'SHAY': 12, 'FTVL': 13, 'LAKE': 14, 'DALY': 15, 'WCRK':16, 'FRMT': 17,
    "ASHB": 18, "OAKL": 19, "CONC": 20, "SFIA": 21, "PITT": 22, "DELN": 23,
    "WDUB": 24, "19TH": 25, "SSAN": 26, "SBRN": 27, "NBRK": 28, "PHIL": 29,
    "MONT": 30, "COLM": 31, "DUBL": 32, "WOAK": 33, "MLBR": 34, "ORIN": 35,
    "MCAR": 36, "HAYW": 37, "LAFY": 38, "COLS": 39, "RICH": 40, "BAYF": 41,
    "BALB": 42, "24TH": 43, "12TH": 44 }
    try:
        return historic_station_map[col]
    except:
        return -1 # don't have this station but a null will break the ML model





# Read in the bart data
def read_in_data():
    """Read in bart and weather historic data and
    return a dataframe ready for machine learning"""
    bart_df = spark.read.csv(
        "s3a://raw-data-2016-bart-weather/bart-data2016/date-hour-soo-dest-2016.csv")
    bart_trans_df = bart_df.select(
        col("_c0").alias('date'), col("_c1").alias("hour"), col("_c2").alias(
            "origin_station"), col("_c3").alias("destination_station"),
            col("_c4").alias("people"), dayofmonth(col("_c0")).alias(
                "day_of_month"), month(col("_c0")).alias("month_n"))
    bart_fix_types_df = bart_trans_df.withColumn(
        "people", bart_trans_df['people'].cast(IntegerType()))

    #grouped_bart_df =
    bart_grouped = bart_fix_types_df.groupby(
        "month_n", 'day_of_month', 'destination_station').sum('people')
    bart_grouped_rename = bart_grouped.select(
        "month_n", "day_of_month", "destination_station",
                col("sum(people)").alias("total_exits"))

    ### read in the weather data
    weather_df = spark.read.csv(
        "s3a://raw-data-2016-bart-weather/weather-data-2016/weather-historical-2016-sf"
        , header=True)
    weather_select = weather_df.select(
        "temp-avg", 'temp-low', 'temp-high',
        'humidity-avg', 'seapress-avg', 'wind-avg', 'precip-inches',
        dayofmonth(col('Month')).alias("day_of_month_weather"),
        month(col("Month")).alias("month_n_weather"))
    grouped_data = weather_select.join(bart_grouped_rename, on =
        [weather_select["month_n_weather"] == bart_grouped_rename["month_n"], \
        weather_select["day_of_month_weather"] ==
        bart_grouped_rename["day_of_month"]])

    # create a final DF for the ML model
    ml_df = grouped_data.select("temp-avg", "temp-low", "temp-high",
        "humidity-avg", "seapress-avg", "wind-avg", "precip-inches",
         "month_n", "day_of_month", "destination_station", "total_exits")
    ##cast to the preset integers per station
    # index the bart station
    ml_df = ml_df.withColumn("indexed_stations_udf",
                    bart_indexer_historic(ml_df['destination_station']))

    bart_trans_df.withColumn("people",
                             bart_trans_df['people'].cast(IntegerType()))
    # set columns as integers
    ml_df = ml_df.withColumn("temp-avg", ml_df['temp-avg'].cast(IntegerType()))
    ml_df = ml_df.withColumn("temp-low", ml_df['temp-low'].cast(IntegerType()))
    ml_df = ml_df.withColumn("temp-high",
                             ml_df['temp-high'].cast(IntegerType()))
    ml_df = ml_df.withColumn("humidity-avg",
                             ml_df['humidity-avg'].cast(IntegerType()))
    ml_df = ml_df.withColumn("seapress-avg",
                             ml_df['seapress-avg'].cast(IntegerType()))
    ml_df = ml_df.withColumn("wind-avg",
                             ml_df['wind-avg'].cast(IntegerType()))
    ml_df = ml_df.withColumn("precip-inches",
                             ml_df['precip-inches'].cast(IntegerType()))
    return ml_df


def train_gb_model(input_df, number_iterations=100):
    """  Train a gradient boost model from the bart and weather data.
    Return the trained model, and the rmse from the train test split"""
    ml_df.cache()
    # train test split
    trainingData, testData = ml_df.randomSplit([0.7, 0.3])
    train_rows = trainingData.count()
    test_rows = testData.count()
    trainingData.cache()
    testData.cache()
    gb_assembler = VectorAssembler(inputCols=['temp-avg', 'temp-low',
        'temp-high', 'seapress-avg', 'humidity-avg', 'wind-avg',
        'precip-inches', 'month_n', 'day_of_month', 'indexed_stations_udf'],
                                   outputCol="features")
    training = gb_assembler.transform(trainingData).select(
        col("features"), col("total_exits").alias("label-exits"))
    # cache the model to test hyperparameters
    training.cache()
    # This takes ~15 minutes to run
    gb_model = GBTRegressor(labelCol="label-exits",
                            featuresCol="features",
                            maxIter=number_iterations, maxDepth=3, maxBins=50)
    gb_model_trained = gb_model.fit(training)
    testing = gb_assembler.transform(testData).select(
        col("features"), col("total_exits").alias("label-exits-true"))
    # cache the model to test hyperparameters
    testing.cache()
    prediction = gb_model_trained.transform(testing)
    predicted = prediction.select(
        col("features"),"prediction","label-exits-true")
    evaluator = RegressionEvaluator(
        labelCol = "label-exits-true", predictionCol="prediction",
        metricName="rmse")
    rmse = evaluator.evaluate(predicted)
    print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)

    return gb_model_trained, rmse


def live_bart_weather_data(sf_year_yes,sf_month_yes,sf_day_yes):
    """Read in bart data and weather data from yesterday.
    Returns a combined dataframe ready to make predictions off of"""
    # bart data from yesterday
    bart_arrival = spark.read.parquet(
        "s3a://normalized-data-weather-bart/bart_arrival_0_{}/{}/{}/*".format(
        sf_year_yes, sf_month_yes, sf_day_yes))
    bart_physical = spark.read.parquet(
        "s3a://normalized-data-weather-bart/bart_physical_0_{}/{}/{}/*".format(
        sf_year_yes, sf_month_yes, sf_day_yes))
    # weather data from yesterday (would fix to today if given enough time)
    wind_table = spark.read.parquet(
        "s3a://normalized-data-weather-bart/wind_df{}/{}/{}/*".format(
        sf_year_yes, sf_month_yes, sf_day_yes))
    main_temp_table = spark.read.parquet(
        "s3a://normalized-data-weather-bart/main-temp{}/{}/{}/*".format(
        sf_year_yes, sf_month_yes, sf_day_yes))
    weather_description_table = spark.read.parquet(
        "s3a://normalized-data-weather-bart/weather-description{}/{}/{}/*".format(
        sf_year_yes, sf_month_yes, sf_day_yes))
    # alias bart columns
    bart_arrival_renamed = bart_arrival.select(
        col('origin_station_0').alias('origin_station_arrival'),
        col("sf_time_0").alias("sf_time_arrival"),
        col("date_0").alias("date_arrival"),
        col("direction_0").alias("direction_arrival"),
        col("hour_0").alias("hour_arrival"),
        col("minutes_til_arrival_0").alias(
                            "minutes_til_arrival_bart_arrival"))
    # join bart tables together
    joined_bart_arrival_physical_df = bart_arrival_renamed.join(bart_physical,
        on = [bart_physical['origin_station_0'] ==
        bart_arrival_renamed['origin_station_arrival'],
        bart_physical['sf_time_0'] ==
        bart_arrival_renamed['sf_time_arrival'],
        bart_physical['direction_0'] ==
        bart_arrival_renamed['direction_arrival'],
        bart_physical['date_0'] ==
        bart_arrival_renamed['date_arrival']])
    # select columns I want
    final_joined_bart_df = joined_bart_arrival_physical_df.select(
        "origin_station_0", "sf_time_0", "date_0", "direction_0",
        "destination_0", "hour_0", "color_0", "bike_flag_0",
        "train_size_0", "capacity_0", "minutes_til_arrival_bart_arrival")
    ## convert the string date to datetime format
    final_joined_bart_df_dt = final_joined_bart_df.withColumn(
        'date_0', change_time(col('date_0')))
    final_bart_df = final_joined_bart_df_dt.select(
        dayofmonth(col('date_0')).alias("day_of_month"),
        month(col("date_0")).alias("month_n"), "origin_station_0",
        "sf_time_0", "date_0", "direction_0", "hour_0", "bike_flag_0",
        "train_size_0", "capacity_0", "minutes_til_arrival_bart_arrival")
    # register as table to run SQL
    final_bart_df.createOrReplaceTempView("final_bart")
    final_bart_df = spark.sql("""SELECT count(bike_flag_0) as
        total_number_of_trains, origin_station_0, date_0,direction_0,
        SUM (train_size_0) as total_number_train_cars,
        sum(capacity_0) as total_capacity, month_n, day_of_month
         FROM final_bart
            WHERE minutes_til_arrival_bart_arrival <5
            GROUP BY origin_station_0,date_0,direction_0, month_n, day_of_month
            ORDER BY total_capacity DESC""")
    # bring in weather data to ultimately join with bart data
    # and create a ML dataframe to feed into GBoost model
    wind_table_alias = wind_table.select(col("hour").alias("hour_wind"),
                                         col("date").alias("date_wind"),
                                         "speed", "deg")
    wind_temp_table = wind_table_alias .join(main_temp_table,
        on = [wind_table_alias['hour_wind'] == main_temp_table['hour'],
        wind_table_alias['date_wind'] == main_temp_table['date']])
    wind_temp_table_final = wind_temp_table.select("hour", "date", 'humidity',
                    "speed", "deg", "pressure", "temp", "temp_max", "temp_min")
    weather_des_final = weather_description_table.select(
        col("col").alias('weather_des'), "hour", "date")
    weather_des_final.registerTempTable("weather_des_final")
    weather_des_ints = spark.sql("""SELECT hour as hour_des,date as
                                      date_des,weather_des,
         CASE WHEN weather_des = 'Rain' THEN 1.0
             WHEN weather_des = 'Mist' THEN .1
             ELSE 0.0 end as weather_precip
           FROM  weather_des_final""")
    weather_des_ints_final = weather_des_ints.select("hour_des",
                                         "date_des", "weather_precip")
    # join weather des with the other two weather table
    combo_df = wind_temp_table_final.join(weather_des_ints_final,
        on = [wind_temp_table_final['date'] ==
        weather_des_ints_final['date_des'], wind_temp_table_final['hour'] ==
        weather_des_ints_final['hour_des']])
    #select the columns you want
    final_df = combo_df.select("hour",
                               "date", "speed", "deg", "pressure", "temp",
                               "temp_max", "temp_min", "weather_precip")
    # convert the date string into the date format for spark
    combo_df = combo_df.withColumn('date', change_time(col('date')))
    # finally, select all of the columns
    # drop duplicates to ensure we only have only weather forecast per hour
    final_weather_df = combo_df.select(dayofmonth(col('date')).alias(
        "day_of_month_weather"), month(col("date")).alias("month_n_weather"),
        "hour", "date", "speed", "deg", "pressure", "temp", "temp_max",
        "temp_min", "weather_precip", "humidity").dropDuplicates(
        ['day_of_month_weather', 'month_n_weather', 'hour'])
    final_weather_df.cache()
    final_bart_df.cache()
    temp_table = final_weather_df.join(final_bart_df,
        on = [final_weather_df['date'] == final_bart_df['date_0']])
    final_bart_weather_table = temp_table.select("day_of_month", "month_n",
        "total_capacity", "total_number_train_cars", "direction_0",
        "date_0", "origin_station_0", "weather_precip", "speed", "deg",
        "pressure", "temp", "temp_max", "temp_min", "humidity")
    # index our bart stations to match the order in our ML algorithm
    final_bart_weather_table_stat = final_bart_weather_table.withColumn(
        "indexed_stations", bart_data_reformat_columns(col("origin_station_0")))
    # 150 people per train is a more realistic assumption of
    final_bart_weather_table_ml = final_bart_weather_table_stat.withColumn(
        'daily_capacity', col("total_number_train_cars")*150).dropna()
    return final_bart_weather_table_ml


def make_predictions_today(input_df,historic_bart_df,trained_model):
    """Take in the bart data and weather data from yesterday (input df)
    and generate predictions
    of station capacity using the trained model"""
    bart_weather_current_assembler = VectorAssembler(inputCols=['temp',
        'temp_min','temp_max', 'humidity', 'pressure', 'speed',
         'weather_precip','month_n', 'day_of_month', 'indexed_stations'],
         outputCol="features")
    # Can only do total exits per station,not direction of exits (i.e.
    # north or south)
    live_bart_weather_testing = bart_weather_current_assembler.transform(
        input_df).select(
        col("features"), col("origin_station_0"), col("date_0"))
    ## create predictions
    prediction_live = trained_model.transform(live_bart_weather_testing)
    predicted_live = prediction_live.select("prediction", "origin_station_0",
                                            "date_0")
    ## get the capacity prediction for yesterday and change prediction to exits
    predicted_live = predicted_live.withColumn("total-predicted-exits",
                                               round(col("prediction"),3))
    predicted_live = predicted_live.where(col('date_0') ==
                                          KeyFileName_yesterday)
    predicted_live = predicted_live.withColumn('prediction',
                            round(col('prediction'), 3))
    live_ridership = predicted_live.toPandas()
    total_capacity = input_df.select("origin_station_0",
                                     "daily_capacity", "date_0").toPandas()
    #historic_df = historic_bart_df.select("origin_station_0","date_0",)
    final_historic_live_df = total_capacity.merge(live_ridership,
                                                  on=['origin_station_0',
                                                      'date_0'])

    ## ensure one prediction per station for the date
    final_historic_live_grouped = final_historic_live_df.groupby(
         ['origin_station_0', 'date_0']).mean().reset_index()
    final_historic_live_grouped['station'] = final_historic_live_grouped[
        'origin_station_0'
    ]
    final_historic_live_grouped['date'] = final_historic_live_grouped['date_0']

    # ## get the percent occupancy
    final_historic_live_grouped['percent_capacity'] = \
    final_historic_live_grouped.apply(lambda x:
                                       x['total-predicted-exits'] /
                                       x['daily_capacity'] if
                             x['total-predicted-exits']/
                             x['daily_capacity'] <= 1.0 else 1.0, axis=1)

    final_historic_live_grouped.sort_values("percent_capacity",
                                            ascending=False, inplace=True)
    final_historic_df = final_historic_live_grouped.loc[:,
        ('station', 'daily_capacity', 'total-predicted-exits',
         'percent_capacity')]
    final_historic_df['percent_capacity'] = \
        final_historic_df['percent_capacity']*100

    return final_historic_df


if __name__ =='__main__':
    # get the current day, and yesterday information to make predictions off
    # of
    # use yseterday's capacity per bart station for the prediction
    # of today's capacity
    # (This assumes all days are the same for number of trains per station)
    # # when running spark-submit, need to create the spark context
    sc = SparkContext()
    spark = SparkSession(sc)
    sqlContext = SQLContext(sc)

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
    if len(str(sf_month_today)) < 2:
        sf_month_today = '0'+str(sf_month_today)
    if len(str(sf_day_today)) < 2:
        sf_day_today= '0'+str(sf_day_today)
    # to group against for the bart and weather data
    KeyFileName_today = "{}-{}-{}".format(
        sf_year_today, sf_month_today, sf_day_today)
    KeyFileName_yesterday = "{}-{}-{}".format(
        sf_year_yesterday, sf_month_yesterday, sf_day_yesterday)
    # define the UDFs
    bart_data_reformat_columns = udf(live_bart_station_map, IntegerType())
    bart_indexer_historic = udf(bart_station_map, IntegerType())
    change_time = udf(change_time_format, DateType())
    # read in historical data
    ml_df = read_in_data()
    # train the gboost model
    trained_gb_model, rmse_gb = train_gb_model(ml_df)
    # combine the live data from bart and the weather
    final_bart_weather_df = \
    live_bart_weather_data(sf_year_yesterday, sf_month_yesterday,
                           sf_day_yesterday)
    # create predictions from the live data
    final_df_predicted_capacity = \
        make_predictions_today(final_bart_weather_df, ml_df, trained_gb_model)
    # get capacity and rider information
    total_daily_capacity = final_df_predicted_capacity['daily_capacity'].sum()
    total_predicted_daily_riders = \
        final_df_predicted_capacity['total-predicted-exits'].sum()
    # delete the previous file
    #os.remove(os.path.expanduser("~/predicted_capacity"))
    # save to html
    with open(os.path.expanduser("~/predicted_capacity"), "w") as fp:
        fp.write("""<h1><em>BART Station Predictions Based Upon Current Weather
                 </em></h1>""")
        fp.write("<p>Updated on {}/{}/{} at SF time= {}:{}</p>".format(
            sf_month_today, sf_day_today, sf_year_today,
        datetime.datetime.now(SF_time).hour,
        datetime.datetime.now(SF_time).minute))
        fp.write("""<h2>For a full description of how this system works,
                 check out my  <a href =https://github.com/jonhilgart22/galvanize-projects/blob/master/Data_Engineering/Daily_Bart_Ridership_Predictions.ipynb
                 >github. </a></h2>""")
        fp.write("""<p> Below is a daily live prediction of the number of people
                 that will exit a given bart station. This data utilizes one
                 year of hourly exits per station access at
                 <a href =http://www.bart.gov/about/reports/ridership>BART data</a>.
                  Alongside these
                  ridership numbers, one year of historical weather
                  for San Francisco was used accessed at
                  <a href=https://www.wunderground.com/history/>weather data.</a></p>""")
        fp.write("""<p> This historic data was fed into a
                 MLlib gradient boosted tree model (300 trees) to predict
                 ridership
                 per station.</p>""")
        fp.write("""<p>This model is updated daily. The total capacity is taken
                 from the total number of trains that arrived at each station
                 times 150 people per train. Alongside this, the weather
                 pulled from midnight is used as the weather prediction.</p>""")
        fp.write("""<h3>Today, it is predicted that {:,} people will ride BART.
                 In addition, today BART has capacity for {:,} people.</h3>""".format(
                     total_predicted_daily_riders, total_daily_capacity
                 ))
        fp.write("""<p> Below the predictions, you can see an architecture
                 of the system.</p>""")
        fp.write(final_df_predicted_capacity.to_html())
        fp.write("""<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile userAgent=\&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36\&quot; version=\&quot;6.2.7\&quot; editor=\&quot;www.draw.io\&quot; type=\&quot;google\&quot;&gt;&lt;diagram name=\&quot;Page-1\&quot;&gt;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&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://www.draw.io/embed2.js?s=flowchart&"></script>
                 """)
