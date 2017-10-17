Spark

- https://academy.datastax.com/resources/getting-started-apache-spark?unit=introduction-spark-architecture


Spark & Cassandra:

Cassandra on EC2
change `rpc_address` to the private IP


https://www.youtube.com/watch?v=ikCzILOpYvA

advanced (scala) - https://www.youtube.com/watch?v=g4RmAS9pZ2Q


Lab
---

1. Start Cluster:

		git clone https://github.com/DSPN/amazon-cloudformation-dse.git
		cd amazon-cloudformation-dse/singledc
		./deploy.sh -i t2.medium

2. [Lab 1 - Accessing the Cluster](https://github.com/DSPN/DataStaxDay/blob/master/labs/Lab%201%20-%20Accessing%20the%20Cluster.md) - Start Spark on each node in the cluster:

		sudo su
		apt-get update
		apt-get upgrade -y
		vi /etc/default/dse

	Set:

	- GRAPH_ENABLED=1
	- SOLR_ENABLED=1
	- SPARK_ENABLED=1

	Finally:

		service dse restart

3. Log into node and install and start Zeppelin:

	1. Get `zeppelin-0.6.1-dse-5.0.2-5.0.3.tar.gz` from the shared
[Google drive folder](https://drive.google.com/folderview?id=0B6wR2aj4Cb6wQ01aR3ItR0xUNms).
	2. Following [Starting Apache Zeppelin with Command Line](https://zeppelin.apache.org/docs/0.6.1/install/install.html#starting-apache-zeppelin-with-command-line):

			tar -xzf zeppelin-0.6.1-dse-5.0.2-5.0.3.tar.gz
			cd zeppelin-0.6.1/
			bin/zeppelin-daemon.sh start
