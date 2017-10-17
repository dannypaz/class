Drinking from the Firehose
----

As your data grow, it will become more difficult to scale on a single instance database. We could [shard](https://docs.mongodb.com/manual/sharding/). Or we could move to [Amazon Redshift](aws.amazon.com/redshift) (a massive parallel processing (MPP) RDBMS that is built off of PostgreSQL 8). But perhaps we don't need ***all*** of our data in a managed system. Perhaps we can save some money by keeping our raw data in S3 and only storing what we need in our database.

This is easy to do with [Kinesis Firehose](https://aws.amazon.com/kinesis/firehose/). To begin with, [create a Firehose Delivery Stream to Amazon S3](http://docs.aws.amazon.com/firehose/latest/dev/basic-create.html#console-to-s3). You can then use [boto3](https://boto3.readthedocs.io/en/latest/reference/services/firehose.html) to stream your data into S3. In much the same way that you inserted documents into MongoDB, you will instead be putting records into the Firehose. 

Hint: Unlike PyMongo, boto3 is not smart enough to convert a Python dict into the appropriate format. You may have use `json.dumps` to convert the tweet back into a string for the Firehose. Also, you will want to insert a **delimiter** (such as a new line character: `\n`) after each datum to make it easier to split when reading it back out.
