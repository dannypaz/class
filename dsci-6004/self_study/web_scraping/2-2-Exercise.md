For this exercise we will scrape reviews from Yelp.  Just like the NYT (and any large tech company really), Yelp's power comes from its data in aggregate.  They will happily give you information on one restaurant or the text of one review, but it is quite hard to get __ALL__ of the reviews for __ALL__ of the restaurants.

We will be using the Yelp [API](http://www.yelp.com/developers/documentation) and the python [wrapper](https://github.com/Yelp/yelp-api/tree/master/v2/python).  Look at the examples for how to use the wrapper in Python.

```python
# example in python

import yelp.search as yelp

key = "xxxx"
c_secret = "xxxx"
token = "xxxx"
t_secret = "xxxx"

url_params = {'term' : 'bars'}

yelp.request(params, key, c_secret, token, t_secret)
```

Before beginning, enter the following into iTerm (it's needed in search.py in the yelp folder):
  ```python
  pip install oauth2
  ```

## Part 1: Downloading

Assume we are building a restaurant recommendation engine based on user reviews (or sentiment). The first step in this process is to get data.

1. Just like with the NYT you need to register to get an API key [here](http://www.yelp.com/developers/manage_api_keys)
1. Using the [Yelp API](http://www.yelp.com/developers/documentation/v2/search_api) find all Gastropubs in SF.
2. Store these records into MongoDB.
3. How many Gastropubs are there in SF?

## Part 2: Parsing

For the second part we will __PARSE__ reviews from Yelp.  Once we have the textual content of the reviews we can do interesting NLP on them such as classifying the cuisine of the restaurant, determining the sentiment of the review, or [aspect based summarization](http://www.ryanmcd.com/papers/local_service_summ.pdf) of reviews.

> To avoid getting the Galvanize IP blocked by Yelp I have downloaded the relevant HTML pages in the `html` folder

2. For each Restaurant count how many 5 star reviews it has gotten.
  
  Going one step further we will parse the textual content of each review.  

3. Parse each review and create a dictionary mapping a username to the text of the review they gave.
3. How would you get the metadata on __EVERY__ restaurant on Yelp in SF?  And get around their limits? (Don't do this because we may get our IP blocked 0_o)

### Part 3: Crawling

Again, to avoid getting blocked by Yelp we will crawl Wikipedia instead.  What distinguishes "crawling" from just downloading and parse web pages is typically the following of additional links.  For example we often want to:

1. Download a page
2. Find all the relevant links on that page
3. Download each of the relevant links
4. Rinse and Repeat

--

For this we will work with a safer web domain (Wikipedia) to get practice traversing links.

1. Retrieve and store every article within 1 hop from the 'Zipf's law' article.
  <b style="color: red">Do not follow external links, only linked Wikipedia
articles</b>

  ___HINT: The Zipf's Law article should be located at: 'http://en.wikipedia.org/w
/api.php?action=parse&format=json&page=Zipf's%20law'___

 We will get some practice now with regular expressions in order to search the content of the articles for the terms `Zipf` or `Zipfian`.  We only want articles that mention these terms in the displayed text however, so we must first remove all the unnecessary HTML tags and only keep what is in between the relevant tags.  Beautiful Soup makes this almost trivial.  Explore the documentation to find how to do this effortlessly: [http://www.crummy.com/software/BeautifulSoup/bs4/doc/](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

2. Find all articles that mention 'Zipf' or 'Zipfian' (case
insensitive) in the text of the article.
 * Test out your Regular Expressions __before__ you run them over __every__document you have in your database: [http://pythex.org/](http://pythex.org/). Here is some useful documentation on regular expressions in Python: [http://docs .python.org/2/howto/regex.html](http://docs.python.org/2/howto/regex.html)

 ___HINT: There should be ~10 articles___

3. Once you have identified the relevant articles, save them to a file for now, we do not need to persist them in the database.

## Fin

Congratulations!  You have successful acquired interesting text content from the Internet.  Now we can do all sorts of interesting analysis on this content or you can grab the text content of your favorite website :)


