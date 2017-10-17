Your Very Own Web Server
====

This lab is adapted from [Getting Started with Vagrant, SSH & Linux Server](https://gist.github.com/learncodeacademy/5f84705f2229f14d758d) only instead of [Precise Pangolin](http://releases.ubuntu.com/12.04/), we'll be using [Xenial Xerus](http://releases.ubuntu.com/16.04/) and instead of [NGINX](https://www.nginx.com/resources/wiki/) we'll be using Python's [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html).

By now you should have installed [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html). (If you haven't, do so now!)

1. Navigate to the directory where you want to host the files for your VM (_i.e._ `DSCI6007-student/Virtualization/lab/`) and run

		vagrant init ubuntu/xenial64

	to generate a Vagrantfile.

2. start and ssh into your new machine to make sure it works

		vagrant up
		vagrant ssh

	- `exit` to disconnect

3. Open the Vagrantfile and uncomment the private_network line & change to your desired IP:

    	config.vm.network "private_network", ip: "22.22.22.22"

	- Optional: make a fake domain for that ip
   		- run `sudo open /etc/hosts -a atom` to open your /etc/hosts file in Atom
    	- add this line to the end of the file and save `22.22.22.22 mytestsite.com`

4. reload and ssh into your new machine

		vagrant reload
		vagrant ssh

	One of the neat things about Vagrant is that it automatically maps the directory on the host machine where the Vagrantfile is located to the `/vagrant/` directory on the VM. So any files that are in the same directory as your Vagrantfile (including the Vagrantfile itself) should be visible if you navigate to `/vagrant/`. For example, if you run `head /vagrant/Vagrantfile` you should see something like:

		# -*- mode: ruby -*-
		# vi: set ft=ruby :

		# All Vagrant configuration is done below. The "2" in Vagrant.configure
		# configures the configuration version (we support older styles for
		# backwards compatibility). Please don't change it unless you know what
		# you're doing.
		Vagrant.configure("2") do |config|
		# The most common configuration options are documented and commented below.
		# For a complete reference, please see the online documentation at

	This will make it easy to move files in and out of your VM.

4. 	update apt-get

		sudo apt-get update

5. 	Install python packages using apt:

		sudo apt-get install python-dev python-pip

	You may also want to install `python-pandas` and `python-yaml` this way.

6. 	Install and update python packages using pip:

		pip install pandas twitter -U

7. Copy files into your `/vagrant/` directory

	1. hit `exit` to disconnect
	2. copy `index.html` and `error.html` into the same directory as your Vagrantfile

8. Test your webserver

	1. `vagrant ssh`  # SSH back into your VM
	2. `cd /vagrant`  # change directories to `/vagrant/`
	3. `python -m SimpleHTTPServer`  # defaults to port 8000

	Now, if you navigate to `22.22.22.22:8000` you should see your "Hello, World!" web page.

9. Run your webserver

	1.  If you want to run your webserver on port 80 (the default HTTP port) you may get `socket.error: [Errno 13] Permission denied`. In order to fix that, you will need to run SimpleHTTPServer with superuser privileges:

			sudo python -m SimpleHTTPServer 80

	2. If you want to run SimpleHTTPServer in the background so you can do other things, append `&` to the end:

			sudo python -m SimpleHTTPServer 80 &

	3. This will leave SimpleHTTPServer running in the background until you exit, at which point it will quit. In order to keep SimpleHTTPServer even after you exit (or "hangup", recalling ancient dialup TTY systems), prepend your command with `nohup`:

			nohup sudo python -m SimpleHTTPServer 80 &

		Note: this technique of running a command with [`nohup [COMMAND] &`](https://en.wikipedia.org/wiki/Nohup) is useful any time you want to keep a continuously running script going on a remote server. There are more advanced ways to do this, such as with [supervisord](http://supervisord.org/) but this will work in a pinch.

10. Port your code from last week's lab to generate an HTML file that will be served by SimpleHTTPServer.

	- _N.B._ You will need to copy your `api_cred.yml` file into your VM. You may use the `/vagrant/` folder to do this but it is not recommended you leave it there. In other words you should do something like this (starting in the host machine; `exit` if you are still in the VM.)
		1. `cp ~/api_cred.yml ./`  # copy credentials file to Vagrant folder
		2. `vagrant ssh`  # ssh into VM
		3. `mv /vagrant/api_cred.yml ~/`  # move credentials file to home directory

		If you then exit the VM your credentials file should no longer be in that directory (and therefore no longer in your repo).

At the end, if you navigate to `22.22.22.22/top10.html` you should see a report of the top 10 trending topics on Twitter.
