HDFS and MapReduce
----

#### By the end of this article you should have:

- Watched:
    - Lessons 2 and 3 of Udacity's Intro to Hadoop and MapReduce course
    - The Combiners and Partition Functions lecture from Stanford's Mining of Massive Datasets course

----

These next two lessons will utilize Udacity's [Intro to Hadoop and MapReduce](https://classroom.udacity.com/courses/ud617) course. We will also borrow a lecture from Stanford's [Mining of Massive Datasets](http://web.stanford.edu/class/cs246/) course to help elucidate combiners, an important but frequently misunderstood component in Hadoop's implementation of the MapReduce framework. You may skip or skim [lesson 1](https://classroom.udacity.com/courses/ud617/lessons/306818608/concepts/3092736490923) on Big Data as much of it is redundant with the first day of this course though it may be worth your while to watch Doug Cutting's [short history of Hadoop](https://classroom.udacity.com/courses/ud617/lessons/306818608/concepts/3138018500923) as well as the lectures on [Core Hadoop](https://classroom.udacity.com/courses/ud617/lessons/306818608/concepts/3092736770923) and the [Hadoop Ecosystem](https://classroom.udacity.com/courses/ud617/lessons/306818608/concepts/3092736780923). Quiz yourself with the [lesson 1 problem set](https://classroom.udacity.com/courses/ud617/lessons/312821779/concepts/3119546880923) to make sure you're ready.

1. Lesson 2: HDFS and MapReduce
    1. Quiz: HDFS - [YouTube](https://www.youtube.com/watch?v=vdkx2xasGlM) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715640923)
    2. Quiz: Data Redundancy - [YouTube](https://www.youtube.com/watch?v=LV1ncV1MO_g) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715680923)
    3. NameNode Standby - [YouTube](https://www.youtube.com/watch?v=E28J0XY9PEM) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715720923)
    4. HDFS Demo - [YouTube](https://www.youtube.com/watch?v=l0I_2nyPNZM) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3095085570923)
    5. MapReduce - [YouTube](https://www.youtube.com/watch?v=7TdCRQa4Yi0) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715730923)
    6. Real World Example - [YouTube](https://www.youtube.com/watch?v=53jdaPf249c) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715740923)
    7. Quiz: Hashtables - [YouTube](https://www.youtube.com/watch?v=KCNKb4-t9WA) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715750923)
    8. Distributed Work - [YouTube](https://www.youtube.com/watch?v=LZfCPgQmeRU) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/4406186530923)
    9. Summary of MapReduce - [YouTube](https://www.youtube.com/watch?v=trDuPnmO8Y8) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3279185400923)
    10. Quiz: Sort Final Result - [YouTube](https://www.youtube.com/watch?v=USTw7q1FooY) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715800923)
    11. Quiz: Multiple Reducers - [YouTube](https://www.youtube.com/watch?v=kSQn47BEQos) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715840923)
    12. Daemons of MapReduce - [YouTube](https://www.youtube.com/watch?v=CyRECFXtVlQ) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715880923)
    13. Running a Job - [YouTube](https://www.youtube.com/watch?v=WyEkdh1Qptk) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3093825950923)
    14. Simplifying Things - [YouTube](https://www.youtube.com/watch?v=d5TZ_2I7dwE) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3093825960923)
    15. A Different Application - [YouTube](https://www.youtube.com/watch?v=0lmk2_lynvE) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3092715890923)
    16. Other Problems - [YouTube](https://www.youtube.com/watch?v=oJCi-JXkOhI) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3127086110923)
    17. Virtual Machine Setup - [YouTube](https://www.youtube.com/watch?v=z1mHYk5aXWE) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3135238740923)
    18. Conclusion - [YouTube](https://www.youtube.com/watch?v=Rx7dD3oWyok) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3139220360923)
2. Mining Massive Datasets: [Combiners and Partition Functions](https://www.youtube.com/watch?v=jYjZ527n-ZU)
3. Lesson 3: MapReduce Code
    1. Introduction - [YouTube](https://www.youtube.com/watch?v=gL1fd3toTGY) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3139967110923)
    2. Quiz: Input Data - [YouTube](https://www.youtube.com/watch?v=YMVGkwE0Apc) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3093825750923)
    3. Quiz: Defensive Mapper Code - [YouTube](https://www.youtube.com/watch?v=pRWMwSP0zrk) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3093825790923)
    4. Quiz: Between - [YouTube](https://www.youtube.com/watch?v=yBT4L_OBkHA) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3093825830923)
    5. Quiz: Reducing - [YouTube](https://www.youtube.com/watch?v=Bq9t02m2Gec) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3093825870923)
    6. Quiz: Reducer Code - [YouTube](https://www.youtube.com/watch?v=qXjmfPwuMxk) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3093825910923)
    7. Putting It All Together - [YouTube](https://www.youtube.com/watch?v=MYo8EZwDRUA) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/4163590600923)
    8. Conclusion - [YouTube](https://www.youtube.com/watch?v=CHfe_nAXJxo) or [Udacity](https://classroom.udacity.com/courses/ud617/lessons/308873796/concepts/3128965970923)

- Optional:
    + To help understand the distinction between MapReduce as a pattern and MapReduce as a framework, I recommend this (optional) video answering the question: [What is MapReduce?](https://player.oreilly.com/videos/0636920020233)
    + [Writing an Hadoop MapReduce Program in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)
    + [On procedural and declarative programming in MapReduce](http://www.unofficialgoogledatascience.com/2015/09/on-procedural-and-declarative.html)
    + [MapReduce for Statistical NLP/Machine Learning](http://www.cs.columbia.edu/~smaskey/CS6998-0412/slides/week7_statnlp_web.pdf)
    + [Data-Intensive Text Processing with MapReduce](https://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf)
