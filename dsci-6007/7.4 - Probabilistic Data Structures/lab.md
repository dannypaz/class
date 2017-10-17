HyperLogLog
-----------

As n increases in size, the latency of our computations become increasingly important.  Any inefficiencies in our code will magnify runtime in relation to the size of n.  One way to curb the runtime on a large n is to use a sample of our data.  A preferred, more precise alternative is to use probabilistic data structures.  The goal of the lab is to explore this idea on our twitter data.

As you read in the [Approximate Algorithms in Apache Spark](https://databricks.com/blog/2016/05/19/approximate-algorithms-in-apache-spark-hyperloglog-and-quantiles.html) blog post, HyperLogLog is implemented in Spark as [countApproxDistinct](http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.countApproxDistinct). Apply this to your tweets dataset to get an approximate count of daily active users (DAUs). Compare this to a true count (_i.e._ not using `countApproxDistinct`). What's the time difference? What's the accuracy tradeoff?

Given the size of our data (which should now be a few hundred gigabytes) we should develop this as a `spark-submit` job run using `nohup`.  The job should do the following:

1. Record the **runtime and result** of distinct counts of users using an exact algorithm
2. Record the same using an approximative algorithm
3. Save the results to a text file on the worker node that shows both runtimes, both results, and the relation between the two

Remember to run this on a subset of your data before scaling.  The final calculation could take over an hour depending on the size of your n.  *The deliverables for this lab are your code and the text document that your code creates*.

## Extra Credit

 Play around with the variable `relativeSD` to adjust the relative accuracy of your computation.  Report this in the text file of your results.
