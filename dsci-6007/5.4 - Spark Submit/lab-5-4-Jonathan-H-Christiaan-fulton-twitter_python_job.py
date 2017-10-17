#!usr/bin/end python
# To run this file, you first need to ssh into your master node for the EMR
# cluster that you created. Once inside the EMR cluster, you can confirm that
# you have pyspark installed by typing 'pyspark' to launch the pyspark IDE.
# Next, you can secure copy, or paste into the text editor the code below that
# will calculate the top ten hashtags from all of the twiiter data available
# (~ 80 Gig as of this writing.) Finally, to submit a job, type spark-submit
# and the name of the python file.
# This command will return the top 10 hashtags to a text file.
# Info http://blog.appliedinformaticsinc.com/how-to-write-spark-applications-in-python/
from pyspark import SparkConf, SparkContext
import sys
import json
import pickle
__author__ = 'Jonathan Hilgart'


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

    except ValueError:
        pass


def main(sc, filename):
    """The main function to run on our stdinexport
    Input: files that contain raw tweets_
    Output: a sorted list of each tweet and the number of times it occurs"""
    hashtags = filename.flatMap(lambda x: x.split('/n'))
    tweets_num = hashtags.map(map_hashtag_to_num).filter(
                                    lambda x: x != None)
    tweet_num_agg = tweets_num.reduceByKey(lambda a, b: a+b)
    hash_num_agg_sorted = tweet_num_agg.takeOrdered(20, key=lambda x: -x[1])
    with open('top_ten.txt', 'wb') as fp:
        pickle.dump(hash_num_agg_sorted, fp)
    return hash_num_agg_sorted


if __name__ == "__main__":
    sc = SparkContext()
    filename = sc.textFile(
        "s3a://twitter-streaming02062017/twitter2017/02/*/*/*")
    # Execute Main functionality
    main(sc, filename)
