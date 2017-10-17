
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, SQLContext
import json
import time
# # when running spark-submit, need to create the spark context
sc = SparkContext()
spark = SparkSession(sc)
sqlContext = SQLContext(sc)

twitter_df = sc.textFile("s3a://twitter-streaming02062017/twitter2017/*/*/*/*")

total_tweets = twitter_df.flatMap(lambda x: x.split('\n'))
def find_user_ids(total_ids):
    for user_id in total_ids:
        try:
            json_user = json.loads(user_id)
            try:
                user_info = json_user.get('user')
                try:
                    id = user_info.get('id')
                    return id
                except:
                    pass
            except:
                pass
        except:
            pass
# try:
#     total_ids = twitter_df.flatMap(lambda x: x.split('\n')).map(\
#                                             lambda x: json.loads(x))\
#                                             .map(lambda x: x['user']).map(lambda x: x['id'])
# except Exception as e:
#     print(e)
#     continue
total_ids = total_tweets.map(find_user_ids).filter(lambda x : x != None)

#start time
now = time.time()
distinct_user_ids = total_ids.distinct().count()
end = time.time()
total = end-now


#start time
now = time.time()
apx_distinct_ids = total_ids.countApproxDistinct(.01)
end = time.time()
aprox_time  = end-now

with open('count_distinct_users.txt', 'wb') as fp:
    fp.write(str(apx_distinct_ids) + ' Hyperloglog aprox distinct user ids \n')
    fp.write(str(aprox_time) + ' Hyperloglog time \n')
    fp.write(str(distinct_user_ids) + 'Exact user ids \n')
    fp.write(str(total) + 'Exact count of user ids \n')
