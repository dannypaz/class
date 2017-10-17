#! usr/bin/env python
from pymongo import MongoClient
##connect to pymongo
client = MongoClient()
db = client.twitter ## name of the database
print('There are ',db.streamingtweets.count(),'tweets in the db')
file=open('number_of_tweets.txt','w')
file.write(str(db.streamingtweets.count()))
file.close()
