Move your Linux machine to the Cloud
====

Part 1: Set up an EC2 key pair
----------------------

To connect to an Amazon EC2 instances, you need to create an **SSH key pair**.

- After setting up your account, go to the <https://console.aws.amazon.com/ec2>

- Choose **N.Virginia** as your region. Do not use a different region.
  *N. Virginia* is the default. Using a different region will require
  configuration to work correctly.

  ![image](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/region.png)

- On the left click **Key Pair** and then **Create Key Pair**

  ![image](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/keypair.png)

- Download and save the `.pem` private key file to a new folder `.ssh`
  in your home directory. Any folder that starts with a `.` will be
  hidden in the folder. In this case, you want to hide the sensitive
  information.

- This file contains the private key identifying your SSH client and so
  needs to be protected from snooping.

  Change the permissions of the file using this command:

  ```
  $ chmod 600 </path/to/saved/keypair/file.pem>
  ```

  These new permissions ensure that only the file's owner will be able to
  read or write the file.
  
Part 2: EC2 on AWS
------------------

EC2 is a remote virtual machine that runs programs much like your
local machine. Here you will learn how to run tasks on an EC2 machine.

- Launch an Ubuntu Server. Choose an instance that is free tier eligible (_i.e._ `t2.micro`). Remember to pick a keypair for which you have the `.pem` file.

- Log into the instance you have launched using `ssh`. The user name
  is `ubuntu`. Replace `KEY-PAIR` and `EC2-INSTANCE` with
  the appropriate values.  The latter is the instance's public DNS name.

        ssh -i ~/.ssh/KEY-PAIR.pem ubuntu@EC2-INSTANCE.amazonaws.com

- Remember to change the permissions on your `.pem` file if you have
  not already. `chmod 600 KEY-PAIR.pem`

- Follow the same steps you took to set up your Ubuntu box in the [Virtualization lab](../Virtualization/lab.md) (steps 4 through 6) only this time do so on this EC2 instance. 
	1. update apt-get
	2. install python packages using apt
	3. install and update python packages using pip

- Use `scp` to copy files into your EC2 machine

- Run your webserver on port 80. There are two things you must keep in mind when it comes to accessing your webserver.
	- The URL or IP address - When you created a webserver in a VM, the VM lived at a locally accessible IP address: 22.22.22.22. (If you completed the optional step, this IP address would have been mapped to the URL mytestsite.com/.) The URL for your EC2 instance will be given after you launch it. It will look something like ec2-XXX-XXX-XXX-XXX.compute-1.amazonaws.com where XXX-XXX-XXX-XXX is the public IP address of the EC2 instance. 
	- The port number - Every standard transfer protocol has a default port number associated with it. For HTTP, that default is 80. As we discussed in the [Virtualization lab](Virtualization/lab.md), the default port used by SimpleHTTPServer is 8000. This is to make sure it doesn't collide with an already running HTTP server. However, for our purposes, SimpleHTTPServer will be our HTTP server so, as before, we will want to tell SimpleHTTPServer to run on port 80 (and not the default port 8000). This is easily done by simply appending the number 80 to the call (_i.e._ `python -m SimpleHTTPServer 80` instead of `python -m SimpleHTTPServer`). As before, you will want to run it with `nohup` and `&` to make sure it doesn't die when you exit.

- You'll notice that even though you have a web server running, you still cannot access it from your laptop. That is because AWS has helpfully blocked that port for you. In order to fix it, you must change the
  **Security Settings** to enable the inbound requests to be made.

- Click on the Security Group for your instance.

  ![Security Groups](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/ec2-security-groups.png)
  

- In the Security Group, select **Inbound**, then **Edit**, and then
  **Add Rule**:
  	- Type: HTTP
  	- Protocol: TCP
  	- Port Range: 80 (the default for HTTP)
  	- Source: Anywhere (0.0.0.0/0)

- Save the rule.

Part 3: cron on AWS
------------------

Set up a cron job to refresh the web page with new data every minute.

Once you are sure that's working, edit the crontab to run every hour.

Part 4: Use cron to email report
-----

- `sudo apt install mailutils` 
	- When it asks, choose to configure as an "Internet Site". If you make a mistake here, you can go back and fix it with `sudo dpkg-reconfigure postfix`
- Use Python's [smtplib](https://docs.python.org/2/library/email-examples.html) module to send your report to me at [alessandro+homework@galvanize.com](mailto:alessandro+homework@galvanize.com) from `student.[your last name]@galvanize.it` with the subject "Twitter Trends".
	- Gmail will recognize that your messages aren't actually coming from Galvanize, so it will send them to the spam folder. Keep this in mind when testing. (It may actually be working though you may not see the result if you don't look in Spam.)

Part 5: (optional) Vagrant to deploy to AWS
----

Wouldn't it have been easier to just use the VM you already configured and deploy that directly to AWS? If you think so, install [vagrant-aws](https://github.com/mitchellh/vagrant-aws) and proceed accordingly.
