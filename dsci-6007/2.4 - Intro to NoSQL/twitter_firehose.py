#! usr/bin/env python
from twitter import *
import os
import yaml
from pymongo import MongoClient
#credentials
credentials = yaml.load(open(os.path.expanduser('~/.ssh/api_credentials.yml')))
#authenticate with Twitter
twitter_stream = TwitterStream(auth=OAuth(credentials['twitter'].get('token'),\
 credentials['twitter'].get('token_secret'),\
               credentials['twitter'].get('consumer_key'),credentials['twitter'].get('consumer_secret')))
##connect to pymongo
client = MongoClient()
db = client.twitter ## name of the database
sample=twitter_stream.statuses.sample()
### run through the tweets
try:
    while True:
        t = next(sample)
        db.streamingtweets.insert_one(t) ## insert item into the database
    #in case the while break
    t = next(sample)
    db.streamingtweets.insert_one(t)
except: ## in case the connection breaks
    while True:
        t = next(sample)
        db.streamingtweets.insert_one(t) ## insert item into the database
    #in case the while break
    t = next(sample)
    db.streamingtweets.insert_one(t)
