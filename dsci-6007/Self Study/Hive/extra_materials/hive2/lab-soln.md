##Individual Assignment (Solutions)  

- Step1: Download 100m movies data from `<Galvanize link>`

- Step2: Load data into hdfs
- Create `<tablename>_txt` to load data as text file.

```
CREATE TABLE movies_txt
  (movieID INT, 
  title STRING, 
  genres STRING) 
row format delimited 
fields terminated by ',' 
stored as textfile 
tblproperties("skip.header.line.count"="1");

load data local inpath 'movies.csv' into table movies_txt;
```

- Create `<tablename>_rc` to load data in rc format.

```
CREATE TABLE movies_rc
  (movieID INT, 
  title STRING, 
  genres STRING) 
row format delimited 
fields terminated by ',' 
stored as rcfile 
tblproperties("skip.header.line.count"="1");

load data local inpath 'movies.csv' into table movies_rc;
```


- Create `<tablename>_orc` to load data in orc format.

```
CREATE TABLE movies_orc
  (movieID INT, 
  title STRING, 
  genres STRING) 
row format delimited 
fields terminated by ',' 
stored as orc 
tblproperties("skip.header.line.count"="1");

load data local inpath 'movies.csv' into table movies_orc;
```

- Step3: Load the data into above tables from hdfs and note the timings. Which table took more time to load?

- Step4: How many movies with the tag `Action` are present in the list? Save a list of the titles and IDs of such movie to the HDFS. Contrast the timings. *Hint : Case sensitive?*

```
select count(*) from movies where genres like '%Action%';
```


####Partitioning
- Step1: Review the data in `hive2_<<country>>.txt`  
- Step2: Load the files to hdfs.  
- Step3: Create table `states` in hive with partition as `country`.  

```
CREATE TABLE states
  (state STRING, 
  population STRING)
partitioned by (country STRING)
row format delimited 
fields terminated by ',' 
stored as textfile; 
```
- Step4: Query about the description of the table. 

```
hive> desc states;         
OK
state               	string              	                    
population          	string              	                    
country             	string              	                    
	 	 
# Partition Information	 	 
# col_name            	data_type           	comment             
	 	 
country             	string              	                    
Time taken: 0.531 seconds, Fetched: 8 row(s)
``` 

- Step5: Load states with data from different files in hdfs.  

```
load data local inpath 'hive2_india.csv' into table states partition (country = 'india');

load data local inpath 'hive2_usa.csv' into table states partition (country = 'usa');
```

- Step6: Check the directory structure in HDFS. Which folder(s) should we be looking at?

####Bucketing
- Step1: Review data in movies.csv  
- Step2: Create table `movies1` **without** bucketing.    

```
CREATE TABLE movies1
  (movieID INT, 
  title STRING, 
  genres STRING) 
row format delimited 
fields terminated by ',' 
stored as textfile 
tblproperties("skip.header.line.count"="1");
```

- Step3: Create table `movies2` **with bucketing over movieID (4 buckets)**.  

```
CREATE TABLE movies2
  (movieID INT, 
  title STRING, 
  genres STRING)
clustered by (movieID) INTO 4 buckets
row format delimited 
fields terminated by ','
stored as textfile 
tblproperties("skip.header.line.count"="1");
```
- Step4: Load same data to both tables and notice difference in time.   
- Step5: Run count(*) command on both tables and notice difference in time.  

```
select count(*) from movies1;
select count(*) from movies2;
``` 

- Step6: Perform sampling on movies2

```
select title from movies2 tablesample(bucket 2 out of 4 on movieID);
```
