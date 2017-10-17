# Postman

Make sure you have [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) installed. Now, open Postman and make a GET request to google.com.

__Sample GET request using Postman__

```
GET  HTTP/1.1
Host: www.google.com
Cache-Control: no-cache
Postman-Token: 4ce8b655-abae-8aed-af11-058633be3129
```

__Sample Response__

```
HTTP/1.1 200 OK
alternate-protocol: 443:quic,p=1
cache-control: private, max-age=0
content-encoding: gzip
content-type: text/html; charset=UTF-8
date: Tue, 12 May 2015 14:12:05 GMT
expires: -1
server: gws
status: 200 OK
version: HTTP/1.1
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="/images/google_favicon_128.png" itemprop="image"><meta content="origin" id="mref" name="referrer"><title>Google</title>   <script>(function(){window.google={kEI:'yglSVaXsAYKZsAWknIDwDg',kEXPI:'3700062,3700334,3700366,4014789,4017578,4023709,4024035,4026111,4029815,4030091,4030312,4032500,4032643,4032645,4032678,4033143,4033191,4033344,4033372,4035295,4035327,4035980,4036006,4036054,4036533,8500394,8501248,8501280,8501295,8501350,8501406,8501489,10200083,10200835,10201102,10201181',authuser:0,j:
...
```

Now, generate a code snippet by clicking the code snippet button. You should be able to generate it in multiple languages. For now, select cURL.

Copy the code snippet you have- you should get something like this:
```shell
curl -X GET -H "Cache-Control: no-cache" -H "Postman-Token: 20f68a93-c63b-7579-c687-5853dc486f3c" 'http://google.com'
```

Try running it in your console- what do you get?
