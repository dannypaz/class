#! usr/bin/env python
from twitter import *
import os
import yaml
import json
import boto3


def insert_twitter_firehouse():
    """Insert twitter tweets into s3 via Amazon kinesis firehose."""
    credentials = yaml.load(open(os.path.expanduser(
                '~/.ssh/api_credentials.yml')))
    # authenticate with Twitter
    twitter_stream = TwitterStream(auth=OAuth(**credentials['twitter']))
    # use boto here
    client = boto3.client('firehose', region_name='us-east-1')
    print(client)
    # #get Twitter tweets
    sample = twitter_stream.statuses.sample()
    while True:
        for tweet in sample:
            try:
                tweet['delete']  # this will find deleted tweets
                # and not insert them into
                print('Found a deleted tweet')
            except:
                try:
                    client.put_record(
                                DeliveryStreamName='twitter-streaming-data',
                                Record={'Data': json.dumps(tweet)+'\n'})
                    print('wrote a tweet!')
                except:
                    pass
                    print('could not write to kinesis')
    print('Exited the while loop')


if __name__ == '__main__':
    insert_twitter_firehouse()
