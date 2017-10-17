Cassandra in the Cloud
----

Motivation: You've been processing data stored in S3. This has the advantage of scaling virtually infinitely (compared to your single-node databases we used earlier in this course) but it has the problem that whenever you want to use it, you have to _move data to code_ which is the _opposite_ of what we want to do. For today's lab, we will now start keeping a copy of our data in Cassandra.

1. Follow the instructions at [amazon-cloudformation-dse/README.md](https://github.com/DSPN/amazon-cloudformation-dse/blob/master/README.md).
_N.B._ `deploy.sh` takes about 10 minutes to run and (in my experience) fails about 50% of the time. So I suggest both pairs run the script and which ever one completes first becomes the driver. Once you make sure everything works (and not before!) the other partner may run `delete-stack` on theirs.

2. Create a `KEYSPACE` and a `TABLE` in which to store Twitter hashtags. Note that Cassandra (like Postgres) supports [array](https://www.postgresql.org/docs/current/static/arrays.html) datatypes (though they are called [lists](https://docs.datastax.com/en/cql/3.1/cql/cql_using/use_list_t.html) in CQL). It even supports [sets](https://docs.datastax.com/en/cql/3.1/cql/cql_using/use_set_t.html) which may be particularly useful for your hashtags.

3. Update your API script so that, in addition to streaming tweets into S3, it also inserts hashtags into Cassandra.
    - _N.B._ If we had used Kafka or Kinesis Streams (instead of Kinesis Firehose) we could have simply added a new consumer for this purpose. This would actually be the preferred solution for a number of reasons. (Can you name them?) But since Kinesis Firehose does not allow us to create our own consumer, we must do this. We could also create a new Kinesis Stream (not Firehose) for this purpose, but that is not necessary. You may consider that a possible extra credit assignment.
