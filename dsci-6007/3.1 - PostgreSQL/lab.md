RDS
----

In today's lab, we will migrate from MongoDB to PostgreSQL and from hosting a database on the same instance as our application server to hosting it separately using Amazon RDS. These two changes are each important in their own right.

### All your eggs in one basket

To begin with, let's log back into that EC2 instance you left running over the weekend. You should have left it with a script running that inserts tweets into your database. SSH into that instance now and use [ps](http://linuxcommand.org/man_pages/ps1.html) to check to see if it's still running (_i.e._ `ps aux | grep python`). You may find that your process is no longer running. What happened? If you used `nohup` to leave it running, it should have sent output (including error messages) to `nohup.out`. So let's take a look at the tail of that file to see what happened (`tail nohup.out`). You may find that the connection to Mongo was closed. Why? Spend a few minutes with your partner to figure out what happened. (If your system is still up and running, great. Find someone's that crashed and work with them.)

---

You may have discovered that your system crashed because your database ran out of space. We intentionally picked a very small instance. An easy solution would be to pick a larger instance but eventually you'll get to a point where Amazon doesn't offer an instance big enough to store all that data.

Another problem is that because we were using one instance for everything, when one application goes down, it's possible that it will take the rest of the system down with it. This also makes debugging difficult. In a system as simple as ours, it's easy to tell that the problem was with MongoDB running out of space, but in a more complex architecture, that may not be so obvious. The solution is to partition our architecture so that each instance does only one thing. To that end, we will now want 3 instances:

- One EC2 instance to pull data from the Twitter Firehose and insert it into our database
- One RDS instance to host our database
- Another EC2 instance to pull data from our database and present it to the user

Note that one of the effects of partitioning our architecture in this way means that our software dependencies are also isolated. Our first EC2 instance needs to have Python Twitter Tools installed, but our second does not. If, at a later date, we wanted to use a more sophisticated web server, we could make that change without affecting our Twitter Firehose.

At this point, you can stop your (possibly now broken) EC2 instance. We will spin up two new ones after we've launched our new database management system (DBMS).

### New feature in Postgres 9.2: Mongo

Ever since version 9.2, PostgreSQL has supported the JSON datatype. This gives us the flexibility of storing the semistructured data that we enjoy in MongoDB without having to give up the functionality of Postgres and the relational data model in general.

#### Getting Started with Amazon RDS

For today's lab, start by [Creating a PostgreSQL DB Instance and Connecting to a Database on a PostgreSQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html). (To stay on the [free tier](https://aws.amazon.com/rds/free/), you'll want to do a Single-AZ deployment on a db.t2.micro instance with no more than 20 GB storage.)

**Important:** Be sure to use Postgres 9.6 or later. (At the time of this writing, RDS still defaults to 9.5, though 9.6 is available.)

