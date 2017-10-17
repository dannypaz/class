#! usr/bin/env python
import os
import yaml
import psycopg2
#get credentials
credentials = yaml.load(open(os.path.expanduser('~/.ssh/api_credentials.yml')))
# end point for RDS system
database_endpoint = "stream-tweets-db.cbx9xkfcpnfu.us-west-2.rds.amazonaws.com"
db_credentials = credentials['postgresstwitter'].get('db_name')
db_user = credentials['postgresstwitter'].get('user')
db_password=credentials['postgresstwitter'].get('password')
##connect to postgress
conn = psycopg2.connect(dbname=db_credentials,\
user=db_user,\
host=database_endpoint,\
password=db_password)
cur = conn.cursor()
###select statement
cur.execute("""REFRESH MATERIALIZED VIEW normalized_hashtags;""")
conn.close()
cur.close()
