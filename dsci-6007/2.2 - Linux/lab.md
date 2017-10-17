Linux Intro
===========

Objectives
----------

By the end of this morning, you will be able to:

- Examine log files using `head` and `vi`

- Create a `pipe` for inter-process communication

- Find patterns using `grep`

- `cut` out selected portions of each line of a file

- `sort` lines of text files

- report or filter out repeated lines in a file using `uniq`

Before you start
----------------

- Using `export LC_CTYPE=C` to set the locale to the default locale
  instead of ASCII.  Setting this prevents warnings such as `Illegal byte sequence`
  when using commands like `rev` and `tr`.

- Always be thinking of the order in which you process data.  It is helpful to filter
  early to reduce the amount of data processed later in the pipeline.

- Use "head -n" if you would like to create a subset of the data to use until you get
  your pipeline working properly.

- History files (e.g, .bash_history) are common in UNIX and are usually stored in your
  home directory.  You already saw them for Postgres and will see that for other utility
  program which we will use in the future.

- Older UNIX programs typically only used command-line switches of a single character
  (e.g., "-h").  Programs created by GNU have added the ability to use long options such
  as --help.  When writing command-line data pipelines consider using the long options to
  improve readability.

Unix Shell Walk-through
----------------------

#### Retrieve some data

    wget https://s3-us-west-2.amazonaws.com/dsci/6007/data/shakespeare-sonnets.txt

#### What is in `shakespeare-sonnets.txt`?

    head shakespeare-sonnets.txt

#### Let's skip the first two lines:

    tail -n +3 shakespeare-sonnets.txt |  # Start from line 3
        head                              # Show top 10 lines


#### Let's translate the characters to lower case:

    tail -n +3 shakespeare-sonnets.txt | tr 'A-Z' 'a-z' | head

#### Let's tokenize our words:

    tail -n +3 shakespeare-sonnets.txt |
        tr 'A-Z' 'a-z' |
        tr -sc 'a-z' '\012' |
        head

#### Let's sort them:

    tail -n +3 shakespeare-sonnets.txt |
        tr 'A-Z' 'a-z' |
        tr -sc 'a-z' '\012' |
        sort |
        head

#### What is our vocabulary?

    tail -n +3 shakespeare-sonnets.txt |
        tr 'A-Z' 'a-z' |
        tr -sc 'a-z' '\012' |
        sort |
        uniq |
        head

Question: Is this the optimal order for the pipeline?  Would it be better to first use 'uniq' and then 'sort'?

#### How big is our vocabulary?

    tail -n +3 shakespeare-sonnets.txt |
        tr 'A-Z' 'a-z' |
        tr -sc 'a-z' '\012' |
        sort |
        uniq |
        wc -w

#### How many times does each word occur?

    tail -n +3 shakespeare-sonnets.txt |
        tr 'A-Z' 'a-z' | tr -sc 'a-z' '\012' |
        sort | uniq -c | head

#### How might we construct a rhyming dictionary?

    # Sort so that all words that end the same way are close together.
    tail -n +3 shakespeare-sonnets.txt |
        tr 'A-Z' 'a-z' | tr -sc 'a-z' '\012' |
        sort | uniq | rev | sort | rev | head

#### What was the first word of each sentence?

    tail -n +3 shakespeare-sonnets.txt |
        awk '{print $1}' |
        head

#### What's the word count of those words?

    tail -n +3 shakespeare-sonnets.txt |
        awk '{print $1}' |
        sort |
        uniq -c |
        head

#### Let's delete punctuation:

    tail -n +3 shakespeare-sonnets.txt |
        awk '{print $1}' |
        sort |
        tr -d '[:punct:]' |
        uniq -c |
        head

Parsing Web Log Files
---------------------

1. Download this data file <http://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz>
The file is a web server log file.  These types of logs are frequently analyzed in
data pipelines.  This log appears to be using the Apache "access" log file format.
If you are curious about the meaning of the various fields you can find out more
about this very common format from: http://httpd.apache.org/docs/2.4/logs.html

2. Using `-c` in `gunzip -c FILE.gz` streams the uncompressed file
without saving it to disk. Use this to look at the
`NASA_access_log_Jul95.gz` file.

3. Find the total number lines in the files.

4. You will notice that (most of) the lines in the log file have ten fields.  The ninth
field is an HTTP status code.  See https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
for an explanation of the meanings of the values of the codes.  Values in the 400-499 range
are for client errors.

Using `gunzip -c` how can you find the total number of lines
containing client errors? These are ALL status codes in the range 400-499.

Note that, although most of the log file lines are in the correct format and have ten fields,
some have only eight or nine fields.  Even for these the status code is always the next to
the last field.  Account for that in your command-line data pipeline.

5. Find the total number of server errors in the file. This means that you will be
including status codes in the range from 500-599.

6. Find the total count of all the different status codes in the
`NASA_access_log_Jul95.gz` file.
