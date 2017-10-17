<a name="Application"></a>

## Running Applications using Hortonworks Sandbox

- Downloading and Installing Hortonworks Sandbox
- Use hadoop examples jar's grep, word-count, and wordmean
- Use use these to split movie reviews into positive and negative
- Run word count on the two sets of files
- See what words are most common in each set

### Downloading and Installing Hortonworks Sandbox

The remainder of this lab will use a local copy of the Hortonworks Sandbox.
Please ensure you have **terminated** the EMR Cluster in Amazon AWS prior to
continuing this lab.

Go to the Hortonworks Sandbox download page - [http://hortonworks.com/products
/hortonworks-sandbox/#install](http://hortonworks.com/products/hortonworks-
sandbox/#install)

Download the latest version. This assumes that you have a local environment for
VirtualBox (free download from
[https://www.virtualbox.org/](https://www.virtualbox.org/)), VMware (Workstation
or Fusion), or Hyper-V to run the Virtual Machine. Download the appropriate VM
for your local environment (which is about 7GB). Instructions for importing the
Virtual Appliance are available on the Hortonworks Sandbox page. Once the
Sandbox has started, the screen should look like the following.

<img src="images/Sandbox.png">

Login to the Sandbox using the instructions for ssh on the screen.

### Use hadoop examples jar's grep,  word-count, and wordmean

Download the dataset 'Complete Works of William Shakespeare' from
<http://www.it.usyd.edu.au/~matty/Shakespeare/shakespeare.tar.gz>

    [root@sandbox ~]# wget http://www.it.usyd.edu.au/~matty/Shakespeare/shakespeare.tar.gz
    --2015-08-25 21:17:10--
    http://www.it.usyd.edu.au/~matty/Shakespeare/shakespeare.tar.gz
    Resolving www.it.usyd.edu.au... 129.78.10.237
    Connecting to www.it.usyd.edu.au|129.78.10.237|:80... connected.
    HTTP request sent, awaiting response... 302 Found
    Location:
    http://sydney.edu.au/engineering/it/~matty/Shakespeare/shakespeare.tar.gz
    [following]
    --2015-08-25 21:17:11--
    http://sydney.edu.au/engineering/it/~matty/Shakespeare/shakespeare.tar.gz
    Resolving sydney.edu.au... 129.78.5.8, 129.78.5.8
    Connecting to sydney.edu.au|129.78.5.8|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 2087964 (2.0M) [application/x-tar]
    Saving to: “shakespeare.tar.gz”

    100%[======================================>] 2,087,964    272K/s   in 9.0s

    2015-08-25 21:17:21 (228 KB/s) - “shakespeare.tar.gz” saved [2087964/2087964]

    [root@sandbox ~]# ls -l shakespeare.tar.gz
    -rw-r--r-- 1 root root 2087964 1995-07-25 06:13 shakespeare.tar.gz

Unzip the William Shakespeare data

    [root@sandbox ~]# mkdir shakespeare
    [root@sandbox ~]# cd shakespeare
    [root@sandbox shakespeare]# tar xvfz ../shakespeare.tar.gz
    README
    comedies/asyoulikeit
    comedies/comedyoferrors
    comedies/cymbeline
    comedies/loveslabourslost
    comedies/measureforemeasure
    comedies/merchantofvenice
    comedies/merrywivesofwindsor
    comedies/midsummersnightsdream
    comedies/muchadoaboutnothing
    comedies/periclesprinceoftyre
    comedies/tamingoftheshrew
    comedies/tempest
    comedies/troilusandcressida
    comedies/twelfthnight
    comedies/twogentlemenofverona
    comedies/winterstale
    comedies/allswellthatendswell
    glossary
    histories/1kinghenryvi
    histories/2kinghenryiv
    histories/2kinghenryvi
    histories/3kinghenryvi
    histories/kinghenryv
    histories/kinghenryviii
    histories/kingjohn
    histories/kingrichardii
    histories/kingrichardiii
    histories/1kinghenryiv
    poetry/various
    poetry/rapeoflucrece
    poetry/sonnets
    poetry/venusandadonis
    poetry/loverscomplaint
    tragedies/coriolanus
    tragedies/hamlet
    tragedies/kinglear
    tragedies/macbeth
    tragedies/othello
    tragedies/romeoandjuliet
    tragedies/timonofathens
    tragedies/titusandronicus
    tragedies/juliuscaesar
    tragedies/antonyandcleopatra

    [root@sandbox shakespeare]# ls -l
    total 80
    drwxr-xr-x 2 root  root  4096 2015-08-25 21:20 comedies
    -rw-r--r-- 1 oozie   28 58966 1992-08-29 05:47 glossary
    drwxr-xr-x 2 root  root  4096 2015-08-25 21:20 histories
    drwxr-xr-x 2 root  root  4096 2015-08-25 21:20 poetry
    -rw-r--r-- 1 oozie   28   971 1992-08-29 06:57 README
    drwxr-xr-x 2 root  root  4096 2015-08-25 21:20 tragedies
    [root@sandbox shakespeare]#

Next we will create a directory in HDFS and upload the data set.

    [root@sandbox ~]# hdfs dfs -mkdir -p /data/shakespeare
    [root@sandbox ~]# hdfs dfs -put * /data/shakespeare
    [root@sandbox ~]# hdfs dfs -ls /data/shakespeare
    Found 6 items
    -rw-r--r--   1 root hdfs        971 2015-08-25 21:23 /data/shakespeare/README
    drwxr-xr-x   - root hdfs          0 2015-08-25 21:23 /data/shakespeare/comedies
    -rw-r--r--   1 root hdfs      58966 2015-08-25 21:23 /data/shakespeare/glossary
    drwxr-xr-x   - root hdfs          0 2015-08-25 21:23 /data/shakespeare/histories
    drwxr-xr-x   - root hdfs          0 2015-08-25 21:23 /data/shakespeare/poetry
    drwxr-xr-x   - root hdfs          0 2015-08-25 21:23 /data/shakespeare/tragedies
    [root@sandbox shakespeare]# hdfs dfs -ls /data/shakespeare/comedies
    Found 17 items
    -rw-r--r--   1 root hdfs     135369 2015-08-25 21:23
    /data/shakespeare/comedies/allswellthatendswell
    -rw-r--r--   1 root hdfs     125179 2015-08-25 21:23
    /data/shakespeare/comedies/asyoulikeit
    -rw-r--r--   1 root hdfs      89525 2015-08-25 21:23
    /data/shakespeare/comedies/comedyoferrors
    -rw-r--r--   1 root hdfs     165209 2015-08-25 21:23
    /data/shakespeare/comedies/cymbeline
    -rw-r--r--   1 root hdfs     129986 2015-08-25 21:23
    /data/shakespeare/comedies/loveslabourslost
    -rw-r--r--   1 root hdfs     130473 2015-08-25 21:23
    /data/shakespeare/comedies/measureforemeasure
    -rw-r--r--   1 root hdfs     122658 2015-08-25 21:23
    /data/shakespeare/comedies/merchantofvenice
    -rw-r--r--   1 root hdfs     131576 2015-08-25 21:23
    /data/shakespeare/comedies/merrywivesofwindsor
    -rw-r--r--   1 root hdfs      96508 2015-08-25 21:23
    /data/shakespeare/comedies/midsummersnightsdream
    -rw-r--r--   1 root hdfs     123413 2015-08-25 21:23
    /data/shakespeare/comedies/muchadoaboutnothing
    -rw-r--r--   1 root hdfs     111604 2015-08-25 21:23
    /data/shakespeare/comedies/periclesprinceoftyre
    -rw-r--r--   1 root hdfs     124237 2015-08-25 21:23
    /data/shakespeare/comedies/tamingoftheshrew
    -rw-r--r--   1 root hdfs      99379 2015-08-25 21:23
    /data/shakespeare/comedies/tempest
    -rw-r--r--   1 root hdfs     158946 2015-08-25 21:23
    /data/shakespeare/comedies/troilusandcressida
    -rw-r--r--   1 root hdfs     116759 2015-08-25 21:23
    /data/shakespeare/comedies/twelfthnight
    -rw-r--r--   1 root hdfs     102007 2015-08-25 21:23
    /data/shakespeare/comedies/twogentlemenofverona
    -rw-r--r--   1 root hdfs     145794 2015-08-25 21:23
    /data/shakespeare/comedies/winterstale

**Note:** For the next three exercises we will be running the grep, wordcount,
and wordmean from the *hadoop-mapreduce-examples.jar* file. This is located in
the **/usr/hdp/<version>/hadoop-mapreduce** directory. Please replace the
<version> with the current Sandbox version you are running with.

#### Grep

We will run the grep example against the William Shakespeare comedies listed in
*/data/shakespeare/comedies*

    [root@sandbox shakespeare]# yarn jar /usr/hdp/current/hadoop-mapreduce-client
    /hadoop-mapreduce-examples.jar grep /data/shakespeare/comedies /data/grep_out
    the
    15/08/25 21:40:27 INFO impl.TimelineClientImpl: Timeline service address:
    http://sandbox.hortonworks.com:8188/ws/v1/timeline/
    15/08/25 21:40:27 INFO client.RMProxy: Connecting to ResourceManager at
    sandbox.hortonworks.com/192.168.148.218:8050
    15/08/25 21:40:27 INFO input.FileInputFormat: Total input paths to process : 17
    15/08/25 21:40:27 INFO mapreduce.JobSubmitter: number of splits:17
    15/08/25 21:40:27 INFO mapreduce.JobSubmitter: Submitting tokens for job:
    job_1440428477248_0004
    15/08/25 21:40:27 INFO impl.YarnClientImpl: Submitted application
    application_1440428477248_0004
    15/08/25 21:40:27 INFO mapreduce.Job: The url to track the job:
    http://sandbox.hortonworks.com:8088/proxy/application_1440428477248_0004/
    15/08/25 21:40:27 INFO mapreduce.Job: Running job: job_1440428477248_0004
    15/08/25 21:40:33 INFO mapreduce.Job: Job job_1440428477248_0004 running in uber
    mode : false
    15/08/25 21:40:33 INFO mapreduce.Job:  map 0% reduce 0%
    15/08/25 21:40:44 INFO mapreduce.Job:  map 18% reduce 0%
    15/08/25 21:40:45 INFO mapreduce.Job:  map 47% reduce 0%
    15/08/25 21:40:54 INFO mapreduce.Job:  map 59% reduce 0%
    15/08/25 21:40:55 INFO mapreduce.Job:  map 88% reduce 0%
    15/08/25 21:40:58 INFO mapreduce.Job:  map 94% reduce 0%
    15/08/25 21:40:59 INFO mapreduce.Job:  map 100% reduce 0%
    15/08/25 21:41:00 INFO mapreduce.Job:  map 100% reduce 100%
    15/08/25 21:41:00 INFO mapreduce.Job: Job job_1440428477248_0004 completed
    successfully
    15/08/25 21:41:00 INFO mapreduce.Job: Counters: 49
            File System Counters
                    FILE: Number of bytes read=244
                    FILE: Number of bytes written=2283926
                    FILE: Number of read operations=0
                    FILE: Number of large read operations=0
                    FILE: Number of write operations=0
                    HDFS: Number of bytes read=2111048
                    HDFS: Number of bytes written=106
                    HDFS: Number of read operations=54
                    HDFS: Number of large read operations=0
                    HDFS: Number of write operations=2
            Job Counters
                    Launched map tasks=17
                    Launched reduce tasks=1
                    Data-local map tasks=17
                    Total time spent by all maps in occupied slots (ms)=149736
                    Total time spent by all reduces in occupied slots (ms)=12832
                    Total time spent by all map tasks (ms)=149736
                    Total time spent by all reduce tasks (ms)=12832
                    Total vcore-seconds taken by all map tasks=149736
                    Total vcore-seconds taken by all reduce tasks=12832
                    Total megabyte-seconds taken by all map tasks=37434000
                    Total megabyte-seconds taken by all reduce tasks=3208000
            Map-Reduce Framework
                    Map input records=70366
                    Map output records=18391
                    Map output bytes=220692
                    Map output materialized bytes=340
                    Input split bytes=2426
                    Combine input records=18391
                    Combine output records=17
                    Reduce input groups=1
                    Reduce shuffle bytes=340
                    Reduce input records=17
                    Reduce output records=1
                    Spilled Records=34
                    Shuffled Maps =17
                    Failed Shuffles=0
                    Merged Map outputs=17
                    GC time elapsed (ms)=1336
                    CPU time spent (ms)=10020
                    Physical memory (bytes) snapshot=3590262784
                    Virtual memory (bytes) snapshot=14613901312
                    Total committed heap usage (bytes)=2378694656
            Shuffle Errors
                    BAD_ID=0
                    CONNECTION=0
                    IO_ERROR=0
                    WRONG_LENGTH=0
                    WRONG_MAP=0
                    WRONG_REDUCE=0
            File Input Format Counters
                    Bytes Read=2108622
            File Output Format Counters
                    Bytes Written=106
    15/08/25 21:41:00 INFO impl.TimelineClientImpl: Timeline service address:
    http://sandbox.hortonworks.com:8188/ws/v1/timeline/
    15/08/25 21:41:00 INFO client.RMProxy: Connecting to ResourceManager at
    sandbox.hortonworks.com/192.168.148.218:8050
    15/08/25 21:41:00 INFO input.FileInputFormat: Total input paths to process : 1
    15/08/25 21:41:00 INFO mapreduce.JobSubmitter: number of splits:1
    15/08/25 21:41:00 INFO mapreduce.JobSubmitter: Submitting tokens for job:
    job_1440428477248_0005
    15/08/25 21:41:00 INFO impl.YarnClientImpl: Submitted application
    application_1440428477248_0005
    15/08/25 21:41:00 INFO mapreduce.Job: The url to track the job:
    http://sandbox.hortonworks.com:8088/proxy/application_1440428477248_0005/
    15/08/25 21:41:00 INFO mapreduce.Job: Running job: job_1440428477248_0005
    15/08/25 21:41:05 INFO mapreduce.Job: Job job_1440428477248_0005 running in uber
    mode : false
    15/08/25 21:41:05 INFO mapreduce.Job:  map 0% reduce 0%
    15/08/25 21:41:09 INFO mapreduce.Job:  map 100% reduce 0%
    15/08/25 21:41:15 INFO mapreduce.Job:  map 100% reduce 100%
    15/08/25 21:41:15 INFO mapreduce.Job: Job job_1440428477248_0005 completed
    successfully
    15/08/25 21:41:15 INFO mapreduce.Job: Counters: 49
            File System Counters
                    FILE: Number of bytes read=20
                    FILE: Number of bytes written=252643
                    FILE: Number of read operations=0
                    FILE: Number of large read operations=0
                    FILE: Number of write operations=0
                    HDFS: Number of bytes read=250
                    HDFS: Number of bytes written=10
                    HDFS: Number of read operations=7
                    HDFS: Number of large read operations=0
                    HDFS: Number of write operations=2
            Job Counters
                    Launched map tasks=1
                    Launched reduce tasks=1
                    Data-local map tasks=1
                    Total time spent by all maps in occupied slots (ms)=2246
                    Total time spent by all reduces in occupied slots (ms)=3452
                    Total time spent by all map tasks (ms)=2246
                    Total time spent by all reduce tasks (ms)=3452
                    Total vcore-seconds taken by all map tasks=2246
                    Total vcore-seconds taken by all reduce tasks=3452
                    Total megabyte-seconds taken by all map tasks=561500
                    Total megabyte-seconds taken by all reduce tasks=863000
            Map-Reduce Framework
                    Map input records=1
                    Map output records=1
                    Map output bytes=12
                    Map output materialized bytes=20
                    Input split bytes=144
                    Combine input records=0
                    Combine output records=0
                    Reduce input groups=1
                    Reduce shuffle bytes=20
                    Reduce input records=1
                    Reduce output records=1
                    Spilled Records=2
                    Shuffled Maps =1
                    Failed Shuffles=0
                    Merged Map outputs=1
                    GC time elapsed (ms)=82
                    CPU time spent (ms)=1050
                    Physical memory (bytes) snapshot=344211456
                    Virtual memory (bytes) snapshot=1660329984
                    Total committed heap usage (bytes)=264765440
            Shuffle Errors
                    BAD_ID=0
                    CONNECTION=0
                    IO_ERROR=0
                    WRONG_LENGTH=0
                    WRONG_MAP=0
                    WRONG_REDUCE=0
            File Input Format Counters
                    Bytes Read=106
            File Output Format Counters
                    Bytes Written=10

Now we can examine the output of the grep program. The output was written into
`/data/grep_out`

    [root@sandbox shakespeare]# hdfs dfs -ls /data/grep_out
    Found 2 items
    -rw-r--r--   1 root hdfs          0 2015-08-25 21:41 /data/grep_out/_SUCCESS
    -rw-r--r--   1 root hdfs         10 2015-08-25 21:41 /data/grep_out/part-r-00000

If we look at the contents we can see that the word **the** appears 18391 times.

    [root@sandbox shakespeare]# hdfs dfs -cat /data/grep_out/part-r-00000
    18391   the

#### Word-Count

We will run the word count example against the William Shakespeare comedies
listed in */data/shakespeare/comedies*

    [root@sandbox shakespeare]# yarn jar /usr/hdp/current/hadoop-mapreduce-client
    /hadoop-mapreduce-examples.jar wordcount /data/shakespeare/comedies
    /data/wordcount_out
    15/08/25 21:29:21 INFO impl.TimelineClientImpl: Timeline service address:
    http://sandbox.hortonworks.com:8188/ws/v1/timeline/
    15/08/25 21:29:21 INFO client.RMProxy: Connecting to ResourceManager at
    sandbox.hortonworks.com/192.168.148.218:8050
    15/08/25 21:29:22 INFO input.FileInputFormat: Total input paths to process : 17
    15/08/25 21:29:22 INFO mapreduce.JobSubmitter: number of splits:17
    15/08/25 21:29:22 INFO mapreduce.JobSubmitter: Submitting tokens for job:
    job_1440428477248_0003
    15/08/25 21:29:22 INFO impl.YarnClientImpl: Submitted application
    application_1440428477248_0003
    15/08/25 21:29:22 INFO mapreduce.Job: The url to track the job:
    http://sandbox.hortonworks.com:8088/proxy/application_1440428477248_0003/
    15/08/25 21:29:22 INFO mapreduce.Job: Running job: job_1440428477248_0003
    15/08/25 21:29:27 INFO mapreduce.Job: Job job_1440428477248_0003 running in uber
    mode : false
    15/08/25 21:29:27 INFO mapreduce.Job:  map 0% reduce 0%
    15/08/25 21:29:40 INFO mapreduce.Job:  map 6% reduce 0%
    15/08/25 21:29:41 INFO mapreduce.Job:  map 47% reduce 0%
    15/08/25 21:29:50 INFO mapreduce.Job:  map 53% reduce 0%
    15/08/25 21:29:52 INFO mapreduce.Job:  map 65% reduce 0%
    15/08/25 21:29:53 INFO mapreduce.Job:  map 82% reduce 0%
    15/08/25 21:29:54 INFO mapreduce.Job:  map 88% reduce 0%
    15/08/25 21:29:56 INFO mapreduce.Job:  map 100% reduce 0%
    15/08/25 21:29:57 INFO mapreduce.Job:  map 100% reduce 100%
    15/08/25 21:29:57 INFO mapreduce.Job: Job job_1440428477248_0003 completed
    successfully
    15/08/25 21:29:57 INFO mapreduce.Job: Counters: 49
            File System Counters
                    FILE: Number of bytes read=1258994
                    FILE: Number of bytes written=4795180
                    FILE: Number of read operations=0
                    FILE: Number of large read operations=0
                    FILE: Number of write operations=0
                    HDFS: Number of bytes read=2111048
                    HDFS: Number of bytes written=410977
                    HDFS: Number of read operations=54
                    HDFS: Number of large read operations=0
                    HDFS: Number of write operations=2
            Job Counters
                    Launched map tasks=17
                    Launched reduce tasks=1
                    Data-local map tasks=17
                    Total time spent by all maps in occupied slots (ms)=176091
                    Total time spent by all reduces in occupied slots (ms)=14330
                    Total time spent by all map tasks (ms)=176091
                    Total time spent by all reduce tasks (ms)=14330
                    Total vcore-seconds taken by all map tasks=176091
                    Total vcore-seconds taken by all reduce tasks=14330
                    Total megabyte-seconds taken by all map tasks=44022750
                    Total megabyte-seconds taken by all reduce tasks=3582500
            Map-Reduce Framework
                    Map input records=70366
                    Map output records=377452
                    Map output bytes=3555826
                    Map output materialized bytes=1259090
                    Input split bytes=2426
                    Combine input records=377452
                    Combine output records=94174
                    Reduce input groups=39502
                    Reduce shuffle bytes=1259090
                    Reduce input records=94174
                    Reduce output records=39502
                    Spilled Records=188348
                    Shuffled Maps =17
                    Failed Shuffles=0
                    Merged Map outputs=17
                    GC time elapsed (ms)=1437
                    CPU time spent (ms)=24530
                    Physical memory (bytes) snapshot=3547303936
                    Virtual memory (bytes) snapshot=14598098944
                    Total committed heap usage (bytes)=2373451776
            Shuffle Errors
                    BAD_ID=0
                    CONNECTION=0
                    IO_ERROR=0
                    WRONG_LENGTH=0
                    WRONG_MAP=0
                    WRONG_REDUCE=0
            File Input Format Counters
                    Bytes Read=2108622
            File Output Format Counters
                    Bytes Written=410977

Now we can examine the output of the word count program. Note that this is a
very simplistic word count program and it does not take into account punctuation
at the end of words or even trying to match words independent of case
sensitivity.
The output was written into `/data/wordcount_out`

    [root@sandbox shakespeare]# hdfs dfs -ls /data/wordcount_out
    Found 2 items
    -rw-r--r--   1 root hdfs          0 2015-08-25 21:29
    /data/wordcount_out/_SUCCESS
    -rw-r--r--   1 root hdfs     410977 2015-08-25 21:29
    /data/wordcount_out/part-r-00000

The following commands will look at the first 10 words beginning with *the* and
*The* to illustrate what the word count program has done.

    [root@sandbox shakespeare]# hdfs dfs -cat /data/wordcount_out/part*|grep "^the"
    | head -10
    the     9883
    the--   1
    theatre 1
    thee    644
    thee!   35
    thee!'  1
    thee,   282
    thee,-- 2
    thee,--if       1
    thee--  1

    [root@sandbox shakespeare]# hdfs dfs -cat /data/wordcount_out/part*|grep "^The"
    | head -10
    The     1382
    Thebes  1
    Thee    3
    Their   42
    Then    172
    Then,   37
    There   188
    There's 66
    There,  15
    There.  1

We can see that the word **the** has occurred 9883 times and the word **The** an
additional 1382 times in the comedies of William Shakespeare. To note, the
simple word count program does not distinguish between the different ending
characters of the word **thee**. Since it is only looking for whitespace, the
additional punctuation is treated as different words for each.

#### Wordmean

The *wordmean* example program counts the average length of the words in the
input files

    [root@sandbox ~]# yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-
    mapreduce-examples.jar wordmean /data/shakespeare/comedies /data/wordmean_out
    15/08/26 21:03:02 INFO impl.TimelineClientImpl: Timeline service address:
    http://sandbox.hortonworks.com:8188/ws/v1/timeline/
    15/08/26 21:03:02 INFO client.RMProxy: Connecting to ResourceManager at
    sandbox.hortonworks.com/192.168.148.218:8050
    15/08/26 21:03:03 INFO input.FileInputFormat: Total input paths to process : 17
    15/08/26 21:03:03 INFO mapreduce.JobSubmitter: number of splits:17
    15/08/26 21:03:03 INFO mapreduce.JobSubmitter: Submitting tokens for job:
    job_1440614713932_0013
    15/08/26 21:03:03 INFO impl.YarnClientImpl: Submitted application
    application_1440614713932_0013
    15/08/26 21:03:03 INFO mapreduce.Job: The url to track the job:
    http://sandbox.hortonworks.com:8088/proxy/application_1440614713932_0013/
    15/08/26 21:03:03 INFO mapreduce.Job: Running job: job_1440614713932_0013
    15/08/26 21:03:08 INFO mapreduce.Job: Job job_1440614713932_0013 running in uber
    mode : false
    15/08/26 21:03:08 INFO mapreduce.Job:  map 0% reduce 0%
    15/08/26 21:03:22 INFO mapreduce.Job:  map 35% reduce 0%
    15/08/26 21:03:23 INFO mapreduce.Job:  map 47% reduce 0%
    15/08/26 21:03:31 INFO mapreduce.Job:  map 53% reduce 0%
    15/08/26 21:03:32 INFO mapreduce.Job:  map 59% reduce 0%
    15/08/26 21:03:34 INFO mapreduce.Job:  map 71% reduce 0%
    15/08/26 21:03:36 INFO mapreduce.Job:  map 88% reduce 0%
    15/08/26 21:03:38 INFO mapreduce.Job:  map 100% reduce 0%
    15/08/26 21:03:39 INFO mapreduce.Job:  map 100% reduce 100%
    15/08/26 21:03:39 INFO mapreduce.Job: Job job_1440614713932_0013 completed
    successfully
    15/08/26 21:03:40 INFO mapreduce.Job: Counters: 49
            File System Counters
                    FILE: Number of bytes read=567
                    FILE: Number of bytes written=2278308
                    FILE: Number of read operations=0
                    FILE: Number of large read operations=0
                    FILE: Number of write operations=0
                    HDFS: Number of bytes read=2111048
                    HDFS: Number of bytes written=28
                    HDFS: Number of read operations=54
                    HDFS: Number of large read operations=0
                    HDFS: Number of write operations=2
            Job Counters
                    Launched map tasks=17
                    Launched reduce tasks=1
                    Data-local map tasks=17
                    Total time spent by all maps in occupied slots (ms)=183470
                    Total time spent by all reduces in occupied slots (ms)=14175
                    Total time spent by all map tasks (ms)=183470
                    Total time spent by all reduce tasks (ms)=14175
                    Total vcore-seconds taken by all map tasks=183470
                    Total vcore-seconds taken by all reduce tasks=14175
                    Total megabyte-seconds taken by all map tasks=45867500
                    Total megabyte-seconds taken by all reduce tasks=3543750
            Map-Reduce Framework
                    Map input records=70366
                    Map output records=754904
                    Map output bytes=10946108
                    Map output materialized bytes=663
                    Input split bytes=2426
                    Combine input records=754904
                    Combine output records=34
                    Reduce input groups=2
                    Reduce shuffle bytes=663
                    Reduce input records=34
                    Reduce output records=2
                    Spilled Records=68
                    Shuffled Maps =17
                    Failed Shuffles=0
                    Merged Map outputs=17
                    GC time elapsed (ms)=1406
                    CPU time spent (ms)=17590
                    Physical memory (bytes) snapshot=3604451328
                    Virtual memory (bytes) snapshot=14649790464
                    Total committed heap usage (bytes)=2380267520
            Shuffle Errors
                    BAD_ID=0
                    CONNECTION=0
                    IO_ERROR=0
                    WRONG_LENGTH=0
                    WRONG_MAP=0
                    WRONG_REDUCE=0
            File Input Format Counters
                    Bytes Read=2108622
            File Output Format Counters
                    Bytes Written=28
    The mean is: 4.420604474211291

The output of the MapReduce job above displays that the average (mean) of the
word length of William Shakespeare's comedies is 4.42 letters.

We can look at the output that was produced:

    [root@sandbox ~]# hdfs dfs -ls /data/wordmean_out
    Found 2 items
    -rw-r--r--   1 root hdfs          0 2015-08-26 21:03 /data/wordmean_out/_SUCCESS
    -rw-r--r--   1 root hdfs         28 2015-08-26 21:03
    /data/wordmean_out/part-r-00000

The contents of the *part-r-00000* file contains:

    [root@sandbox ~]# hdfs dfs -cat /data/wordmean_out/part-r-00000
    count   377452
    length  1668566

The average length was calculated based on the output of these two values. The
reduce phase counted the total number of words found in all of the comedies and
the total length of all the words combined. By dividing the length by the count
we get the average (mean):

    length / count = mean
    1668566 / 377452 = 4.42060447

