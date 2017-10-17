Final Project Proposal
----------------

By the end of today, you should have a fleshed out proposal for a "big data" system that satisfies most if not all of the desired properties described in today's [README](README.md). You must provide two things:

1. A diagram describing your architecture including the tools used. You may use Graphviz (like in the [Lab Overview](../Lab Overview.ipynb)) or [Gliffy](https://www.gliffy.com/) or even pen and paper (in which case you should upload a photo). The important thing is that it is clear both to you and to us what is involved in your design and how it all connects.  **At minimum, your architecture should have the following characteristics:**
    1. **Stream**: A way to continuously query data from a website or API (at least one, but preferably two sources of data)
    2. **Store**: Storage for all unstructured data in its entirety
    3. **Structure**: Separate storage for structured data in 3NF (similar to how we stored raw tweets in s3 and structured tables in postgres)
    4. **Synthesize**: Some sort of batch process/transformation with Spark
    5. **Show**: A way to communicate the results of your pipeline such as a static website or flask app

2. Take a look at each of the 8 desired properties of a big data system and answer the following two questions:
    1. How does my system have this property?
    2. How does my system fall short and how could it be improved?

As an example, the system we've been building in class is scalable both in terms of data storage and in processing, though it's possible that the node that serves as the pipeline between Twitter and Kinesis could fall over if sampling were turned off. At the same time, we have done very little to make sure our system would be easy to debug. (Remember the discussion on how to deal with corrupt data. Does your `except` clause just pass on to the next row, or does it record the failure somewhere?)
