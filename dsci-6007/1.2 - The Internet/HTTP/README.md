## Objectives

- Explain what HTTP is.
- Explain why HTTP is useful?
- Explain what an HTTP request is.
- Explain what an HTTP response is.
- Diagram HTTP request-response cycle.
- Send HTTP requests and receive HTTP responses for HTML.
- Explain what JSON is.
- Explain why JSON is useful.
- Send HTTP requests and receive HTTP responses for JSON.

## What's HTTP?

**Hypertext** is text that uses hyperlinks to connect the reader to other files that contain hypertext. The most popular hypertext format is, of course, the Hypertext Markup Language, better known as HTML. The approximately 4.6 billion HTML pages, interconnected via hyperlinks, form the structure known as the **World Wide Web**, or Web for short.

HTML files are transferred across the Internet using a communication protocol. A **protocol** is a system of rules that allow two or more devices on a computer network to transmit information. The protocol of the Web is called the Hypertext Transfer Protocol (**HTTP**) and its job, as you might expect, is to transmit hypertext over a computer network. As it turns out, HTTP is quite flexible and is also used to transmit non-hypertext data as well. Tim Berners-Lee and his team at CERN are credited with inventing HTTP in 1989 and then HTML in 1990.

HTTP is request–response protocol. In other words, it sends messages between two programs called a client and a server. Typically, a **web browser** acts as the client and an application hosting a web site, known as a **web server**, acts as the server.

**NOTE:** The term "server" here is referring to software and _not_ a physical machine which is often called a server as well.

