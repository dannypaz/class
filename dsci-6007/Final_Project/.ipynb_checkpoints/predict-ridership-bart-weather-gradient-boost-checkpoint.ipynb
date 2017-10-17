{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import *\n",
    "from pyspark.sql.types import *\n",
    "from pyspark.ml import Pipeline\n",
    "from pyspark.ml.regression import GBTRegressor\n",
    "from pyspark.ml.feature import VectorIndexer,StringIndexer, VectorAssembler\n",
    "from pyspark.ml.evaluation import RegressionEvaluator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "bart_df = spark.read.csv(\"s3a://raw-data-2016-bart-weather/bart-data2016/date-hour-soo-dest-2016.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "bart_trans_df = bart_df.select(col(\"_c0\").alias('date'),col(\"_c1\").alias(\"hour\"),col(\"_c2\").alias(\"origin_station\"),\n",
    "                         col(\"_c3\").alias(\"destination_station\"),col(\"_c4\").alias(\"people\"),\n",
    "                         dayofmonth(col(\"_c0\")).alias(\"day_of_month\"),month(col(\"_c0\")).alias(\"month_n\") )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "bart_fix_types_df =bart_trans_df.withColumn(\"people\",bart_trans_df['people'].cast(IntegerType()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "#grouped_bart_df = \n",
    "bart_grouped = bart_fix_types_df.groupby(\"month_n\",'day_of_month','destination_station').sum('people')\n",
    "bart_grouped_rename = bart_grouped.select(\"month_n\",\"day_of_month\",\"destination_station\",\n",
    "                                          col(\"sum(people)\").alias(\"total_exits\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+------------+-------------------+-----------+\n",
      "|month_n|day_of_month|destination_station|total_exits|\n",
      "+-------+------------+-------------------+-----------+\n",
      "|      1|           4|               CIVC|      19792|\n",
      "|      1|          13|               19TH|      13751|\n",
      "|      1|          19|               POWL|      26823|\n",
      "|      1|          25|               DALY|       8902|\n",
      "|      1|          25|               RICH|       4443|\n",
      "|      1|          26|               24TH|      14010|\n",
      "|      1|          27|               ASHB|       5870|\n",
      "|      1|          31|               16TH|       6650|\n",
      "|      2|          18|               WDUB|       3675|\n",
      "|      2|          20|               12TH|       5378|\n",
      "|      2|          22|               DELN|       9488|\n",
      "|      2|          22|               ORIN|       3097|\n",
      "|      2|          29|               SHAY|       3196|\n",
      "|      3|          29|               ORIN|       3196|\n",
      "|      4|           5|               EMBR|      47860|\n",
      "|      4|          19|               LAFY|       4020|\n",
      "|      4|          20|               SANL|       6426|\n",
      "|      4|          20|               PITT|       6742|\n",
      "|      4|          22|               ASHB|       5130|\n",
      "|      4|          27|               SSAN|       4055|\n",
      "+-------+------------+-------------------+-----------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# ready for our model\n",
    "bart_grouped_rename.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "## Next bring in the weather data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "weather_df = spark.read.csv(\"s3a://raw-data-2016-bart-weather/weather-data-2016/weather-historical-2016-sf\",header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "weather_select = weather_df.select(\"temp-avg\",'temp-low','temp-high',\n",
    "                                   'humidity-avg','seapress-avg','wind-avg','precip-inches',\n",
    "                                   dayofmonth(col('Month')).alias(\"day_of_month_weather\"),\n",
    "                                  month(col(\"Month\")).alias(\"month_n_weather\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "grouped_data = weather_select.join(bart_grouped_rename, on =\n",
    "                                  [weather_select[\"month_n_weather\"]==bart_grouped_rename[\"month_n\"], \\\n",
    "                                   weather_select[\"day_of_month_weather\"]==bart_grouped_rename[\"day_of_month\"]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "ml_df = grouped_data.select(\"temp-avg\",\"temp-low\",\"temp-high\",\"humidity-avg\",\"seapress-avg\",\"wind-avg\",\n",
    "                    \"precip-inches\",\"month_n\",\"day_of_month\",\"destination_station\",\"total_exits\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "## Index the string station name to a numeric name\n",
    "ml_df =StringIndexer(inputCol=\"destination_station\", outputCol=\"indexedStation\").fit(ml_df ).transform(ml_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+--------+---------+------------+------------+--------+-------------+-------+------------+-------------------+-----------+--------------+\n",
      "|temp-avg|temp-low|temp-high|humidity-avg|seapress-avg|wind-avg|precip-inches|month_n|day_of_month|destination_station|total_exits|indexedStation|\n",
      "+--------+--------+---------+------------+------------+--------+-------------+-------+------------+-------------------+-----------+--------------+\n",
      "|      52|      50|       54|          85|        30.2|       7|            0|      1|          10|               CAST|        881|          24.0|\n",
      "|      54|      48|       59|          77|       30.13|      15|         0.33|      1|          13|               19TH|      13751|          22.0|\n",
      "+--------+--------+---------+------------+------------+--------+-------------+-------+------------+-------------------+-----------+--------------+\n",
      "only showing top 2 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "ml_df.show(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "# confirm that our groupby worked\n",
    "# ml_df.where((col(\"month_n\")==1) & (col(\"destination_station\")=='CIVC')) .show(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DataFrame[date: string, hour: string, origin_station: string, destination_station: string, people: int, day_of_month: int, month_n: int]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bart_trans_df.withColumn(\"people\",bart_trans_df['people'].cast(IntegerType()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DataFrame[temp-avg: int, temp-low: int, temp-high: int, humidity-avg: int, seapress-avg: int, wind-avg: int, precip-inches: int, month_n: int, day_of_month: int, destination_station: string, total_exits: bigint, indexedStation: double]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# set columns as integers\n",
    "ml_df = ml_df.withColumn(\"temp-avg\",ml_df['temp-avg'].cast(IntegerType()))\n",
    "ml_df = ml_df.withColumn(\"temp-low\",ml_df['temp-low'].cast(IntegerType()))\n",
    "ml_df = ml_df.withColumn(\"temp-high\",ml_df['temp-high'].cast(IntegerType()))\n",
    "ml_df = ml_df.withColumn(\"humidity-avg\",ml_df['humidity-avg'].cast(IntegerType()))\n",
    "ml_df = ml_df.withColumn(\"seapress-avg\",ml_df['seapress-avg'].cast(IntegerType()))\n",
    "ml_df = ml_df.withColumn(\"wind-avg\",ml_df['wind-avg'].cast(IntegerType()))\n",
    "ml_df = ml_df.withColumn(\"precip-inches\",ml_df['precip-inches'].cast(IntegerType()))\n",
    "ml_df.cache()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 5702 rows of training and 2487 rows of testing data\n"
     ]
    }
   ],
   "source": [
    "trainingData, testData = ml_df.randomSplit([0.7, 0.3])\n",
    "train_rows = trainingData.count()\n",
    "test_rows = testData.count()\n",
    "print(\"There are {} rows of training and {} rows of testing data\".format(train_rows,test_rows))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+-----------+\n",
      "|            features|label-exits|\n",
      "+--------------------+-----------+\n",
      "|[51.0,45.0,56.0,5...|       4301|\n",
      "|[51.0,48.0,54.0,5...|       6650|\n",
      "|[52.0,50.0,54.0,8...|        881|\n",
      "|[53.0,45.0,60.0,7...|       5378|\n",
      "|[54.0,49.0,58.0,8...|       8902|\n",
      "|[54.0,49.0,58.0,8...|       4443|\n",
      "|[55.0,49.0,60.0,7...|       8070|\n",
      "|[56.0,47.0,64.0,6...|       3196|\n",
      "|[56.0,49.0,62.0,7...|       7982|\n",
      "|[56.0,50.0,61.0,7...|       3675|\n",
      "|[58.0,48.0,68.0,7...|       9488|\n",
      "|[58.0,52.0,63.0,8...|       7252|\n",
      "|[58.0,53.0,62.0,8...|       5130|\n",
      "|[58.0,53.0,62.0,8...|      26823|\n",
      "|[59.0,53.0,64.0,6...|       6202|\n",
      "|[59.0,53.0,65.0,7...|       5321|\n",
      "|[60.0,52.0,67.0,8...|       3196|\n",
      "|[60.0,52.0,68.0,8...|       4675|\n",
      "|[60.0,53.0,67.0,8...|       1566|\n",
      "|[61.0,54.0,67.0,8...|       9282|\n",
      "+--------------------+-----------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DataFrame[features: vector, label-exits: bigint]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gb_assembler = VectorAssembler(inputCols=['temp-avg',\n",
    " 'temp-low',\n",
    " 'temp-high',\n",
    " 'humidity-avg',\n",
    " 'seapress-avg',\n",
    " 'wind-avg',\n",
    " 'precip-inches',\n",
    " 'month_n',\n",
    " 'day_of_month',\n",
    " 'indexedStation',\n",
    " 'total_exits'], outputCol=\"features\")\n",
    "training = gb_assembler.transform(trainingData).select(col(\"features\"),col(\"total_exits\").alias(\"label-exits\"))\n",
    "training.show()\n",
    "## cache the model to test hyperparameters\n",
    "training.cache()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "gb_model = GBTRegressor(labelCol=\"label-exits\",featuresCol=\"features\",maxIter=200,maxDepth=3,maxBins=50)\n",
    "gb_model_trained = gb_model.fit(training)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+----------------+\n",
      "|            features|label-exits-true|\n",
      "+--------------------+----------------+\n",
      "|[52.0,46.0,57.0,8...|           14010|\n",
      "|[53.0,47.0,58.0,8...|           19792|\n",
      "|[54.0,48.0,59.0,7...|           13751|\n",
      "|[55.0,49.0,60.0,7...|            4055|\n",
      "|[55.0,49.0,61.0,8...|            5870|\n",
      "|[58.0,48.0,68.0,7...|            3097|\n",
      "|[61.0,56.0,65.0,7...|            6519|\n",
      "|[65.0,50.0,79.0,5...|           47860|\n",
      "|[67.0,55.0,78.0,6...|           14987|\n",
      "|[71.0,57.0,84.0,5...|            3357|\n",
      "|[54.0,45.0,63.0,7...|            4644|\n",
      "|[56.0,47.0,64.0,6...|            6931|\n",
      "|[58.0,53.0,62.0,8...|            5674|\n",
      "|[59.0,48.0,70.0,6...|            5529|\n",
      "|[60.0,48.0,71.0,7...|            7056|\n",
      "|[61.0,52.0,70.0,7...|            5581|\n",
      "|[61.0,56.0,65.0,7...|           28433|\n",
      "|[61.0,56.0,66.0,8...|            1331|\n",
      "|[63.0,55.0,70.0,7...|            9299|\n",
      "|[67.0,54.0,80.0,9...|            8399|\n",
      "+--------------------+----------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DataFrame[features: vector, label-exits-true: bigint]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testing = gb_assembler.transform(testData).select(col(\"features\"),col(\"total_exits\").alias(\"label-exits-true\"))\n",
    "testing.show()\n",
    "## cache the model to test hyperparameters\n",
    "testing.cache()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------------------+------------------+----------------+\n",
      "|            features|        prediction|label-exits-true|\n",
      "+--------------------+------------------+----------------+\n",
      "|[52.0,46.0,57.0,8...|14151.195758889318|           14010|\n",
      "|[53.0,47.0,58.0,8...|22589.490141147173|           19792|\n",
      "|[54.0,48.0,59.0,7...|13655.782118741836|           13751|\n",
      "|[55.0,49.0,60.0,7...|4073.5359256222882|            4055|\n",
      "|[55.0,49.0,61.0,8...| 5828.050678583003|            5870|\n",
      "|[58.0,48.0,68.0,7...|3040.6595956371975|            3097|\n",
      "|[61.0,56.0,65.0,7...| 6496.733250098102|            6519|\n",
      "|[65.0,50.0,79.0,5...| 50845.08057795934|           47860|\n",
      "|[67.0,55.0,78.0,6...|14350.477385933322|           14987|\n",
      "|[71.0,57.0,84.0,5...|3350.8958005100376|            3357|\n",
      "|[54.0,45.0,63.0,7...| 4827.678057528416|            4644|\n",
      "|[56.0,47.0,64.0,6...| 6881.440379702534|            6931|\n",
      "|[58.0,53.0,62.0,8...|5722.0800705642505|            5674|\n",
      "|[59.0,48.0,70.0,6...| 5461.830648176785|            5529|\n",
      "|[60.0,48.0,71.0,7...|  7089.13204566173|            7056|\n",
      "|[61.0,52.0,70.0,7...| 5663.400811306439|            5581|\n",
      "|[61.0,56.0,65.0,7...| 27832.09753453409|           28433|\n",
      "|[61.0,56.0,66.0,8...| 1483.309106842631|            1331|\n",
      "|[63.0,55.0,70.0,7...|  9154.96286904847|            9299|\n",
      "|[67.0,54.0,80.0,9...| 8272.560834124146|            8399|\n",
      "+--------------------+------------------+----------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "prediction = gb_model_trained.transform(testing)\n",
    "predicted = prediction.select(col(\"features\"),\"prediction\",\"label-exits-true\")\n",
    "predicted.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Root Mean Squared Error (RMSE) on test data = 981.354\n"
     ]
    }
   ],
   "source": [
    "evaluator = RegressionEvaluator(\n",
    "    labelCol=\"label-exits-true\", predictionCol=\"prediction\", metricName=\"rmse\")\n",
    "rmse = evaluator.evaluate(predicted)\n",
    "print(\"Root Mean Squared Error (RMSE) on test data = %g\" % rmse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# save our model\n",
    "gb_model_trained.save(\"s3a://predicting-bart-ridership-model/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda env:dsci6007]",
   "language": "python",
   "name": "conda-env-dsci6007-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
