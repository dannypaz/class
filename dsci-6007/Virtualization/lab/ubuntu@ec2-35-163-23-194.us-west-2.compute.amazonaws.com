
# coding: utf-8

# In[ ]:

#https://gist.github.com/garnaat/833135 - for boto to s3 connection


# In[ ]:

#get_ipython().system('/usr/bin/env python')


# In[42]:


import os
import yaml
import pandas as pd
from twitter import *
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
    return trending_tweets_us[:n].to_html('top10.html')








# In[57]:
top_n_tweets_us(10)

# html_index = 
# html_index.to_html('index.html')


# In[65]:

error_html = """
<html>
  <head><title>Something is wrong</title></head>
  <body><h2>Something is terribly wrong with my S3-based website</h2></body>
</html>"""

Html_file= open("error.html","w")
Html_file.write(error_html)
Html_file.close()

index_html = """
<html>
  <head><title>Hello World!</title></head>
  <body><h2>Welcome!</h2></body>
</html>
"""
Html_file= open("index.html","w")
Html_file.write(index_html)
Html_file.close()








