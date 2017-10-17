Virtualization
====

#### By the end of this article you should have:

- Watched:
    - Virtualization Overview
    - Server Virtualization
    - Vagrant Tutorial
- Downloaded and installed:
	- 	VirtualBox
	-  Vagrant

---

In this lesson you will learn more about virtual machines (VMs). We touched on this a bit in [the first lesson](../Course Overview/README.md) but now you will learn how to host a VM on your own laptop.  

Begin by watching this [Virtualization Overview](https://www.youtube.com/watch?v=CC2qSfZTwCY). By the end of it, you should be able to distinguish and describe the relationship between logical address space and physical address space. The term "logical" is a term of art in computing and you may hear it a lot to distinguish between soft resources and hard (or physical) resources. For example, if you have "partitioned" your hard disk, that means you have multiple "logical" disks mapped onto one "physical" disk.

Next follow up with this introduction to [Server Virtualization](https://www.youtube.com/watch?v=rivJYVPP76I). By the end of this video, you should be able to describe what a hypervisor does. Between the two videos, you should be able to list at least two advantages and at least one disadvantage of virtualization.

Now, download and install the latest versions of [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html). (Make sure that VirtualBox has finished installing before you install Vagrant.) It is important that both of these applications be downloaded and installed _before_ class.

Finally, watch the [Vagrant Tutorial - Running a VM For Your Local Development Environment](https://www.youtube.com/watch?v=PmOMc4zfCSw). You do not need to follow along with this tutorial as we will be doing something similar for the first part of our [lab](lab.md). However, you should watch it before class. By the end of it, you should be able to answer the question: "What should you always do when you spin up a new VM?"

Before coming to class run `vagrant box add ubuntu/xenial64` from the command line. This will download the image for the VM we will use in class. It's a largish file, so it's best to do this on your own ahead of time rather than having everyone try to download it at once in class.

---

#### On completing this article, you should have:

- Watched three videos about virtualization
- Downloaded and installed VirtualBox and Vagrant
- Downloaded the `ubuntu/xenial64` vagrant box image
