# HTTP In More Depth

What is HTTP? The _Hypertext Transfer Protocol_, or HTTP, defines a protocol, or set of rules around how communication may occur, to transfer hypertext. Read Introduction paragraph and sections "Types and uses of hypertext", "History", "Implementations" in [Hypertext](https://en.wikipedia.org/wiki/Hypertext). Answer the following questions:

  1. Who is Tim Berners-Lee?
  1. What is hypertext and why is it important?
  1. Is hypertext a new concept (new meaning in the last 30 years)?

The corresponding answers are provided here:

  1. [Tim Berners-Lee](http://i.guim.co.uk/img/static/sys-images/Technology/Pix/pictures/2012/10/9/1349788648537/tbl-460.png?w=620&q=85&auto=format&sharp=10&s=630f0146cc833c820ed33318f9058610) is the creator of the World Wide Web, the project was started while he was a scientist at CERN. Did Tim Berners-Lee create the internet? No.
  1. Hypertext is text displayed on the screen of a device (for our purposes a computer) which can link to other pieces of text. Hypertext is an important concept because it is the concept behind the world wide web. Recall that the internet provides support for the communication of computers which are attached to it, we can refer to this as machines that are networked. The world wide web utilizes a network of computers to communicate via the HTTP protocol. This allows computers, or _nodes_, to communicate hypertext documents with eachother.
  1. Not at all. Like many other computer science concept, hypertext was first toyed around with in the 1940s on paper. In the 1960s when technology had evolved sufficiently to meet the ability of theory, many advances were made, including the introduction of the first word processor. So a word processor is really just an example of hypertext system.

But that is just a high-level of what HTTP is. Later in this Learning Experience you will go through an exercise that gets into the nitty gritty of what HTTP boils down to: strings being sent across a network. Whether is it the hypermedia document itself or the routing of location (URL), everything will rely on strings. Can you think of any reason why communication of this sort, a.k.a. involving strings, may have security implications?

In music a popular pattern is known as [call and response (watch this at normal speed)](https://www.youtube.com/watch?v=pxg4AP1MKDk). It appears in all different types of music from folk to blues to tribal and religious music from around the world. But how is this possibly related to HTTP? HTTP works off of an analogous model known as _request_ and _response_.

In the most simplified view of a networked application, your machine, `localhost`, will serve as the server and your browser as the client (you can think of this as the entity who makes requests of the server for [hypermedia](http://www.rc.au.net/papers/www-0595/wwwhype2.html)). Here is the _very rough_ chain of events (with some major simplifications) for a program that is running locally:

  1. Open browser, visit `localhost:8000`. Another way to say this is use a client, in this case a browser, to make an HTTP request to `localhost:8000`.
  1. Machine is smart enough to know that `localhost` does not involve the internet, so relays to port `8000` of itself
  1. Web server running on port `8000` of machine receives the request and processes it
  1. Web server, based on the procesing of the request, _responds_ with hypertext or hypermedia
  1. Browser (client) receives hypermedia and renders it

Later in this Learning Experience you will build a simple HTTP server using Node.js. Unfortunately the model for the general world wide web is not as simple. There are a few concepts to understand upfront that are useful:

  1. An _IP address_ determines the location of a machine on the network. An analogy for this is that people can find you by going to your home address, this is no different, but machines are much more precise with location. IP addresses take the form of `XXX.XXX.XXX.XXX` where each grouping of `XXX`, or _octet_, is a value that is greater than or equal to `0` and less than or equal to `255`, so each grouping of `XXX` can be one of 256 values.
  1. The _Domain Name System_, or _DNS_ is a mapping of domain names (like `google.com`) to IP addresses (like `216.58.217.46`). In a simplified view of this, it can be thought of like a giant JavaScript object whose keys are the domain names and whose values are the corresponding IP addresses. One of the most popular DNS providers is Google.

Before moving on, work through the following two questions:

  1. How many different IP addresses are there (do not worry about computing the value)?
  1. What is DNS?

The corresponding answers are:

  1. Too many to count, *_just kidding_*! `256<sup>4</sup>`
  1. DNS is the Domain Name System, the service maps domain names to IP addresses.

You need to know what DNS is and how it factors in to the bigger picture, this is a diagram of how the web works with DNS included:

![DNS Diagram](http://ods.org/images/dns_diagram.jpg)

Here is an alternative view of the same concept:

![DNS Diagram 2](http://50.17.207.32/wp-content/uploads/2012/09/DNS_basics3.png)

Compare and contrast the model that uses DNS with the model for the server running locally, make sure you can identify which parts use the network connection.

The following, sequenced exercises should help make the request/response paradigm more evident by using Node.js in a web context and make some of the details of HTTP more concrete.
