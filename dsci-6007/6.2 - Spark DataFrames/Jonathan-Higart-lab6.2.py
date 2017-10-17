
# coding: utf-8

# In[34]:

from pyspark.sql.functions import split, explode


# In[3]:

spark_session = SparkSession     .builder     .appName("Python Spark SQL basic example")     .config("spark.some.config.option", "some-value")     .getOrCreate()


# In[87]:

dataframe_spark = spark_session.read.json("s3a://twitter-streaming02062017/twitter2017/02/23/02/*")


# In[7]:

dataframe_spark.printSchema()


# In[88]:

tweets_dataframe = dataframe_spark.selectExpr('id as tweet_id', 'timestamp_ms', 'user.id AS user_id', 'text')


# In[89]:

user_dataframe = dataframe_spark.selectExpr('user.id','user.name').distinct()
user_dataframe.show()


# In[90]:

hashtags_dataframe = dataframe_spark.selectExpr('entities.hashtags.text as hashtags', 'id as tweet_id')
hashtags_dataframe.show()


# In[91]:

exploded_hashtags_dataframe = hashtags_dataframe.select(hashtags_dataframe['tweet_id'],explode(hashtags_dataframe.hashtags).alias("hashtags"))
exploded_hashtags_dataframe.show()


# In[92]:

#write parquet
tweets_dataframe.write.parquet("s3a://twitter-streaming02062017/parquet_files/tweets_dataframe.parquet")


# In[93]:

#Parquet
hashtags_dataframe.write.parquet("s3a://twitter-streaming02062017/parquet_files/hashtags_dataframe.parquet")
user_dataframe.write.parquet("s3a://twitter-streaming02062017/parquet_files/user_dataframe.parquet")


# In[94]:

exploded_hashtags_dataframe.groupby(exploded_hashtags_dataframe['hashtags']).count().show()


# In[ ]:



