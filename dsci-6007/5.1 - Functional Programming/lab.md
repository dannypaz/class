# Meet MrJob

`mrjob` is a Python package that helps you write and run Hadoop Streaming jobs. It supports Amazon's Elastic MapReduce (EMR) and it also works with your own Hadoop cluster.  It has been released as an open-source framework by Yelp and we will use it as interface for Hadoop due to its legibility and ease to use with MapReduce tasks.  Feel free to take a pause and read through some of the [mrjob docs](http://mrjob.readthedocs.org/en/latest/index.html) or this [mrjob tutorial](https://pythonhosted.org/mrjob/guides/quickstart.html) to familarize yourself with the main concepts.

`mrjob` fully supports Amazon's Elastic MapReduce (EMR) service, which allows you to buy time on a Hadoop cluster on an hourly basis. It also works with your own Hadoop cluster.

Some important features:

* Run jobs on EMR, your own Hadoop cluster, or locally (for testing).
* Write multi-step jobs (one map-reduce step feeds into the next)

## Refactoring for MRJob

1. Install the `mrjob` python module:

    ```
    pip install mrjob
    ```

2. Go back to [Tuesday's lab](../MapReduce Intro/lab.md) and rework your solution to use MRJob instead of Hadoop Streaming. Note:
    1. You will now have one file instead of two.
    2. You can test this locally without a Hadoop instance.

3. Implement [`combiner`](https://pythonhosted.org/mrjob/job.html#mrjob.job.MRJob.combiner)s in your MRJob classes.

4. Which design pattern(s) that you learned about can help us here. Implement that in your combiner.

5. Run on Amazon EMR

	1. Set up your MrJob config file. Check out the [documentation](https://pythonhosted.org/mrjob/guides/emr-quickstart.html).
	
	    * Create `~/.mrjob.conf`
	    * Set the environment variables `aws_access_key_id` and `aws_secret_access_key`.
	
	2. Do the same task, but this time in the cloud! Use the `-r emr` flag to tell `mrjob` to use EMR instead of running the job locally.


## Extra Credit: Counters

Since word counts are really common, MrJob has a counter built in. Here's a version of the simple word count script using the counter:

```python
'''The classic MapReduce job: count the frequency of words.'''

from mrjob.job import MRJob
from string import punctuation


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            self.increment_counter("word", word.strip(punctuation).lower())

if __name__ == '__main__':
    MRWordFreqCount.run()

```

1. Run this. Note that the output is now in the logs, so you need to run it like this to save the results:

    ```
    python wordcounts2.py mini_20_newsgroups/ 2> counts2
    ```

2. Can you use `increment_counter` above instead of how you implementing your word count by topic script?