Note: the screenshots under [Using pgAdmin to Connect to a PostgreSQL DB Instance](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html#CHAP_GettingStarted.Connecting.PostgreSQL) are still based on pgAdmin 3. We will be using pgAdmin 4 which is slightly different but should follow the same principles.

#### DDL

There are two parts of the Structured Query Language: the data definition language (DDL) and the data manipulation language (DML). Most of the time we are focused on the DML which provides us with the CRUD operations: INSERT, SELECT, UPDATE, DELETE, before we do any of that, we need a data model to manipulate. MongoDB lets us off easy by not requiring any DDL statements. You refer to a collection and if it doesn't already exist, MongoDB automagically creates it for you. (This can lead to a proliferation of orphan collections due to typos.) Postgres and other RDBMSs require you to CREATE your tables before you put anything into them. For today's lab, we will keep it simple. You need only [CREATE](https://www.postgresql.org/docs/current/static/sql-createtable.html) a table with a single column of the [JSON](https://www.postgresql.org/docs/current/static/datatype-json.html) datatype. Later we will work on normalizing this data to make it more useful for Online Analytical Processing (OLAP).

To do this using [pgAdmin](https://www.pgadmin.org/docs4/1.x/index.html):

1. Connect to your RDBMS. The easiest way to do this is to click "Add New Server" under "Quick Links".
    1. Name it whatever you want (I pick the same name I used in AWS for simplicity).
    2. Go to the "Connection" tab
    3. Enter the Host address. This is the URL provided by AWS which should be [your database name].[some hash].[your region (_i.e._`us-east-1`)].`rds.amazonaws.com`. This appears as your "endpoint" (not including `:5432`) in your RDS configuration detailed-schedule
    4. Leave the port (5432) and maintenance database (postgres) alone
    5. Fill in the user name and password you specified when launching your database. You may (if you wish) save your password.
    6. You may ignore Role and SSL mode for now.
    7. Save.
2. Create your table
    - You'll now see your RDS server on the left under Servers. Expand it.
        - You'll now see Databases, Login/Group Roles, and Tablespaces under your server. Click "Databases"
            - You'll now see your database along with "postgres" under Databases. Ignore "postgres" (that is the maintenance database) and click on the one you created in AWS.
                - You'll now see Casts, Catalogs, Event Triggers, Extensions, Foreign Data Wrappers, Languages, and Schemas. These are all advanced topics to be covered on your own at a later date. For now, click "Schemas"
                    - For now, there should just be one Schema: "public". Expand it.
                        - Now we have Collations, Domains, _etc. &c._
                        - Right click on "Tables" and select Create -> Table...
                            1. Name your table `raw_tweets`
                            2. Leave Owner, Schema, and Tablespace default and go to the "Columns" tab
                            3. Hit the "+" on the right to create a new column
                                1. Name: `status`
                                2. Data type: `json`
                                3. Length and Precision do not apply to `json` data
                                4. For now, go with the default and allow NULL and do not set a primary key. We will fix this when we normalize our data tomorrow.        

### Pipeline

Once your database has been created and your data model defined, you will need to populate your database. You can start with the code you used to populate MongoDB. There are a few things to watch out for when connecting to RDS.

1. Don't forget to put all your credentials in your `api_cred.yml` file (and not in your code).
2. By now you might have noticed that many of the objects we receive from the Twitter firehose are not actually tweets but deletions. We don't need those. Filter those out before inserting them into RDS.
3. In order to convert from a Python dict to a Postgres Json datatype, you will want to import the Json class from `psycopg2.extras`.
4. The [`execute`](http://initd.org/psycopg/docs/cursor.html#cursor.execute) method expects a tuple or list.
5. Don't forget to [`commit`](http://initd.org/psycopg/docs/connection.html#connection.commit) your transaction after your insert. You may commit after every insert or, to save time, you may want to commit after every 100 or so inserts.

**Optional:** This time, try making this instance using the [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/) instead of Ubuntu. Of course, your user name will not be `ubuntu` this time, but `ec2-user`. The next thing you will notice is that you will be using [yum](https://en.wikipedia.org/wiki/Yellowdog_Updater,_Modified) instead of [apt](https://en.wikipedia.org/wiki/Advanced_Packaging_Tool) to install Linux packages. Just as before, you will want to start by updating everything (`sudo yum update` instead of `sudo apt-get update`). Unlike Ubuntu, you may need to install `gcc-c++` in order for some python packages to work. Some packages may also have slightly different names (_e.g._ `python27-psycopg2` instead of `python-psycopg2`). Of course, you can always `search` for packages just as you could with `apt` (_e.g._ `yum search python postgres`)

**N.B.:** You may find that RDS will not accept a connection from your EC2 instance (even though it may from your laptop). This is because RDS automatically allows connections from the IP address that created it (_i.e._ your laptop) but no where else. By now you should know how to fix this. The important thing is to change the inbound rules on the security group for your RDS instance to allow the source to be anywhere (or, if you want to be more restrictive, you can set it to just the security group you are using for your EC2 instance).

### Querying

Now that you have data streaming into your database, trying querying it. Take a look at the [PostgreSQL JSON Tutorial](http://www.postgresqltutorial.com/postgresql-json/) to see how. Start by selecting out the text of each tweet and see if you can work up to being able to select out the hashtags. _Hint_: The [`json_array_elements`](https://www.postgresql.org/docs/current/static/functions-json.html) function may come in handy.
