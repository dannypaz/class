RAT - HDFS
--------

1) Hadoop Distributed File System

2) Rewrite the entire file and replace the old file.
https://www.quora.com/Is-HDFS-an-append-only-file-system-Then-how-do-people-modify-the-files-stored-on-HDFS

3) 3

- The first replica will be on the DataNode.
- The second replica will be on a machine in a different rack.
- The third replica will be on another machine in the same rack as the
  second replica.

4) If I run the command `hadoop fs -ls` what directory will this list?

- The home directory of the current user.

- If the current user is `eliose` it will list `/eliose/jim`.

5) The main goal of HDFS High availability is
A - Faster creation of the replicas of primary namenode.

__B - To reduce the cycle time required to bring back a new primary namenode after existing primary fails.__

C - Prevent data loss due to failure of primary namenode.

D - Prevent the primary namenode form becoming single point of failure.






---
Extra questions
----

What are the names of the following daemons?

Q: HDFS master daemon that manages the metadata?

- NameNode

Q: HDFS master daemon that compacts the metadata? 

- Secondary NameNode

Q: HDFS master daemon that is a backup for the main master daemon?

- Standby NameNode

Q: HDFS worker daemon?

- DataNode


I want to change the replication of a file using `setrep`. 

Q: What is the difference between `setrep 10 file1` and `setrep -w 10 file1` with the added `-w`?

- The version with `-w` will block until `file1` is replicated 10 times.

Q: Which one is faster?

- The version with `-w` will be slower because it blocks.
