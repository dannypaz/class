Intro to Parallelization
-----

#### By the end of this article you should have:

- Watched:
    - Multiprocessing with Python
- Read:
    - Parallel MapReduce in Python in Ten Minutes
    - Using `ipyparallel`

----

When we talk about distributed systems, we are typically talking about a multi-node architecture. What a "node" is can be a little abstract. At first glance, we can see a node as a computer, such as an EC2 instance or your laptop. But these days, even a single node can have many physical computing elements including multiple cores on CPUs, not to mention the GPU. We can host multiple virtual machines which would act as nodes on a single physical machine, and we can create more virtual engines to share processing on our cores. As usual, when computing, we are more interested in the logical architecture than the physical one, so we will talk in terms of nodes and engines and not in terms of computers and CPUs. For this lesson, we will focus on distributing processing across multiple engines on a single node. Later, we will scale out to multiple nodes.

The Python library I like to use for simple parallel processing (which we will be using for our lab) is [`ipyparallel`](http://ipyparallel.readthedocs.io/en/latest/intro.html). I like it because it is relatively easy to use and also because it can scale to a multi-node architecture without changing anything. (That is, once it knows about other nodes running ipython engines, it can treat them all as if they were on one giant computer.) Unfortunately, I was not able to find any good videos explaining ipyparallel, so we will have to settle on Pinku Surana's DevelopMentor webinar: [Multiprocessing with Python](https://www.youtube.com/watch?v=s1SkCYMnfbY). By the end of it, you should be able to explain what the GIL is and why it matters. You should also be able to use the `multiprocessing` library in Python. Once you've completed that video, take a look at Michael Cvet's blog on [Parallel MapReduce in Python in Ten Minutes](https://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/). Be aware that because this is a WordPress blog, it automatically tried to change `(w)` in line 13 of one of the snippets into an image containing the WordPress logo. (So where it says `w = sanitize <img width="16" height="16" class="wp-smiley emoji" draggable="false" alt="(w)" src="https://s2.wp.com/wp-content/mu-plugins/wpcom-smileys/wordpress.svg" style="height: 1em; max-height: 1em;" scale="0">`, it should say `w = sanitize(w)`.) Once you've read through this, you should be able to explain the basics of the MapReduce pattern and implement it in Python.

Once you've completed that, read through this primer on [Using `ipyparallel`](http://people.duke.edu/~ccc14/sta-663-2016/19C_IPyParallel.html) (actually, the whole course on [Computational Statistics in Python](http://people.duke.edu/~ccc14/sta-663-2016/index.html) is probably worth bookmarking).

**Optional:** Now would be a good time to go through lesson 2 in the Cloud Computing Concepts course we started last week with the following two lectures:

1. [A cloud IS a distributed system](https://www.coursera.org/learn/cloud-computing/lecture/DI6AV/2-1-a-cloud-is-a-distributed-system)
2. [What is a distributed system?](https://www.coursera.org/learn/cloud-computing/lecture/nvMXE/2-2-what-is-a-distributed-system)

Though not required for this lesson, they will help prepare you for tomorrow's lesson.

---

#### On completing this article, you should have:

- Watched 1 video
- Read one blog post and one Computational Statistics in Python lesson
