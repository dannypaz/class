A Quick Example
---------------

Work through [A Quick Example](http://spark.apache.org/docs/latest/streaming-programming-guide.html#a-quick-example) on your Spark cluster. This example assumes that you have downloaded Spark to a local directory and that you are in that directory, hence the relative paths `./bin/spark-submit` and `examples/src/main/python/streaming/network_wordcount.py`. Since you will be using en EMR cluster, you should not use the relative path `./bin/spark-submit` but rather call `spark-submit` as normal just as you did in the [`spark-submit` lab](../5.4 - Spark Submit/lab.md). Also, do not use `examples/src/main/python/streaming/network_wordcount.py` but make your own according to the code given.

Notice that unlike most of our Spark labs so far, this one _cannot_ be done interactively. It can only be completed using `spark-submit`.

Time permitting (in other words, the following is optional) work through the rest of the examples in the [Spark Streaming Programming Guide](http://spark.apache.org/docs/latest/streaming-programming-guide.html). As an advanced exercise, try to use Spark Streaming to count the distinct users in your Twitter stream. (You may need to set up a separate [Kinesis stream](http://spark.apache.org/docs/latest/streaming-kinesis-integration.html) for this.)

If you complete only the [Spark Streaming Programming Guide](http://spark.apache.org/docs/latest/streaming-programming-guide.html), you must submit proof of completion in the form of screen captures of both the output (the Spark Streaming output) and the input (what you enter into Netcat). (_N.B._ by "screen capture" I just mean saving the text that's in your terminal to a file. I **don't** mean a "screen shot" much less anything more elaborate like a video capture.)

If you complete the advanced exercise of developing a Spark Streaming app to consume Twitter data, you must submit code for both your producer and your consumer as well as a screen capture of what the consumer outputs. (No need to capture input as that is covered by your producer script.)
