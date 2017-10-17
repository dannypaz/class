Conencting to the Cloud with Python
===

Part 1: Create a Conda Environment
-----------

Follow the instructions to [create an environment](http://conda.pydata.org/docs/using/envs.html#create-an-environment) to create a conda environment called `dsci6007` for this class using Python 2. Install `boto` and `awscli`. You will probably also want to install `jupyter` and `pandas` while you're at it. For the rest of this course, it will be assumed that you are in the dsci6007 envirnoment unless otherwise specified. 

Note on boto vs. boto3: boto3 is a relatively new Python library that may someday replace boto. It brings you closer to the underlying API, but it is not as easy to use and doesn't have as good documentation (yet). You can complete this and future labs with either library, though it is recommended that you stick with boto for now.

Part 2: Create an IAM User
----------------------

Follow the instructions for [Creating IAM Users](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) summarized here:

1. Sign in to the Identity and Access Management (IAM) console at [console.aws.amazon.com/iam](https://console.aws.amazon.com/iam/)
2. In the navigation pane, choose **Users** and then choose **Add user**.
3. Type the user name for the new user. This is the sign-in name for AWS.
4. Select both **Programmatic access** and **AWS Management Console access**
5. Choose **Next: Permissions**.
6. On the **Set permissions page**, specify how you want to assign permissions to this set of new users. Choose **Attach existing policies to user directly** to select from existing managed policies. IAM displays a list of currently defined managed policies, both AWS- and customer-defined. Select **AdministratorAccess**
7. Choose **Next: Review** to see all of the choices you made up to this point. When you are ready to proceed, choose **Create user**.
8. To view the users' access keys (access key IDs and secret access keys), choose **Show** next to each password and secret access key that you want to see. To save the access keys, choose **Download .csv** and then save the file to a safe location. You will use these in the next step.

Part 3: Configure AWS CLI
------
Today's lab involves creating a Python client to connect to AWS. This client must be authenticated with a user's access key and secret. You may specify this in your code but please don't include them when you submit your lab. These are, after all, the key and secret for your AWS account! 

Instead, run `aws configure` and fill out the AWS Access Key ID and Secret Access Key with the access keys you downloaded in the last step above.

Part 4: S3 on AWS
-----------------

S3 is the storage system on AWS. Next you will practice interacting with it through the Amazon GUI and with the Python library `boto`.

- **The bucket name must be:** (1) Unique (no one has ever used it).
  Prefix it with a unique id. (2) Lowercase. (3) Must not have
  underscore.

- Download the Shakespeare sonnets file if needed

  curl -o shakespeare-sonnets.txt http://www.gutenberg.org/cache/epub/1041/pg1041.txt

- Upload (using the GUI) `shakespeare-sonnets.txt` to your bucket.

  ![image](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/s3-upload.png)

- Note the link to the file.

  ![image](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/s3-file-link.png)

Part 5: Writing to S3 using Python
----

You should know how to read and write files to S3 using a Python script at the end of this exercise.

- Write a program that reads the file from S3 using boto.

- Calculate the frequencies of all the words in the file.

- Word frequencies are frequently used to group similar documents
  together. For example, news stories about the same subject will tend
  to have similar word frequencies.

- Sort the words in descending order of frequency.

- Print out the 20 most frequently used words and their frequencies.

- Upload the calculated and sorted frequencies for all the words to
  S3.
  
- Hints: 
	- there exists in the [`collections`](https://docs.python.org/2/library/collections.html) module a class that may be useful to you
	- Pandas' `DataFrame` class has various `.to_` methods that may be helpful in constructing a string or file which you can use to set the contents of your S3 key.

Part 6: Create a website on S3
----

S3 is a convenient way to host a static website very cheaply. The URL is a bit clumsy, though that can be remedied using Route 53 (see below). 

- Follow the first three steps on [Hosting a Static Website on Amazon Web Services](http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html) to turn your bucket into a website.

Stretch Goal: Route 53
----
Though beyond the scope of this course, you now know enough to maintain a static website. If you wish to do so but don't like the idea of having `s3-website-us-east-1.amazonaws.com` in the URL, take a look at [Route 53](https://console.aws.amazon.com/route53/home). 
