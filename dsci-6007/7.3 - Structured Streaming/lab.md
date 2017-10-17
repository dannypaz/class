# A Live View into our Firehose

In the last lab, we looked at Spark Streaming using a simple tutorial that allowed us to count words entered into Netcat, a utility that writes data across network connections.  Netcat simulated streaming data from an API.  In the wild, we would want to point Kinesis, Kafka, Twitter, or other data sources to a Spark **receiver** that takes data and turns it into a **DStream** or Discretized Stream.

Today, we will be expanding upon this lab in a still somewhat contrived way.  Instead of using Netcat, we'll be running a script that will handle our connection and write tweets to our socket.  This is more similar to what we'll see in the wild.  Like yesterday, run this in a different window from your `spark-submit` script.  Today, instead of a simple word count, we'll be counting our hashtags in real time.

The script to simulate a data stream is available in `twitter_stream.py`.  Read through it and modify it to use your twitter credentials.  There have been some challenges running `pip` with `sudo` so when installing dependencies you might consider running:

        sudo `which pip` install <package>

Change your word count script to return hashtag counts and to run your job every 10 seconds.  Note that actions like `top` might not work on transformed DStreams.

Your deliverables for this lab are the code you used to run your `spark-submit` job as well as screen captures of both EMR terminal windows.

## Extra Credit

Use either stateful or window transformations to deliver a running total of hashtags.
