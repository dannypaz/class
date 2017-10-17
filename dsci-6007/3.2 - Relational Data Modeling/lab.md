Data Modeling Practice
----------------------

In this exercise, you will demonstrate your understanding of normalization by designing a data model. By now you should have a collection of tweets stored as Json in your Postgres database. Start by creating a new table for tweets using the tweet id as your primary key. Other data that are atomic and functionally dependent on the tweet id should be included such as the `text`, `favorite_count`, `retweet_count`, _etc._ Considering that the Json type is itself a violation of 3NF, think about how you might want to handle keys like `user` and `entities`. What is the relationship between a tweet and a user (one-to-one, one-to-many, many-to-many)? Similarly, what is the relationship between tweets and entities?

1. Design a simple data model involving tweets, users, and entities. How many tables do you need? 2? 3? 4? What is the relationship between them? What are the primary keys and foreign keys? Draw this out. You may use an [ER](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) diagram, [UML](http://www.agiledata.org/essays/umlDataModelingProfile.html), or something of your own design, so long as it is easy to read and understand. You may use [Graphviz](http://www.graphviz.org/) or pen and paper or a tool like [Gliffy](https://www.gliffy.com/).

2. [`CREATE MATERIALIZED VIEW`](https://www.postgresql.org/docs/current/static/sql-creatematerializedview.html)s off of your raw twitter data to generate this data model.

3. Create a (normal) view that counts the frequency of hashtags in your data in descending order.

4. Optional: Create a second EC2 instance that will serve as your reporting web server (if you haven't already) and use it to generate an HTML table representing the top 10 hashtags used in your database.
