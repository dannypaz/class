RAT solution
----

1. 
C Consistency Every EC2 server has the same data all the time.
A Availability. I'm SRE for Google and people can make queries
P Partition Tolerance My datacenter has self-healing tologogy

2. RMDS  = CA
Cassandra = AP
Zookeeper = AP

3) 

1) Hard to test
2) Hard to hire

1) What is Cassandra's core abstraction that enables linear scaling?

&nbsp;&nbsp; A. Short term leases (<5ms)  
&nbsp;&nbsp; B. Consistent hashing  
&nbsp;&nbsp; C. Messaging  
&nbsp;&nbsp; D. Open source  
&nbsp;&nbsp; E. Hiring people from Standford
&nbsp;&nbsp; F. Spending billions of dollars 

__consistent hashing__
Allows distributing data across a cluster which minimizes reorganization when nodes are added or removed

5) What is the relationship between SQL and CQL?

CQL is selected dialect of SQL for querying Cassandra.

Optional:
_2_
Start at 0: 
steps: 1, 2, 3, 4, 5, 6, 7
ending location: 2, 1, 0, 2, 1, 0, 2

----
extra questions
-----

2) What distrubted system property does Cassandra give up to achieve that scaling? Explain your logic.

strong consistency
gossip protocal

6) What is important about the predicate in CQL queries that help with agregrative queries?

It is should be a parition key then allowing for predicate pushdown. the query execution engine only has to reterve the needed data from disk via the hash function


4) What is the most important property of CQL predicates that facilitates aggregation queries (e.g.,  AVERAGE, COUNT, MAX, MIN, and SUM)?

<br>
<br>
