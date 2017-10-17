__author__ = 'Jonathan Hilgart'

import boto
from boto.s3.key import Key
import pandas as pd
from collections import Counter
from textblob import TextBlob
import csv

#https://dzone.com/articles/file-handling-in-amazon-s3-with-python-boto-librar



srcFileName="shakespeare-sonnets.txt"
destFileName="shakespeare.txt"
bucketName="1776jhbucket"

conn = boto.connect_s3()
bucket = conn.get_bucket(bucketName)
#Get the Key object of the given key, in the bucket
k = Key(bucket,srcFileName)
#Get the contents of the key into a file 
k.get_contents_to_filename(destFileName)

## open the file

file=open("shakespeare.txt");
shakes=file.read();

## convert to textblob class and find the frequency of each word in the sonnet

blob= TextBlob(shakes)
shakes_count = Counter(blob.words)
twenty_most_common_words = shakes_count.most_common(20)
print(shakes_count.most_common(20))

## upload to s3

#http://stackoverflow.com/questions/15578331/save-list-of-ordered-tuples-as-csv
#save as a filr first
with open('sorted_top_20.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerow(['word','frequency'])
    for row in twenty_most_common_words:
    	w.writerow(row)

## new conenction instance
key = Key(bucket,name='sorted_20_words.txt')
try:
	key.set_contents_from_filename('sorted_top_20.csv')
except:
	'Could not upload file'






