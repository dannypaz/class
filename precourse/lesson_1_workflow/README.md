Lesson 1: Tools and Workflow
===

![](http://imgs.xkcd.com/comics/tech_loops.png)

This is an introduction to the tools and workflow for the Master's Program.  Please note, there are no assignments you need to hand in for this lesson. It sets you up to complete the other lessons.

Having an effective workflow is foundational to your success at Galvanize and as a data scientist in the wild. This document will cover the  current best practices.

-----
Overview
----
1. Tools: Know the tools, use the tools, _love_ the tools
1. Interactive Development Workflow: Move Fast and Break Things
1. Errata: Other stuff to know

Tools, aka things to install
---

- [Google Chrome](https://www.google.com/chrome/browser/desktop/) is the web browser that best supports interactive features
- [Anaconda Python](http://docs.continuum.io/anaconda/install) __Python 3.5__ is the default language for GalvanizeU
- [Sublime Text 3](http://www.sublimetext.com/3) is a swiss army knife of text editors that can read all data formats and supports many 3rd party packages
- [iTerm 2](https://www.iterm2.com/) is an improved version of default Terminal.app

Interactive Development Workflow
---

Almost everyday you'll be writing programs in Python. For the Precourse you will be using [Jupyter Notebook](http://jupyter.org/) (previously called iPython Notebook). It is an interactive environment writing and running code, having a tight feedback loop between writing and running code
ensures that you catch mistakes early and get the appropriate feedback.

The ideal workflow is to write a little bit of code and then ensure that the code is doing what you expect. Plus, having a tight feedback loop is more fun.

You will be making __many__ mistakes. The faster you find broken code, the faster you will learn.

git & GitHub
--

![](http://imgs.xkcd.com/comics/git.png)

`git` is used for version control. It has a steep learning curve and will seem cryptic at times. However, it will be a critical part of your workflow. 

git is independent of GitHub. Each copy of a git repository is on personal computers (aka, local) and independent of all the others. GitHub is in the cloud (aka, remote). Since GitHub is in the cloud, anybody can access that repository at anytime, which makes it an ideal place to collaborate with other people. GitHub is the standard way to collaborate with other programmers.

Here at Galvanize, we have all of our curriculum in git repositories hosted on GitHub. You'll be viewing, cloning, and forking those repositories quite a bit.

If you are unfamiliar with git/GitHub, read more [here](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/) and then complete [git school](https://try.github.io/levels/1/challenges/1).

---
How to submit the assignments
---

You will submit your solutions with a git [pull request](https://help.github.com/articles/using-pull-requests). Here are step-by-step instructions of how to do this:

1. Fork this repository (go to [the code repository](https://github.com/zipfian/gU-precourse) and click "Fork")
1. [Install git](https://help.github.com/articles/set-up-git) on your computer if you don't already have it
1. Clone your forked repository onto your computer: `git clone https://github.com/<your username>/gU-precourse`
1. Edit the assignment files with your solutions
1. Add your changes to the repository: `git add <file you edited>`
1. Commit your changes: `git commit -m "My solutions to gU-precourse"`
1. Push your changes to your fork: `git push origin master`

A Note on Individual Style
---

We do much of [programming paired](https://en.wikipedia.org/wiki/Pair_programming), switching pairs often. Having similar work environments reduces low-level friction and allows more open space to focus on higher level learning. While you are pairing here at Galvanize, please follow the tools and workflow as they are presented here. Consider it the Galvanize Way.

When you're working solo, go ahead and do whatever you'd like. Note however that it'll be easier to get help from the faculty if you're following the Galvanize Way.

---
Recap
---
1. Install and make sure the tools are working on your computer
1. Keep a tight feedback loop when writing code
	- Write, run, repeat
 	- Jupyter Notebook running Python 3 is our preferred environment
1. Use git and GitHub
	- __A__lways __B__e __C__ommitting (ABC), aka saving your code
	- Sharing is caring so use GitHub for social coding
    
    "Test commit"
    
