Welcome to Data Engineering!
===

#### By the end of this article you should have:

- Watched:
    - What Is The Cloud?
    - Cloud Computing Basics
    - Creating An AWS Account - Part 1
    - Creating An AWS Account - Part 2
- Read (in addition to this article):
    - Create Virtual Environments for Python with Conda
- Completed:
    - Setting up AWS account
    - Activated your AWS activate free credit
    - Obtained a consumer key, consumer secret, access token, and access token secret from Twitter

---

Before we begin, there are a few things you need to do before the first day of class. You will need to set up your Amazon Web Services (AWS) and Twitter App accounts.

[Set up AWS](https://aws.amazon.com/)
---

By the end of this, you should have an AWS account up and running and 1,000 free credit.

Amazon Web Services, or AWS, is the cloud computing service we will be using in this course. Many startups and other tech companies (including most of your practicum sites) use AWS. To find out more about what this thing called "the cloud" is, and more about AWS in particular, start by watching:

- [What Is The Cloud?](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awscloud-demo/0101.mp4) - ([Prezi](https://prezi.com/h-yzlfktxo3y/is_0101/))
- [Cloud Computing Basics](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awsintro-demo/0101.mp4)

In this course we will be needing a lot of AWS. Following the instructions below to set up your account and claim the free credit that is available to you. By the end of watching those videos, you should be able to exlain what is the value of using AWS and roughly how it works.

### Step 1: Create an AWS account

1. Watch [Creating An AWS Account - Part 1](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awsintro-demo/0104.mp4).  
This videos walk you through the actual process of setting up an AWS account as well the importance of setting up Identity & Access Management (IAM) accounts within that. For now, you only need to do the first part in order to proceed with the next step (that is, getting your Activate credit). You might also find reading [EC2 for Poets](http://ec2.forpoets.org/) helpful.

2. Go to [http://aws.amazon.com/](http://aws.amazon.com/) and sign up:

	- You may sign in using your existing Amazon account or you can create a new account by selecting **Create a free account** using the button at the right, then selecting **I am a new user**.

	- Enter your contact information and confirm your acceptance of the AWS Customer Agreement.

	- Once you have created an Amazon Web Services Account, you may need to accept a telephone call to verify your identity. Some people have used Google Voice successfully if you don't have or don't want to
	  give a mobile number.

	- Once you have an account, go to
	  [http://aws.amazon.com/](http://aws.amazon.com/) and sign in. For now, you will work primarily from the Amazon Management Console.

### Step 2: Activate your AWS free credit

As a Galvanize member, you are entitled to free AWS credits. Follow the steps below to activate your credits. They will come in about two weeks.

Go to [aws.amazon.com/activate/portfolio-signup](https://aws.amazon.com/activate/portfolio-signup/) and fill in
your details. Some details you will need:

- Organization ID (case­sensitive): 19tPn
- If it asks for Start Date, put 1/19/2017 (the first day of class)
- Make sure you enter Organization ID (and Start Date, if needed) as specified. Otherwise your application might get rejected.
- To see your credit balance, applicable services, and expiration date, go to Account > Billing & Cost Management > Credits
- You will be eligible for:
	- \$1,000 in AWS Promotional Credit valid for 1 year.
	- 2 months of AWS Business Support.
	- Access to the AWS Technical and Business Essentials web­based (or instructor­-led) training (\$600 value per course).
	- 80 credits for Self­Paced Labs (\$80 value).
	- Access to 1:1 Virtual Office Hours with AWS Solutions Architects

**If you cannot sign up please let the instructors know.**

After you've created your AWS account and registered it using Galvanize's Activate Portfolio, watch [Creating An AWS Account - Part 2](http://infiniteskills.bc.cdn.bitgravity.com/iskills-media/awsintro-demo/0105.mp4). This will prepare you for the [lab](lab.md) on the first day of class.

[Create a Twitter App](https://apps.twitter.com/)
---

If you do not already have a Twitter account, create one now at [twitter.com/signup](https://twitter.com/signup)

Go to [apps.twitter.com/app/new](https://apps.twitter.com/app/new) and create an "application". Some notes:  

- The name of your app doesn't matter, but it must be unique
- The website URL doesn't matter either, though it must be valid

We will not be using this until day 2, but since it sometimes takes time for the app to be approved, you will want to do this ahead of time.

[Conda Environments](http://conda.pydata.org/docs/using/envs.html#create-an-environment)
---

For this course, we will need to create a new conda environment. Conda environments are an extension of virtual environments (not to be confused with virtual *machines* which we will discuss separately in this course). Virtual environments allow you to specify which packages and which versions you will use for your application (for example, Python 2 instead of Python 3, and boto3 but not scikit-learn). This is useful both for avoiding version conflicts and for help in deploying code as you more easily make sure that your environment matches that on the machine to which you will be deploying.

Setting this up and installing the necessary packages will be the first part of our first [lab](lab.md) assignment. Before we begin, you will want to read how to [create virtual environments for python with conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/).

---

#### On completing this article, you should have:

- Watched 4 videos about AWS
- Read one blog article about conda environments
- Created an AWS account
- Received \$1000 in promotional AWS credit
- Created an account for a Twitter "app"

Finally, here are some resources about data engineering in general to whet your appetite for what's to come.  
(_These are optional._)  

- Watch: [Bridging the Gap Between Data Science and Data Engineering](https://www.youtube.com/watch?v=EtYv7zPyS2A)
- Read: [What’s the Difference Between Data Engineering and Data Science?](http://www.galvanize.com/blog/difference-between-data-engineering-and-data-science/)
- Read: [Data Scientist, Data Engineers, & Infrastructure Engineers](http://multithreaded.stitchfix.com/blog/2016/03/16/engineers-shouldnt-write-etl/)
- Watch: [Data Engineering @ Slack](https://drive.google.com/file/d/0BxGB59WxQI5oTXpQd09jbVpvalE/view)  
