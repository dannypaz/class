Generating Reports
====
Our first report will be a simple one: what are the top 10 trending topics on Twitter today or T6. 

**Don't forget:**

	$ source activate dsci6007

Part 1: Of Consumer Keys and Access Tokens
----

Before you begin, you will need your consumer key, consumer secret, access token, and access token secret. This was generated when you created your Twitter "app" at [apps.twitter.com](https://apps.twitter.com/). You will not want to store this in your code directly, as that is a security risk. Instead, put it in a YAML file outside of your git repo (replacing the strings as appropriate):

```yaml
twitter:
    consumer_key: MY_CONSUMER_KEY
    consumer_secret: MY_CONSUMER_SCRET
    token: MY_ACCESS_TOKEN
    token_secret: MY_ACCESS_TOKEN_SECRET
```

You can then load your credentials into a Python dictionary thus:

```python
import os
import yaml
credentials = yaml.load(open(os.path.expanduser('~/api_cred.yml')))
```

Your Twitter credentials would then be nested under `'twitter'` so, for example, you could get your `consumer_key` with `credentials['twitter'].get('consumer_key')`

Part 2: Accessing the Twitter API in Python
----

There are about [a dozen Python libraries](https://dev.twitter.com/resources/twitter-libraries) for accessing the Twitter API. I like [Python Twitter Tools](https://github.com/sixohsix/twitter) which can easily be installed with `pip install twitter`. Which ever one you use, you will need to then use your credentials to authenticate with the Twitter API and then you are off to the races. 

Consult the [Twitter Developer Documentation](https://dev.twitter.com/rest/public) to find out how to get the top 10 trending topics for a specific place. (You may need to search a little.) Depending on the Python library you use, this feature may be built in as a specific method in an object you instantiate, or you may simply specify the endpoint and provide the parameters. Either way, you will be using Twitter's REST API (more or less directly) so it will behoove you to know how the REST API works.

Part 3: Generating the Report
----

You are limited only by your creativity in how you want to generate this report in the form of a HTML page named `top10.html`. The only constraint is that it be in the form of a static web page. The simplest thing would probably be to load the data into a pandas DataFrame and call the `.to_html()` method. This main downside to this is that it makes your script dependent upon pandas. When we deploy your script to EC2, this will slow you down as pandas has a lot of dependencies. 

On the other hand, if you want to be more fancy (and don't mind a lot of dependencies) you might try generating a bar plot or some other visualization (a word cloud, perhaps?). You could either output this to SVG and embed it in your HTML or you could output it as an image file and reference it using the HTML `IMG` tag.

Part 4: Publishing the Report
----
Use boto or boto3 to publish your HTML to the website bucket you created yesterday. Mitch Garnaat's [s3_website.py](https://gist.github.com/garnaat/833135) gist may provide a helpful template of how to do this.

Part 5: Bundling it up into a script
----

If you are like me, perhaps you have been working entirely in Jupyter up to this point. If so, that's okay, but now you need to move your code into an executable Python script. An easy way to get this process started is go to File > Download as > Python (.py). This will produce a Python script that may be executable off the bat. You will probably want to clean it up however, and put `#!/usr/bin/env python` at the top so the shell knows how to execute it. (See Wikipedia's article on [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) for details on how that works.)

Part 6: OPTIONAL - Creating a Web App (Advanced)
----
If you want to take this a step further, install [Flask](http://flask.pocoo.org/) and try creating a web app that serves this page and refreshes it each time you load it. In other words, your web app should poll Twitter for trending topics each time the page is loaded and thus keep it constantly up to date, rather than always being as old as the last time you ran the script.