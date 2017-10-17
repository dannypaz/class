\*NIX
====

#### By the end of this article you should have:

- Completed Udacity's Linux Command Line Basics course

---

### macOS

_N.B._ macOS (formerly OS X) belongs to the BSD family of UNIX operating systems. Linux is built off of GNU which stands for "GNU's Not UNIX", which is a reverse engineered open source equivalent to UNIX. macOS is not Linux and Linux is not UNIX, but they function in many similar ways (especially when compared to operating systems like DOS and Windows). See [Unix-like](https://en.wikipedia.org/wiki/Unix-like) for more details.
![Unix Timeline](https://upload.wikimedia.org/wikipedia/commons/c/c5/Unix_timeline.en.png)

### Linux

Linux itself has many many versions (see the [List of Linux distributions](https://en.wikipedia.org/wiki/List_of_Linux_distributions) at Wikipedia) but for our purposes, we will be primarily focused on two branches of this family tree: the Red Hat branch and the Debian branch. On the Red Hat side we have centOS and Amazon's own distribution. On the Debian side, we have Ubuntu. Ubuntu has become a very popular distribution and will often be the go to version for many applications.

#### RHEL

RHEL stands for Red Hat Enterprise Linux and is behind centOS and Amazon Linux. centOS is the distribution preferred by many operations engineers because of it's commitment to stability. This commitment is so strong, however, it has prevented them from moving off of Python 2.6. Many of the Python libraries we depend on require Python 2.7 or later, so centOS is not a good choice for data science.

Amazon's version of Linux is similar to centOS. I have not been able to find it on any family tree so I don't know for sure if it is a branch of centOS or another RHEL distribution of Linux. Suffice to say, it has a lot of the advantages of other RHEL distributions but unlike centOS, it supports Python 2.7.

Many of the labs in this course have been tested using both Ubuntu and Amazon's distribution. There are advantages and disadvantages to either and it doesn't hurt to be at least a little familiar with both.

### POSIX

Arguably the most important feature of all Unix-like operating systems is their adherence to [POSIX](https://en.wikipedia.org/wiki/POSIX). This includes macOS, Ubuntu, and so on and it is why code that runs on macOS is likely (with few changes) to run on a Linux server.

Command Line Basics
----

Now, without further ado, let's dive into [Udacity's Command Line Basics Course](https://www.udacity.com/course/linux-command-line-basics--ud595).

### Cheat sheet from Week 0

Command | Explanation
--- | ---
pwd | print current working directory
ls | list the files in a directory
cp | copy a file or directory
mv | used both to move and to rename a file
mkdir | create a new directory
rm | remove a file
rmdir | remove a directory
head | display the first 10 lines in a file
tail | display the last 10 lines in a file
less | page through a file, also search
wc | count characters, words, and lines in given file
man | display manual page for given unix command
history | record of shell commands you have used
grep pattern file(s) | search files for pattern
cat | read from `stdin` and write to `stdout`
cat > file | read from `stdin`, write to file
cat >> file | read from `stdin`, *append* to file
cat < file | read from file, write to `stdout`
cat file1 file2 > file3 | concatenate file1 and file2, write to file3
sort | sort data
sort -r | sort in reverse order
cat file &#124; sort &#124; uniq | use `pipes` to sort the file then remove duplicate lines"

### Optional:

- [Week 0 Material](https://github.com/zipfian/gU-week-0-student) especially [1.2 More on Unix](https://github.com/zipfian/gU-week-0-student/blob/master/d1/6000_1.2_More_on_Unix.ipynb)
- [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)
- [The Rise of "Worse is Better"](https://www.jwz.org/doc/worse-is-better.html)
- [UNIX for Poets](http://web.stanford.edu/class/cs124/kwc-unix-for-poets.pdf)
- [The Data Scientist’s Toolbox tutorial](https://www.youtube.com/watch?v=S7AQdOdu2EI) (16 minutes)
- [Data Science at the Command Line](http://datascienceatthecommandline.com/)
- [The Cathedral and the Bazaar](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar)
