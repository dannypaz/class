## Intro To The Web

[How The Internet Works](https://www.youtube.com/watch?v=7_LPdttKXPc)

## DNS Lookup & IP Addresses
__DNS__, or __Domain Name System__ is a distributed set of servers that looks up an IP address for a human readable domain, like [https://www.google.com/](https://www.google.com/).

#### Exercise

Using chrome developer tools and the network tab, figure out the IP address for a popular site like google.

## Data Transmission

![Data Transmission](http://odetocode.com/aimages/http/netlayer.png)

### TCP/IP - One Protocol To Rule Them All

Thank TCP/IP for the modern web- it's the underlying transport protocol that gets everything where it needs to go. It's the standardized way that all internet devices talk to one another.

__TCP__ or Transmission Control Protocol is responsible for ensuring that data gets to and from a server reiably and in a timely manner.  The internet is an unreliable place so TCP can handle retransmitting things that fail to send.  It also has the job of taking a bigger chunk of data and breaking it down into smaller packets that get sent out.

__IP__ or Internet Protocol is responsible for getting the packets to the correct place.  The IP address is analogous to a physical street address that the IP layer uses to route packets to the right place.

## A few other protocols

#### DHCP - Dynamic Host Configuration Protocol

DHCP is used for allocation of dynamic IP addresses to computers in a network.

#### LDAP - Lightweight Directory Access Protocol

LDAP is used for collecting information about users and e-mail addresses from the internet.

#### SSL - Secure Sockets Layer

The SSL protocol is used to encrypt data for secure data transmission.

#### TLS - Transport Layer Security

The TLS protocol is a newer and more secure version of SSL.

##### Still confused about TCP/IP vs HTTP? Check out these articles

http://stackoverflow.com/questions/23157817/http-vs-tcp-ip-send-data-to-a-web-server
http://www.differencebetween.net/technology/internet/difference-between-tcp-and-http/
http://www.quora.com/What-is-the-difference-between-HTTP-protocol-and-TCP-protocol
