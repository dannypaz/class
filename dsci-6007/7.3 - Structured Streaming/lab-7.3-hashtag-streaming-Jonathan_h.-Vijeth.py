## ssh using two separate terminals into your EMR cluster


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json




def map_hashtag_to_num(x):
    """ Input an individual tweet
    Output: each hastag followed by the number one."""
    try:
        entity = json.loads(x)
        try:
            entity = entity['entities']
            if entity is not None and (entity['hashtags'] is not None
                                        or len(entity['hashtags']) != 0):
                for hashtags in entity['hashtags']:
                    return(hashtags['text'].lower().encode('utf-8'), 1)
            else:
                pass
        except (KeyError, TypeError):
            pass
    except ValueError:
        pass

def updateFunction(newValues, runningCount):
    """Update dstream state to get running total"""
    if runningCount is None:
        runningCount = 0
    print(newValues,'newvalues', runningCount,'running count')
    return sum(newValues, runningCount)

def main(sc, filename):
    """The main function to run on our stdinexport
    Input: files that contain raw tweets_
    Output: a sorted list of each tweet and the number of times it occurs"""
    hashtags = filename.flatMap(lambda x: x.split('\n'))
    tweets_num = hashtags.map(map_hashtag_to_num).filter(
                                    lambda x: x != None)
    tweet_num_agg = tweets_num.reduceByKey(lambda a, b: a+b)
    sorted_tweets = tweet_num_agg.transform(
        (lambda foo: foo
            .sortBy(lambda x: (-x[1]))))
    sorted_tweets.pprint()
    #runningCounts = tweet_num_agg.updateStateByKey(updateFunction)

    #runningCounts.pprint()



sc = SparkContext("local[2]")
ssc = StreamingContext(sc,10)
sc.setLogLevel('ERROR') #only log errors
lines = ssc.socketTextStream("localhost", 9995)


checkpointDirectory = "s3a://twitter-streaming02062017/checkpoint-streaming-spark-hashtags"
# Get StreamingContext from checkpoint data or create a new one
StreamingContext.checkpoint(ssc, checkpointDirectory)

main(ssc, lines)
# start streaming
ssc.start()
ssc.awaitTermination()
