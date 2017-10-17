## ssh using two separate terminals into your EMR cluster
## run nc -lk 9999 in one terminals
## in the other terminal, you may need to run unset PYSPARK_DRIVER_PYTHON
## then, run spark-submit this file
## finally, enter text into the terminal running nc and watch
## spark streaming pick it up in real time!


from pyspark import SparkContext
from pyspark.streaming import StreamingContext

#define the spark context
sc = SparkContext("local[2]") # define for the master node
sc.setLogLevel('ERROR') #only log errors

# Create the streaming context from the SparkContext object
ssc = StreamingContext(sc,5)

## determine where your stream is coming from
lines = ssc.socketTextStream("localhost", 9999)
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()

# start streaming
ssc.start()
ssc.awaitTermination()
