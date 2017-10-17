Hive 2: Quiz
============

Q1: Suppose you have the following table definition:  

```sql
CREATE TABLE movies (
  title STRING, 
  rating STRING, 
  length DOUBLE)  
PARTITIONED BY (genre STRING);
```

What will the folder structure in HDFS look like for the movies table?  

- Within `/apps/hive/warehouse/movies` will be subfolders named
  `/genre=value`. For example, `/genre=scifi`, `/genre=comedy`,
  `/genre=drama`, etc.

Q2: What is a *SerDe*?

- SerDe is a short name for Serializer and deserializer.

Q3: Where should you place the largest table in a `JOIN`?

- At the end.

Q4: You provide a Hive-based storage for your client's sales
transactions. Your clients run queries on their own data. 

Between *partitioning* and *bucketing* which is optimal for strong
this data?

- You should use partitioning.

- Each client will get their own partition and will query within it.
