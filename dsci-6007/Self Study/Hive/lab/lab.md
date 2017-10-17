## Step 1: Start VM and establish connections

Ensure that your Hortonworks Sandbox VM is started.

Sometimes it is useful to simultaneously work with multiple running
programs on a remote machine.  For this lab you may want to be
running the Hive shell while you are also using Bash commands.
If so, then either make two SSH connections to the Sandbox or use a
tool like 'tmux' as described in a previous lab.

## Step 2: Hive shell

The Hive shell is started by the command 'hive'.  If you prefer to
place SQL statements in a separate text file and run them in batch mode
you may do so using 'hive -f mycmds.sql'.

In addition, a single statement may be executed using the '-e'
command-line parameter.  In the lecture we learned that Hive translates
SQL into MapReduce jobs.  Let's verify that by running the following
from a Bash shell:

    hive -e 'set -v' | grep hive.execution.engine

## Question:
What is the value returned for 'hive.execution.engine' and what does it mean?
Is it 'mr' for MapReduce?

Note that, once Hive on Spark support is finalized, you will be able
to improve Hive SQL performance by switching to the Spark engine instead.

## Step 3: Retrieve Movielens Data

Download the MovieLens data fileset from
<http://files.grouplens.org/datasets/movielens/ml-latest-small.zip>

Unzip it and look at the list of files.  You should see at least the
following files.

- `links.csv`
- `movies.csv`
- `ratings.csv`
- `tags.csv`

## Question:
You will need the header lines from each of these files in order to
create appropriate schemas for Hive tables.  How do you view the
header lines?  Look at the first few lines of each file and record
the names and likely SQL data types for each column.


## Step 4: Upload Movielens Data to HDFS

Create the following dirs in HDFS:

- `/user/root/links` 
- `/user/root/movies` 
- `/user/root/ratings` 
- `/user/root/tags`

Upload each of the CSV files into its directory in HDFS.

## Question:
What command(s) did you use to create the directories and to copy
over the files?


## Step 3: Create Tables and Ingest the Data

Go ahead and start the Hive shell now.

## Question:
What Hive SQL statement will create an external table for the data in
the 'links.csv' file and also ingest it into the table?

## Question:
What Hive SQL statement can be used to examine the schema in the table?

If you forget what HDFS directory into which you loaded data for an
external table, Hive provides the following additional parameter to
the 'DESCRIBE' statement:

    'DESCRIBE FORMATTED table_name'

Try that with the 'links' table to examine the location of the links
data in HDFS.

## Question:
What Hive SQL statement can be used to list the first 5 entries in the
table?

Repeat the previous steps to ingest the 'movies', 'ratings', and 'tags' data
into their own tables.


## Step 4: Hive Queries

Queries may return many rows.  If you want to store the results to HDFS then
precede your queries with 'INSERT OVERWRITE DIRECTORY' as in this example:

    INSERT OVERWRITE DIRECTORY '<HDFS output path>' SELECT * FROM table WHERE id > 100;

## Question:
What Hive queries would perform the following actions?
    Count the number of movies in the `movies` table.
    Count the number of distinct tags grouped by tags.

Optional: If you are curious as to how Hive maps SQL to map and reduce
operations then precede your queries with 'EXPLAIN EXTENDED'.
For example:

    EXPLAIN EXTENDED SELECT columnA, COUNT(columnA) FROM sometable GROUP BY columnA;

This won't execute the SELECT but it will show you an abstract syntax tree
as well as the map and reduce steps which would be run.

## Question:
What Hive queries would be needed to answer these questions?
    How many ratings does each movie have?
    What is the average rating for each movie?


## Step 5: Extra Credit

## Question:
How would you find the top 10 movies with the highest average ratings that have at
least 5 ratings?

## Question:
Creating external tables to .csv files is useful, but it would be even better
if the files were in a format such as AVRO which supported an evolving schema,
data compression, etc.  You don't need to write out the exact SQL here, but
generally, if you wanted to use Hive to convert the links.csv data to an AVRO
file what steps would be required?

## Step 6: Cleanup

## Question:
What Hive commands will delete the tables you created for this lab?
What other commands do you need in order to remove the associated
data in HDFS?
