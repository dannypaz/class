Hive 1: Quiz
============

1) __False__SQL-like queries (HiveQL), which are implicitly converted into MapReduce or Tez, or Spark jobs.

2 Can Hive be used to process image or video data?  

    - Hive is designed to work for structured and semi-structured data.

    - It does not have built-in SerDes for processing image or video data.

3. Where does Hive store table metadata and where does it store table
    data?

    - Hives stores table metadata in the MetaStore.

    - Hive stores table data in HDFS.



6. List three different ways data can be loaded into a Hive table.

    - Manually copying files into the table’s folder in HDFS

    - Using the LOAD DATA command

    - Inserting data as the result of a query

7. What will this query do? 

    `SELECT * FROM movies ORDER BY title;`

    - The `ORDER BY` clause causes the output to be totally ordered by
      `title` across all output files.

    - However, it only uses 1 reducer. 

    - To make this more scalable consider using `CLUSTER BY` instead.
  
  ----
  extra
  ---
  1. How are number of mappers decided in Hive? Is there any default or
    minimum number for Hive queries?  

    - Same way as they are decided in MapReduce programs, i.e. by the
      input splits. 

    - The number of mappers depends on the number of blocks in the
      directory for the table we are running the query on.

    - There is no default or minimum requirement.



4. True or False: The Hive MetaStore requires an underlying SQL
    database.

    - True. 

    - Hive uses an in-memory database called Derby by default, but you can configure Hive to use any SQL database, such as MySQL.

5. What happens to the underlying data of a Hive-managed table when
    the table is dropped? 

    - The data and folders are deleted from HDFS.