![](http://i.imgur.com/VbuGgIn.png)

## Why is HTTP useful?

HTTP provides a consistent, uniform interface that separates clients from servers. This separation of concerns means that, for example, clients can focus on presenting the user interface instead of managing resources. On the other hand, servers can focus on managing resources instead of presenting the user interface. This allows both clients and servers to be much simpler and more scalable. Additionally, clients and servers can be replaced and developed independently so long as the HTTP interface between them is not altered.

## What's an HTTP Request?

The client (or user agent) sends a plain-text message called an **HTTP request** to a server on behalf of the user. Aside from web browsers, other common user agents include web crawlers, native apps, and mobile apps.

An HTTP request is composed of the following parts.

1. A method (or verb)
1. A path
1. An HTTP version
1. Key-value pairs called **headers**
1. And an optional body

Here's an example of what an HTTP request looks like.

```
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: fs-student-roster.herokuapp.com
User-Agent: HTTPie/0.9.3
```

**QUESTION:** Looking at the above message, can you identify the parts of an HTTP request?

While an HTTP request can only contain one method, there are several different methods that a client can choose from. Each method instructs a server on how to process the request. Without the use of Ajax, web browsers are only capable of sending HTTP requests with the following methods.

| Method | Description                                                 |
|--------|-------------------------------------------------------------|
| `GET`  | Used retrieve a resource, like an HTML file, from a server. |
| `POST` | Used send information, like user input, to a server.        |

**QUESTION:** When does a web browser make `GET` requests? When does it make `POST` requests?

## What's an HTTP response?

The server receives an HTTP request, attempts to process it, and sends a plain-text message called an **HTTP response** back to the client. Popular web servers include Apache, Nginx, Node.js, and Python's built-in `SimpleHTTPServer`.

An HTTP response is composed of the following parts.

1. An HTTP version
1. A status code
1. Key-value headers
1. And an optional body

Here's an example of what an HTTP response looks like.

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 631
Content-Type: text/html; charset=utf-8
Date: Sun, 22 May 2016 22:54:23 GMT
Etag: W/"277-ENWB837FwX/qicQv2cu/qA"
Server: Cowboy
Vary: Accept
Via: 1.1 vegur

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/style.css">
    <title>Student Roster</title>
  </head>
  <body>
    <main>
      <h1>Student Roster</h1>

        <section>
          <h3>Daenerys Targaryen</h3>
          <h4>Hobby: Motherhood</h4>
          <img src="https://i.imgur.com/KlycRG5.jpg" alt="Daenerys Targaryen" />
        </section>

        <section>
          <h3>Tyrion Lannister</h3>
          <h4>Hobby: Traveling</h4>
          <img src="https://i.imgur.com/fFMusdC.png" alt="Tyrion Lannister" />
        </section>

    </main>
  </body>
</html>
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

- [HTTP Status Cats](https://http.cat/)
- [HTTP Status Dogs](https://httpstatusdogs.com/)
- [Wikipedia - List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

**QUESTION:** The most common status codes are `200`, `302`, `304`, `404`, and `500`. Can you figure out why?

## How do you diagram the HTTP request-response cycle?

[SEE WHITEBOARD]

## How do you send HTTP requests and receive HTTP responses for HTML?

cURL is a command line program that sends HTTP requests to servers and outputs their raw HTTP response to the Terminal. In other words, it can do pretty much anything your web browser can do except render the HTTP response body as a pretty picture. cURL is often used for testing and debugging HTTP requests and responses.

Try running the following command.

```
curl -v -X GET https://fs-student-roster.herokuapp.com/students
```

You should see something like this.

```
*   Trying 54.225.74.127...
* Connected to fs-student-roster.herokuapp.com (54.225.74.127) port 443 (#0)
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* Server certificate: *.herokuapp.com
* Server certificate: DigiCert SHA2 High Assurance Server CA
* Server certificate: DigiCert High Assurance EV Root CA
> GET / HTTP/1.1
> Host: fs-student-roster.herokuapp.com
> User-Agent: curl/7.43.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: Cowboy
< Connection: keep-alive
< Access-Control-Allow-Origin: *
< Vary: Accept
< Content-Type: text/html; charset=utf-8
< Content-Length: 631
< Etag: W/"277-ENWB837FwX/qicQv2cu/qA"
< Date: Mon, 23 May 2016 14:42:19 GMT
< Via: 1.1 vegur
<
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/style.css">
    <title>Student Roster</title>
  </head>
  <body>
    <main>
      <h1>Student Roster</h1>

        <section>
          <h3>Daenerys Targaryen</h3>
          <h4>Hobby: Motherhood</h4>
          <img src="https://i.imgur.com/KlycRG5.jpg" alt="Daenerys Targaryen" />
        </section>

        <section>
          <h3>Tyrion Lannister</h3>
          <h4>Hobby: Traveling</h4>
          <img src="https://i.imgur.com/fFMusdC.png" alt="Tyrion Lannister" />
        </section>

    </main>
  </body>
</html>
* Connection #0 to host fs-student-roster.herokuapp.com left intact
```

cURL is a very useful command and pre-installed on most Unix operating systems. However, I prefer another program called [HTTPie](https://github.com/jkbrzt/httpie). Like cURL, HTTPie is a command line HTTP client. But its goal is to make command line interaction with a web server as human-friendly as possible. Also like cURL, HTTPie is used for testing and debugging HTTP requests and responses.

To install HTTPie, run the following command.

```
brew install httpie
```

The try out the exact some cURL command as above in HTTPie.

```
http -v GET https://fs-student-roster.herokuapp.com/students
```

You should see something like this.

```
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: fs-student-roster.herokuapp.com
User-Agent: HTTPie/0.9.3



HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 631
Content-Type: text/html; charset=utf-8
Date: Sun, 22 May 2016 22:54:23 GMT
Etag: W/"277-ENWB837FwX/qicQv2cu/qA"
Server: Cowboy
Vary: Accept
Via: 1.1 vegur

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/style.css">
    <title>Student Roster</title>
  </head>
  <body>
    <main>
      <h1>Student Roster</h1>

        <section>
          <h3>Daenerys Targaryen</h3>
          <h4>Hobby: Motherhood</h4>
          <img src="https://i.imgur.com/KlycRG5.jpg" alt="Daenerys Targaryen" />
        </section>

        <section>
          <h3>Tyrion Lannister</h3>
          <h4>Hobby: Traveling</h4>
          <img src="https://i.imgur.com/fFMusdC.png" alt="Tyrion Lannister" />
        </section>

    </main>
  </body>
</html>
```

## What's JSON?

JavaScript Object Notation (**JSON**) is the de facto data exchange format of the Web. JSON is a string that looks very similar to native objects and arrays. That means JSON must be parsed in order for it to have meaning in a program.

Here's an example of an empty JSON object.

```json
{ }
```

Here's an example of a non-empty JSON object.

**NOTE:** Both JSON strings and JSON object keys **must** be wrapped in double quotes `"`.

```json
{
  "avatar": "https://i.imgur.com/KlycRG5.jpg",
  "hobby": "Motherhood",
  "name": "Daenerys Targaryen"
}
```

Here's an example of a JSON array.

```json
["Daenerys Targaryen", "Tyrion Lannister"]
```

Here's an example of a JSON array of objects.

```json
[
  {
    "avatar": "https://i.imgur.com/KlycRG5.jpg",
    "hobby": "Motherhood",
    "name": "Daenerys Targaryen"
  },
  {
    "avatar": "https://i.imgur.com/fFMusdC.png",
    "hobby": "Traveling",
    "name": "Tyrion Lannister"
  }
]
```

## Why is JSON useful?

**Serialization** is the process of translating a program's data to and from a string. Data that's been serialized to a string can be stored in a file, inserted into a database, or transmitted across a computer network. At some point in the future, a program retrieves the string and the data is reconstructed. The programs involved in the serialization process can be completely different and even written in completely different languages. The key to serialization is the data remains unchanged from end to end.

JSON is a serialization format. JavaScript objects, arrays, numbers, strings, booleans, and null are all translated into a JSON string. Here's an example of translating a JavaScript object into a JSON string.

```javascript
var queen = {
  avatar: 'https://i.imgur.com/KlycRG5.jpg',
  hobby: 'Motherhood',
  name: 'Daenerys Targaryen'
};

var queenJSON = JSON.stringify(queen);

// Store or transmit the JSON string
```

This JSON string can now be stored or transmitted across a computer network. At some point in the future, a program retrieves the string and the data is reconstructed into the same JavaScript objects, arrays, numbers, booleans, and null. Here's an example of translating a JSON string back to JavaScript object.

```javascript
var queenJSON = '{ "avatar": "https://i.imgur.com/KlycRG5.jpg", "hobby": "Motherhood", "name": "Daenerys Targaryen" }';

var queen = JSON.parse(queenJSON);

console.log(queen.name);  // Daenerys Targaryen
```

In other words, JSON is what allows two programs to transfer data to each other and guarantee the data remains the same on both sides.

## How do you send HTTP requests and receive HTTP responses for JSON?

In addition to HTML, the server in charge of our student roster can accept HTTP requests for JSON. Try running the following command.

```
http -vj GET http://fs-student-roster.herokuapp.com/students
```

You should see something like this.

```
GET / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/json
Host: fs-student-roster.herokuapp.com
User-Agent: HTTPie/0.9.3



HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 186
Content-Type: application/json; charset=utf-8
Date: Mon, 23 May 2016 16:41:06 GMT
Etag: W/"ba-5jN/E7c/BNAIQrvxBntdMg"
Server: Cowboy
Vary: Accept
Via: 1.1 vegur

[
    {
        "avatar": "https://i.imgur.com/KlycRG5.jpg",
        "hobby": "Motherhood",
        "name": "Daenerys Targaryen"
    },
    {
        "avatar": "https://i.imgur.com/fFMusdC.png",
        "hobby": "Traveling",
        "name": "Tyrion Lannister"
    }
]
```

**QUESTION:** What are some of the differences in the HTTP request and response when requesting JSON?

Go to this [student roster page](https://fs-student-roster.herokuapp.com/students). How can you add a student profile to this page without web form? With the server's **web API**, of course!

Try running the following command.

```
http -vj POST http://fs-student-roster.herokuapp.com/students
```

You should see something like this.

```
POST / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 0
Content-Type: application/json
Host: fs-student-roster.herokuapp.com
User-Agent: HTTPie/0.9.3



HTTP/1.1 400 Bad Request
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 129
Content-Type: application/json; charset=utf-8
Date: Mon, 23 May 2016 19:34:17 GMT
Etag: W/"81-UYxtgaXWHAmNTFCDu0HMMw"
Server: Cowboy
Vary: Accept
Via: 1.1 vegur

{
    "error": "Invalid JSON Body",
    "fix": "Needs name, hobby, and avatar key/value String pairs",
    "see": "GET / Accept: application/json"
}
```

Well, that didn't work as expected. It looks like to make a `POST` request to this server, the HTTP request needs to include a JSON object with the following key/value pairs.

| Key     | Value                                     |
|---------|-------------------------------------------|
| `name`  | Your full name as a string                |
| `hobby` | Your favorite hobby as a string           |
| `avatar`| A URL of your profile picture as a string |

Try running this command, but replacing the values with your own information.

```
http -vj POST http://fs-student-roster.herokuapp.com/students name='Philip J. Fry' hobby='Time travel' avatar='http://i.imgur.com/F48J2Ij.jpg'
```

You should see something like this.

```
POST / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 93
Content-Type: application/json
Host: fs-student-roster.herokuapp.com
User-Agent: HTTPie/0.9.3

{
    "avatar": "http://i.imgur.com/F48J2Ij.jpg",
    "hobby": "Time travel",
    "name": "Philip J. Fry"
}

HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 33
Content-Type: application/json; charset=utf-8
Date: Mon, 23 May 2016 19:44:19 GMT
Etag: W/"21-ZUo1a34ZIx+AEtYefXTYkw"
Server: Cowboy
Vary: Accept
Via: 1.1 vegur

{
    "success": "New student created"
}
```

**QUESTION:** What's different about this HTTP request and response?

Try sending another `GET` request to the server.

```
http -vj GET http://fs-student-roster.herokuapp.com/students
```

**QUESTION:** What's different about this response?

## What's a web API?

An application programming interface, or **API**, is a broad term used to describe any set of protocols for interacting with a computer program. A web API is a contract between a client and a server. According to the contract, a web API allows a client to send specific HTTP requests to a server and the server will send specific HTTP responses back.

## How do you use a web API?

One fantastic web API is the OMDB API. The contract for this API is defined at the [OMBD API documentation](http://omdbapi.com/). After reading the documentation, we determine that we can use the query parameter `t` to search the database for movies with a specific title. Lets search OMDB for Game of Thrones.

[http://www.omdbapi.com/?t=Game of Thrones](http://www.omdbapi.com/?t=Game of Thrones)

```shell
http -v GET 'http://www.omdbapi.com/?t=Game of Thrones'
```

You should see something like this.

```
GET /?t=Game%20of%20Thrones HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: www.omdbapi.com
User-Agent: HTTPie/0.9.3



HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
CF-Cache-Status: HIT
CF-RAY: 2a73b9e4c0490c4d-SEA
Cache-Control: public, max-age=86400
Connection: close
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Date: Sun, 22 May 2016 22:32:48 GMT
Expires: Mon, 23 May 2016 22:32:48 GMT
Last-Modified: Sun, 22 May 2016 22:22:02 GMT
Server: cloudflare-nginx
Set-Cookie: __cfduid=d2175d3d50fb3d257156bd344bd64c6341463956368; expires=Mon, 22-May-17 22:32:48 GMT; path=/; domain=.omdbapi.com; HttpOnly
Transfer-Encoding: chunked
Vary: Accept-Encoding
X-AspNet-Version: 4.0.30319
X-Powered-By: ASP.NET

{
    "Actors": "Peter Dinklage, Lena Headey, Emilia Clarke, Kit Harington",
    "Awards": "Won 1 Golden Globe. Another 180 wins & 297 nominations.",
    "Country": "USA",
    "Director": "N/A",
    "Genre": "Adventure, Drama, Fantasy",
    "Language": "English",
    "Metascore": "N/A",
    "Plot": "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise up to power. Meanwhile a forgotten race, bent on destruction, return after thousands of years in the North.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjM5OTQ1MTY5Nl5BMl5BanBnXkFtZTgwMjM3NzMxODE@._V1_SX300.jpg",
    "Rated": "TV-MA",
    "Released": "17 Apr 2011",
    "Response": "True",
    "Runtime": "56 min",
    "Title": "Game of Thrones",
    "Type": "series",
    "Writer": "David Benioff, D.B. Weiss",
    "Year": "2011–",
    "imdbID": "tt0944947",
    "imdbRating": "9.5",
    "imdbVotes": "951,668"
}
```

## Exercise

Try searching for a few of your favorite movies using the OMDB API.

## Resources

- [The Open Movie Database](http://omdbapi.com/)
- [Wikipedia - Application Programming Interface](https://en.wikipedia.org/wiki/Application_programming_interface)
- [Wikipedia - Hypertext](https://en.wikipedia.org/wiki/Hypertext)
- [Wikipedia - Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [World Wide Web Size](http://www.worldwidewebsize.com/)
- [Youtube - History of the Internet](https://www.youtube.com/watch?v=9hIQjrMHTv4)
- [Youtube - How The Internet Works](https://www.youtube.com/watch?v=7_LPdttKXPc)

## Further Exercises

[HTTP Header Parser](https://github.com/gSchool/http-parser-js)

Go to this [student roster page](https://pacific-stream-1533.herokuapp.com/). It is empty!  Your job is to create a profile picture of yourself using the apis:

1. Using curl, make a GET request to https://pacific-stream-1533.herokuapp.com/students.  Use [a json visualizer](http://jsonlint.com/) to see what you're working with.  Make your request verbose!
2. Make a post request to https://pacific-stream-1533.herokuapp.com/students using curl.  There are some specs for the api request:
    * The content type of the request should be application/json
    * The json object must contain 3 fields: __name__, __hobby__, and __avatar__.  The avatar value should be a url of a picture of you.
    * The api has a very easily breakable form of authentication.  In order to post, your request must send a cookie.  The name of the cookie is login and the value is g9fullstack.
3. Make another GET request to https://pacific-stream-1533.herokuapp.com/students to make sure your name got posted. Make your request verbose.

- https://github.com/gSchool/StudentRosterGetAndPostPractice

## Terms

Protocol
> The way in which information is being retrieved.

Domain
> The human-readable name of the computer location

Query Parameters
> Key / Value pairs added to URLs to provide additional information about the request.

HTTP Verbs
> GET, POST, PUT, and DELETE. These four main actions are used to describe what kind of action is being taken when accessing an endpoint.

HTTP Status Codes
> Codes provided on a response to give more information about what happened.

* SLIDES: [How the Web Works](http://slides.com/wesleyreid/how-the-web-works#/)

## Dig Deeper

- [History of the Web](History of the Web.md)
- [Learn more about HTTP](Deeper.md)
- [Learn more about Postman](Postman.md)
