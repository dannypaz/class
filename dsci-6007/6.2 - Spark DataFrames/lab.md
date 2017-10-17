DataFrames
----------

So far, we've introduced the concept of distributed systems using parallel processing on a single machine with `ipyparallel` and its `scatter`/`gather` functions.  We then expanded on this idea by using different nodes (instead of different processors) to distribute our workload with the map/reduce paradigm.  In the last lab, we explored how Spark can also handle map/reduce jobs.

In this lab, we will repeat what we've been doing, but this time leverage Spark's [DataFrame](http://spark.apache.org/docs/latest/sql-programming-guide.html) API. This is similar in many ways to Pandas' [DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) only it uses camelCase because it's Spark (so `groupBy` instead of `groupby` for example). The way it uses `select` also takes a little getting used to but will make more sense when we see it in terms of Spark SQL.

Are you tired of Zeppelin yet? That's good because we are going to go back to using Jupyter now to make sure our DataFrames work. (When testing this lab earlier this month, we found that Zeppelin did not interface with Spark 2.1 correctly when trying to create a DataFrame out of JSON. We're not huge fans of Zeppelin anyway, so rather than fix it, we decided to use Jupyter instead.)

Getting pyspark to work with Jupyter is easier than you might think. You already know how to install Jupyter on EC2 from the [Distributed Systems lab](4.2 - Distributed Systems/lab.md) (we won't need `ipyparallel` this time because we'll be using Spark instead, but you may want to install `pandas`). Next you will need to do two things: set `PYSPARK_DRIVER_PYTHON` to the location of `jupyter` and set `PYSPARK_DRIVER_PYTHON_OPTS` so that it tells the notebook to accept connections from all IP addresses and without opening a brower. To find out where `jupyter` is installed, you can use the `which` command (as in `which jupyter`). Your `PYSPARK_DRIVER_PYTHON_OPTS` will look familiar is they are the same options you used in the Distributed Systems lab, namely `notebook --NotebookApp.open_browser=False --NotebookApp.ip='*' --NotebookApp.port=8888`. In the end, you will want to append the following two lines to your `.bashrc` file:

	export PYSPARK_DRIVER_PYTHON=`which jupyter`
	export PYSPARK_DRIVER_PYTHON_OPTS="notebook --NotebookApp.open_browser=False --NotebookApp.ip='*' --NotebookApp.port=8888"

Then run `source ~/.bashrc` followed by `pyspark` (_not_ `jupyter notebook`). You should see the familiar standard output telling you that Jupyter Notebook is starting.

Make sure you are allowing connections on port 8888 (in [Security Groups](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:search=ElasticMapReduce-master)) and point your browser to the master node:8888 and don't forget the token. (_i.e._ your URL should look something like `http://ec2-XXX-XXX-XXX-XXX.compute-1.amazonaws.com:8888/tree?token=000111222333444555666777888999aaabbbcccdddeeefff#`)

From there you should see the familiar Jupyter console. As in yesterday's lab, the Spark context (`sc`) and session (`spark`) are already given so you can get started right away. Other classes and functions, like Spark SQL's [`explode`](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.functions.explode) function, will need to be imported in the usual way.

For this lab you must create at least four (4) DataFrames. The first two will be saved as Parquet files to be used later. The third is an aggregation on the second. All three should be normalized.

The first DataFrame should include atomic data about the tweets. The tweet `id` will be the key. It must include `timestamp_ms` and `user.id`. Notice that there is a bit of a problem here if you use `select('id', 'timestamp_ms', 'user.id', 'text')` because `id` is ambiguous. Spark will let you do this but it will cause problems later. Instead try `selectExpr('id', 'timestamp_ms', 'user.id AS user_id', 'text')`. You may include other data (like `text`) if you wish. (Note that data like `favorited_count` will always be zero because you are receiving the tweet before anyone has had a chance to favor it.)

The second DataFrame should consist of your user data. You may just use `user.*` for this. But be sure to store only `distinct` users.

The third DataFrame should have as a composite key the `id` and `entities.hashtags.text`. You will want to `explode` this latter column in order to get it into 1NF. You may include other data relevant to hashtags, but remember 2NF.

[Write](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameWriter.parquet) these three to S3 in [Parquet](https://parquet.apache.org/) format for use tomorrow.

Finally, using the hashtags DataFrame, compute an aggrate to show the top 20 hashtags as before. When you `.show()` it, the result should look something like:

	+--------------------+-----+
	|                 col|count|
	+--------------------+-----+
	|        iHeartAwards|27299|
	|         BestFanArmy|19892|
	|        BestFans2017|12534|
	|        OneDBestFans|10829|
	|        GagaBestFans| 9164|
	|YOU_NEVER_WALK_ALONE| 8229|
	|                 BTS| 7566|
	|      CamilaBestFans| 7224|
	|            Lovatics| 6491|
	|  HappyBirthdayHarry| 5391|
	|             NOW2016| 5345|
	|   BlackHistoryMonth| 5042|
	|       RTした人全員フォローする| 4855|
	|   ALDUB81stWeeksary| 4567|
	|      ALDUBLoveMonth| 4513|
	|      BestMusicVideo| 4435|
	|   PBBPADALUCKMAYMAY| 4060|
	|            ツインテールの日| 4029|
	|           사설토토사이트추천| 3933|
	|         gameinsight| 3796|
	+--------------------+-----+

(Of course, your results will look different from mine.)

---

Once you have completed this lab with your partner, see if you can do something similar with your own data.
