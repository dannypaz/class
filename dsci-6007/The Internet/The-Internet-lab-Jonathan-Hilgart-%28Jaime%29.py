
# coding: utf-8

# In[ ]:

#https://gist.github.com/garnaat/833135 - for boto to s3 connection


# In[ ]:

get_ipython().system('/usr/bin/env python')


# In[42]:


import os
import yaml
import pandas as pd
import boto
credentials = yaml.load(open(os.path.expanduser('~/api_credentials.yml')))
#credentials['twitter'].get('consumer_key')


# In[3]:

from twitter import *


# In[5]:

def top_n_tweets_us(n):
    t = Twitter(
    auth=OAuth(credentials['twitter'].get('token'), credentials['twitter'].get('token_secret'),\
               credentials['twitter'].get('consumer_key'),credentials['twitter'].get('consumer_secret')))
    us_trends = t.trends.place(_id=23424977)
    trending_tweets_us = pd.DataFrame([i for i in us_trends[0]['trends']])
    trending_tweets_us = trending_tweets_us.sort_values(by='tweet_volume',ascending=False)
    html_trending_tweets = trending_tweets_us[:n].to_html()
    return html_trending_tweets_tweets



# In[62]:

html_trending_tweets = top_n_tweets_us(10)

# In[63]:

conn = boto.connect_s3()


# In[64]:

conn.get_all_buckets()


# In[57]:

jh_bucket = conn.create_bucket('the_internet')


# In[65]:

error_html = """
<html>
  <head><title>Something is wrong</title></head>
  <body><h2>Something is terribly wrong with my S3-based website</h2></body>
</html>"""


# In[66]:

index_key = jh_bucket.new_key('index.html')
index_key.content_type = 'text/html'
index_key.set_contents_from_string(html_trending_tweets, policy='public-read')

error_key = jh_bucket.new_key('error.html')
error_key.content_type = 'text/html'
error_key.set_contents_from_string(error_html, policy='public-read')


# In[68]:

# Top ten trending tweets in the US
# https://s3.amazonaws.com/the_internet/index.html


# In[ ]:



