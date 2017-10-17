How the Internet Works
----

#### By the end of this article you should have:

- Watched:
    - How the Internet Works in 5 Minutes
    - REST API concepts and examples
- Read:
    - Intro to HTML
    - What's HTTP?
    - Configure a Bucket for Website Hosting
- Completed:
    - creating a static web page
    - issued a GET request

---

In today's lesson we will

- get data from the Internet using HTTP
- cover just enough HTML to be dangerous
- create a simple report on the web

1. Begin by reading this article on [HTML](HTML/README.md).  
HTML can get pretty complicated, especially when you include things like CSS and JavaScript, but for now we will focus on just enough to create the simplest of web pages for reporting statistics.  
<small>(Note that this article, and the one below on HTTP, are both borrowed from our Web Development Immersive course. You are only expected to read the README files in each, though supplementary material has been included for your benefit. The supplementary material may include broken links, or links to resources you don't have access to. If such is the case, let us know and we will get you the resource for which you are looking.)</small>
2. Watch [How the Internet Works in 5 Minutes](https://www.youtube.com/watch?v=7_LPdttKXPc).
After watching this video you should be able to answer such questions as: do you have the same IP address when you are at Galvanize as you do when you are at home? Do you have the same IP address as the student sitting next to you? This will become especially important when we set up security groups in EC2. But I get ahead of myself....
3. Read the article on [HTTP](HTTP/README.md), then watch [REST API concepts and examples](https://www.youtube.com/watch?v=7YcW25PHnAA) (9 min). By the end of this, you should have a clear idea of how HTTP works in general and how web APIs (specifically REST APIs) work in particular.
4. A 404 error is the most common error we'll come across, indicating that client can communicate with a server but that the server was not able to find what was requested.  Read through the developer guide on how to [Configure a Bucket for Website Hosting](http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html).  Using 'Example 3: Redirect for an HTTP error', create a redirect rule for a 404 error that redirects to a new file `404-error.html`.

For today's lab, you will be generating a static web page based upon data gleaned from the Twitter API. You will be hosting that web page on S3. This web page is so simple, it does not need a dedicated server. That said,_(the following is optional)_ if you feel like taking it a step further, watch [How to use SimpleHTTPServer for local development](https://www.youtube.com/watch?v=O3DWY7Rak0s) to see how to more closely mimic what happens when you host a static website on S3. If you want to go further still, check out [Flask](http://flask.pocoo.org/)  to see how you might create a dynamic web service. Alternatively, if you are interested in hosting your own website on S3 using a custom domain (instead of `<bucket-name>.s3-website-<AWS-region>.amazonaws.com`), check out this [Example: Setting Up a Static Website Using a Custom Domain](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)

#### On completing this article, you should have:

- Watched two videos
- Read three articles
- Practiced creating a static web page
- Issued a simple GET request
