<a name="Application"></a>

## Running Applications using Hortonworks Sandbox

- Why use the sandbox instead of EMR
- Downloading and Installing Hortonworks Sandbox
- Use hadoop examples jar's grep, word-count, and wordmean
- Use use these to split movie reviews into positive and negative
- Run word count on the two sets of files
- See what words are most common in each set

### Why use the sandbox instead of EMR

Q: What is the Hortonworks Sandbox?

- Instead of running Hadoop on a cluster the Hortonworks Sandbox lets
  you run it locally in a virtual machine.

Q: Why would I need the sandbox?

- While in production you will run a cluster on Amazon, for
  development and testing it is a lot easier to spin up a one-machine
  cluster locally.

- It is a great training and learning environment for experimenting
  with new technologies.

- It is a great development environment where you can use small data
  sets to verify that your application logic is correct.

- Finally once everything is tested you can run your analysis on real
  data on EMR.

- Also this is (a lot) cheaper.

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

**Step 1:** Download and uncompress Shakespeare's works.

Download the dataset 'Complete Works of William Shakespeare' from
<http://www.it.usyd.edu.au/~matty/Shakespeare/shakespeare.tar.gz> in
the sandbox instance.

    [root@sandbox ~]# wget http://www.it.usyd.edu.au/~matty/Shakespeare/shakespeare.tar.gz

Unzip the William Shakespeare data

    mkdir shakespeare
    cd shakespeare
    tar xvfz ../shakespeare.tar.gz

Make sure you have all the files.

    ls -l

**Step 2:** Create a directory in HDFS called `/data/shakespeare`

**Step 3:** Verify using `hadoop fs -ls -R /data/shakespeare` that your upload worked.

**Note:** For the next three exercises we will be running the grep,
wordcount, and wordmean from the *hadoop-mapreduce-examples.jar* file.
This is located in the **/usr/hdp/<version>/hadoop-mapreduce**
directory. Please replace the `current` in the paths below with the
current Sandbox version you are running with.

#### Grep

Use this command to find the number of times that `the` occurs in
`/data/shakespeare/comedies`.

    yarn jar /usr/hdp/current/hadoop-mapreduce-client \
        /hadoop-mapreduce-examples.jar grep /data/shakespeare/comedies /data/grep_out \
        the

Look at the contents of `/data/grep_out` in HDFS to find out how many
times `the` occurred.

#### Exploring Examples

Run this command to get a list of all the sub-programs under
`hadoop-mapreduce-examples.jar`

    yarn jar /usr/hdp/current/hadoop-mapreduce-client \
        /hadoop-mapreduce-examples.jar

#### Word-Count

Run `wordcount` against `/data/shakespeare/comedies`. This calculates
the frequency of all the words.

Look at the output directory to verify that the command worked and
produced results.

#### Wordmean

Run `wordmean` against `/data/shakespeare/comedies`. This calculates
the average word length across all the words.
