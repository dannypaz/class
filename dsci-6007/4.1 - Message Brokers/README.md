I ♥ Logs
----

#### By the end of this article you should have:

- Watched:
    - I ♥ Logs: Apache Kafka and Real-Time Data Integration
    - Introducing Amazon Kinesis Firehose

----

This week, we have started to consider what a multi-server architecture might look like. One of the things you've seen is that a single EC2 instance to handle all of your system's needs is not very sustainable.

We will also discover that storing all of your data on a single machine is also not sustainable when dealing with so-called "big data". For that, we will want to store our data on something like a distributed file system (DFS). For the time being, we will use S3 (which is "something like a distributed file system").

In order to solve these problems (multiple dedicated machines and streaming data into a DFS or S3) we will need something called a message broker to move the data around. For the purposes of this course, we will be focussing on two such systems: Apache Kafka and Amazon Kinesis. Beginning with Apache Kafka, watch this video by Jay Kreps, the author of Apache Kafka, called [I ♥ Logs: Apache Kafka and Real-Time Data Integration](https://www.youtube.com/watch?v=aJuo_bLSW6s). By the end of this video, you should understand essentially what [Kafka](https://kafka.apache.org/) is and what makes it valuable.

Now that you know what a message broker is, watch [Introducing Amazon Kinesis Firehose](https://www.youtube.com/watch?v=YQR_5W4XC94). [Kinesis Firehose](console.aws.amazon.com/firehose) is Amazon's version of Apache Kafka (sort of). With Kafka we would need to program both a producer and a consumer, but with Kinesis Firehose, the consumer is already defined and you just need to pick a destination (S3 or Redshift). Amazon Kinesis has other offerings as well if you want to develop more advanced consumers, but for our purposes, the Firehose will suffice. (Later, when we get to analyzing streaming data, the other offerings may become useful.)

For a primer on Kinesis, you may wish to complete Qwiklab's [Introduction to Amazon Kinesis Firehose](https://run.qwiklab.com/focuses/2988). It's optional but may be helpful, particularly if you get stuck during the lab. One difference worth noting, however, is that Qwiklab's lab uses the [Kinesis Agent](http://docs.aws.amazon.com/firehose/latest/dev/writing-with-agents.html) while I recommend you use [boto3](http://boto3.readthedocs.io/en/latest/reference/services/firehose.html) for the class lab.

#### On completing this article, you should:

- Have watched two videos.
- Be able to identify the relationship between Kafka and Kinesis and explain what they are and why they exist.
