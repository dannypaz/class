Streaming Tweets into Mongo
====

Starting with the EC2 instance you launched earlier in this course:

1. [Install MongoDB](https://docs.mongodb.com/master/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition)
			
		sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
				
		echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

		sudo apt-get update

		sudo apt-get install -y mongodb-org
		
2. Start MongoDB  
	If you want to be able to connect to MongoDB remotely (like, from your laptop), you will need to follow these steps:
	1. Edit the inbound rules in your EC2 instance's security group to allow connections on port 27017
	2. Edit `/etc/mongod.conf` to comment out `bindIp: 127.0.0.1` under `# network interfaces` in order to allow `mongod` to accept remote connections
	3. 	Similarly, when you start mongod, include the tag `--bind_ip 0.0.0.0` _i.e._:

			sudo service mongod restart --bind_ip 0.0.0.0

3. Stream tweets from Twitter's public Firehose [sample](https://dev.twitter.com/streaming/reference/get/statuses/sample) API endpoint into Mongo using an infinite loop.   
	Hints: 
		- Use the [TwitterStream](https://github.com/sixohsix/twitter/tree/master#the-twitterstream-class) class in the Python Twitter Tools library
		- It may be tempting to use the `.insert_many` method, but this may run into issues since the TwitterStream iterator is unbounded. May be easier to just `insert_one` at a time. You might try experimenting with [islice](https://docs.python.org/2/library/itertools.html#itertools.islice) but it too can have strange effects.

4. Package this into a script and run it using `nohup` and `&` (as you did with `SimpleHTTPServer` before) and let it run over the weekend, accumulating tweets in your Mongo database.
 
5. Optional: Use the [aggregation](https://docs.mongodb.com/manual/aggregation/) framework to reproduce something like the top trending topics using your sample of Twitter's firehose.
