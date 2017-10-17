#! usr/bin/env python
from twitter import *
import os
import yaml
import psycopg2
import json
from psycopg2.extras import Json

#credentials
credentials = yaml.load(open(os.path.expanduser('~/.ssh/api_credentials.yml')))
#authenticate with Twitter
twitter_stream = TwitterStream(auth=OAuth(credentials['twitter'].get('token'),\
 credentials['twitter'].get('token_secret'),\
               credentials['twitter'].get('consumer_key'),credentials['twitter'].get('consumer_secret')))

# end point for RDS system
database_endpoint = "stream-tweets-db.cbx9xkfcpnfu.us-west-2.rds.amazonaws.com"
db_credentials = credentials['postgresstwitter'].get('db_name')
db_user = credentials['postgresstwitter'].get('user')
db_password=credentials['postgresstwitter'].get('password')

##twitter tweets
sample=twitter_stream.statuses.sample()
### run through the tweets
while True:
    tweet = next(sample)
    try:
        tweet['delete'] ### this will find deleted tweets
    except:
        try:
            #Json will convert the sample into a JSON object
            ##connect to postgress
            conn = psycopg2.connect(dbname=db_credentials,\
            user=db_user,\
            host=database_endpoint,\
            password=db_password)

            cur = conn.cursor()
            cur.execute("""INSERT INTO raw_tweets (status) VALUES (%s)""",[Json(tweet)])
            conn.commit()
            conn.close()
            cur.closer()
            #INSERT INTO bar(first_name,last_name) VALUES (%(first_name)s, %(last_name)s
        except:
            print "I can't SELECT this table"
