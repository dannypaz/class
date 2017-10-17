## The Syntax of a Uniform Resource Locator (URL)

All resource on the Internet is associated with a global identifer: a Uniform Resource Locator (URL). Each URL, furthmore, [conforms to a particular syntax](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax)

Let's explore a description of the syntax from the perspective of [how Googlers talk about parts of a URL](https://www.mattcutts.com/blog/seo-glossary-url-definitions/).

## Underlying Parts of a URL

Some parts of a URL can be understood based on an initil read, such as a query string. However, further elaboration would help with two parts: hostname (with IP address) and protocol. The latter will be discussed during the next section; the former will be discussed now.

#### IP Address

An IP address determines the location of a machine on a network. This an analogous to how a home can be gound with an address. In regards to the Internet, an IP address takes the form of `XXX.XXX.XXX.XXX`, where each grouping of `XXX` (octet) is a value that is >= `0` && <= `255`. In other words, each octet can be one of 256 values.

#### Domain Name System (DNS)

The[DNS](http://www.webopedia.com/TERM/D/DNS.html) maps domain names (e.g., `google.com`) to IP addresses (like `216.58.217.46`) for improved user experience--words are easier to remember. In very general terms, a DNS could be conceptualized as a large JavaScript object--keys are the domain names and values are the corresponding IP addresses.

## The HTTP

The most important component of a web URL is arguably the protocol: A set of rules that define the communication between a client and a server. For websites, the protocol is often [HTTP](https://en.wikipedia.org/wiki/Hypertext). Many of you may have noticed this protocol being used when you visit your favorite websites. There's a lot to learn about HTTP, but we'll focus our attention on HTTP's use of a request and response model.

#### HTTP Request

A client sends an HTTP request in many ways, including entering a URL in an address bar of a web browser, submiting a form, or clicking a hyperlink. When any of these three events occur, a browser submits a request with three components:

- request line (includes a method)
- headers
- body

#### HTTP Response

In turn, a request will return a response with three components:

- response line (includes a [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes))
- headers
- body

## Why is an HTTP server useful?

In 1989, Tim Berners-Lee proposed a new project to his employer CERN. The goal of this project was to ease the exchange of information between scientists by using a hypertext system. In 1990, the project resulted in two programs—the world's first HTTP client and server.

Because exchanging information over HTTP is so effective, there are countless HTTP clients and servers in existence today. The most effective of these servers are able to handle [thousands of requests per second](https://www.techempower.com/benchmarks/), thus giving millions of people around the world the ability to access and exchange information every day. Without HTTP servers, the rapid and global exchange of information over the Internet would not exist.

## What's an HTTP Request?

The client (or user agent) sends a plain-text message called an **HTTP request** to a server on behalf of the user. Aside from web browsers, other common user agents include web crawlers, native apps, and mobile apps.

An HTTP request is composed of the following parts.

1. A method (or verb)
1. A path
1. An HTTP version
1. Key-value headers
1. And an optional body

Here's an example of what an HTTP request looks like.

```text
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/0.9.3
```

**QUESTION:** Looking at the above message, can you identify the parts of an HTTP request?

While an HTTP request can only contain one method, there are several different methods that a client can choose from. Each method instructs a server on how to process the request. Without the use of Ajax, web browsers are only capable of sending HTTP requests with the following methods.

| Method | Description                                                 |
|--------|-------------------------------------------------------------|
| `GET`  | Used retrieve a resource, like an HTML file, from a server. |
| `POST` | Used send information, like user input, to a server.        |

You'll learn about additional HTTP methods, like `PUT`, `PATCH`, and `DELETE`, when we encounter RESTful HTTP servers later in the course.

**QUESTION:** When does a web browser make `GET` requests? When does it make `POST` requests?

## What's an HTTP response?

When the server receives an HTTP request, its job is to process the request and sends a plain-text message, called an **HTTP response**, back to the client. In addition to Node.js, popular HTTP servers include Apache, Nginx, and Python's built-in `SimpleHTTPServer`.

An HTTP response is composed of the following parts.

1. An HTTP version
1. A status code
1. Key-value headers
1. And an optional body

Here's an example of what an HTTP response looks like.

```text
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 11
Content-Type: text/plain
Date: Mon, 13 Jun 2016 04:28:36 GMT

Hello world
```

**QUESTION:** Looking at the above message, can you identify the parts of an HTTP response?

While an HTTP response can only contain one status code, there are many different codes that a server can choose from. Each status code explains to the client how the server interpreted the request. Status codes are three-digit numbers that are grouped into the following categories.

| Status Code Group | Description                                             |
|-------------------|---------------------------------------------------------|
| `1XX`             | Request accepted, ready for the next one.               |
| `2XX`             | Request accepted, the server's work is complete.        |
| `3XX`             | Request accepted, but additional client work is needed. |
| `4XX`             | Request accepted, but there was an error on the client. |
| `5XX`             | Request accepted, but there was an error on the server. |

Here are a few websites that list the possible HTTP status codes and their meaning through cute photos of animals.

- [HTTP Status Cats](https://http.cat/)
- [HTTP Status Dogs](https://httpstatusdogs.com/)

And, of course, there's boring-old Wikipedia when you need the official, textual explanation.

- [Wikipedia - List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

**QUESTION:** The most common status codes are `200`, `302`, `304`, `404`, and `500`. Can you figure out why?
