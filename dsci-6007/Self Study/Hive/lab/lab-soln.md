## Question:
What is the value returned for 'hive.execution.engine' and what does it mean?
Is it 'mr' for MapReduce?

## Answer:
For Hortonworks Sandbox it is Tez.


## Question:
You will need the header lines from each of these files in order to
create appropriate schemas for Hive tables.  How do you view the
header lines?  Look at the first few lines of each file and record
the names and likely SQL data types for each column.

## Answer:
```bash
head -n 2 links.csv
head -n 2 movies.csv
head -n 2 ratings.csv
head -n 2 tags.csv
```


## Question:
What command(s) did you use to create the directories and to copy
over the files?

## Answers:
```bash
hadoop fs -mkdir -p /user/root/links
hadoop fs -mkdir -p /user/root/movies
hadoop fs -mkdir -p /user/root/ratings
hadoop fs -mkdir -p /user/root/tags
```

```bash
hadoop fs -put links.csv   /user/root/links/links.csv
hadoop fs -put movies.csv  /user/root/movies/movies.csv
hadoop fs -put ratings.csv /user/root/ratings/ratings.csv
hadoop fs -put tags.csv    /user/root/tags/tags.csv
```


## Question:
What Hive SQL statement will create an external table for the data in
the 'links.csv' file and also ingest it into the table?

## Answer:
```sql
-- Drop table if it exists.
DROP TABLE IF EXISTS links;

-- Create table.
CREATE EXTERNAL TABLE links
  (movieId INT,
  imdbId STRING,
  tmdbId STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/links'
TBLPROPERTIES("skip.header.line.count"="1");
```

The statements are similar for the other tables.

```sql
-- Drop table if it exists.
DROP TABLE IF EXISTS movies;

-- Create table.
CREATE EXTERNAL TABLE movies
  (movieId INT,
  title STRING,
  genres STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/movies'
TBLPROPERTIES("skip.header.line.count"="1");

-- Drop table if it exists.
DROP TABLE IF EXISTS ratings;

-- Create table.
CREATE EXTERNAL TABLE ratings
  (userId INT,
  movieId INT,
  rating FLOAT,
  time STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/ratings'
TBLPROPERTIES("skip.header.line.count"="1");

-- Drop table if it exists.
DROP TABLE IF EXISTS tags;

-- Create table.
CREATE EXTERNAL TABLE tags
  (userId INT,
  movieId INT,
  tag STRING,
  time STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/tags'
TBLPROPERTIES("skip.header.line.count"="1");
```

### Notes

We had to rename `timestamp` to `time` because `timestamp` is a
reserved word in HiveQL.


## Question:
What Hive SQL statement can be used to examine the schema in the table?

## Answer:
```sql
DESCRIBE links;
```


## Question:
What Hive SQL statement can be used to list the first 5 entries in the
table?

## Answer:
```sql
SELECT * FROM links LIMIT 5;
```


## Question:
What Hive queries would perform the following actions?
    Count the number of movies in the `movies` table.
    Count the number of distinct tags grouped by tags.

## Answer:

- Count the number of movies in the `movies` table.

```sql
SELECT COUNT(title) FROM movies;
```

- Count the number of distinct tags grouped by tags.

```
SELECT tag,COUNT(*) FROM tags GROUP BY tag;
```


## Question:
What Hive queries would be needed to answer these questions?
    How many ratings does each movie have?
    What is the average rating for each movie?

## Answer:

- For each movie find how many ratings it has.

```sql
SELECT movies.title, COUNT(ratings.rating)
FROM movies
LEFT JOIN ratings
ON (movies.movieId = ratings.movieId)
GROUP BY movies.movieId, movies.title;
```

- For each movie find out the average rating.

```sql
SELECT movies.title, AVG(ratings.rating)
FROM movies
LEFT JOIN ratings
ON (movies.movieId = ratings.movieId)
GROUP BY movies.movieId, movies.title;
```


## Question:
How would you find the top 10 movies with the highest average ratings that have at
least 5 ratings?

## Answer:

- Find top 10 movies with the highest average ratings that have at least 5 ratings.

```sql
-- Create table.
DROP TABLE IF EXISTS movie_ratings;
CREATE TABLE movie_ratings (
  movieId INT,
  title STRING,
  rating_count INT,
  rating_avg DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Save intermediate data in it.
INSERT INTO movie_ratings
SELECT movies.movieId, movies.title,
  COUNT(ratings.rating) AS rating_count,
  AVG(ratings.rating)   AS rating_avg
FROM movies
LEFT JOIN ratings
ON (movies.movieId = ratings.movieId)
GROUP BY movies.movieId, movies.title;

-- Now calculate the result.
SELECT *
FROM movie_ratings
WHERE rating_count > 5
DISTRIBUTE BY rating_avg
SORT BY rating_avg DESC
LIMIT 10;
```


## Question:
Creating external tables to .csv files is useful, but it would be even better
if the files were in a format such as AVRO which supported an evolving schema,
data compression, etc.  You don't need to write out the exact SQL here, but
generally, if you wanted to use Hive to convert the links.csv data to an AVRO
file what steps would be required?

## Answer:
Hive has good support for AVRO files and schemas.

First load the links .CSV data into a 'textfile' table as you have already done
in this lab.  Then create a new table to hold data in AVRO format (i.e. instead
of 'STORED AS TEXTFILE' substitute 'STORED AS AVRO') and specifying the AVRO
schema in TBLPROPERTIES.  Then copy the data from the first - textfile - table
into the second - AVRO - table.


## Question:
What Hive commands will delete the tables you created for this lab?
What other commands do you need in order to remove the associated
data in HDFS?

```sql
DROP TABLE links;
DROP TABLE movies;
DROP TABLE ratings;
DROP TABLE tags;
```

We have to delete the data in HDFS since we used external tables.

```bash
hadoop fs -rm -r /user/root/links
hadoop fs -rm -r /user/root/movies
hadoop fs -rm -r /user/root/ratings
hadoop fs -rm -r /user/root/tags
```
