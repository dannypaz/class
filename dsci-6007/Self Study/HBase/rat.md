4) Explain the relationship between HBase and HDFS.  
















HBase runs on top of Hadoop and relies on HDFS for its data storage.


---
Extra Questions
---


*  Given an HBase table name, put the following in order of retrieval to access a cell’s value:
a) Column qualifier b) Rowkey c) Column family d) Timestamp
    + Answer: Column Family -> Rowkey -> Column Qualifier -> Timestamp 
* True or False: Every cell in HBase has its own timestamp.
    + Answer: True.

Consider the following HBase code:
put.add("a".getBytes(), "b".getBytes(), "c".getBytes());

* What does “a” represent? ________________________________ 
    + Answer: Column family
* What does “b” represent? ________________________________ 
    + Answer: Column qualifier
* What does “c” represent? ________________________________ 
    + Answer: Cell value
* The data type of the key passed to a TableMapper is ImmutableBytesWritable. What does this key contain?
    + Answer: The rowkey
* What is the data type of the value passed to a TableMapper?
    + Answer: The value is a Result object, which contains all the data of the row.