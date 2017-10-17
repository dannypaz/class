import os
import ssl
import pandas as pd
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto
__author__ = "Jonathan Hilgart"
# This allows us to use buckets with dots in them
if hasattr(ssl, '_create_unverified_context'):
   ssl._create_default_https_context = ssl._create_unverified_context
s3_connection = boto.connect_s3(host='s3.amazonaws.com')
website_bucket = s3_connection.get_bucket('bart-capacity-predictions.com')
predicted_capacity = ''
with open(os.path.expanduser("~/predicted_capacity")) as fp:
    predicted_capacity = fp.read()
html = '<!DOCTYPE html><HTML><BODY>{}</BODY></HTML>'.format(
    predicted_capacity)
output_file = website_bucket.new_key('index.html')
output_file.content_type = 'text/html'
output_file.set_contents_from_string(html, policy='public-read')
