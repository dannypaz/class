import socket
import sys
from thread import *
import requests
import requests_oauthlib
import json
import oauth2 as oauth
from datetime import datetime
import time
import yaml

#Variables that contains the user credentials to access Twitter API
credentials = yaml.load(open('twitter_api_cred.yml'))['twitter']
auth = requests_oauthlib.OAuth1(credentials['consumer_key'], credentials['consumer_secret'], credentials['token'], credentials['token_secret'])


#Function for handling connections. This will be used to read data from tweeter and write to socket
def clientthread(conn):
    url='https://stream.twitter.com/1.1/statuses/filter.json'
    #
    data = [('language', 'en'), ('locations', '-130,-20,100,50')]
    #,('track','ibm,google,microsoft')
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in data])
    response  = requests.get(query_url, auth=auth, stream=True)
    print(query_url, response) # 200 <OK>
    count = 0
    for line in response.iter_lines():  # Iterate over streaming tweets
        try:
            if count > 10000000:
                break
            post= json.loads(line.decode('utf-8'))
            #contents = [post['text'], post['coordinates'], post['place']]
            count+= 1
            conn.send(line+'\n')
            #time.sleep(1)

            print (str(datetime.now())+' '+'count:'+str(count))
        except:
            e = sys.exc_info()[0]
            print( "Error: %s" % e )
    conn.close()


HOST = ''
PORT = 9995 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'

#now keep talking with the client
while True:
    #wait to accept a connection - blocking call
    print('inside while')
    print(s.accept())
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
print('outside while')
s.close()
