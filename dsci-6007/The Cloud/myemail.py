#https://docs.python.org/2/library/email-examples.html
#!/usr/bin/env python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# me == my email address
# you == recipient's email address
me = "jonathan.hilgart@galvanize.it"
you = "jonathan.hilgart@gmail.com"
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Twitter Report"
msg['From'] = me
msg['To'] = you
# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
# file_html_index = open("index.html", "r").decode('utf-8')
#print(file_html_index)
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the table you wanted. {}
    </p>
  </body>
</html>
""".format(open("index.html", "r").read())
#html = file_html_index
# Record the MIME types of both parts - text/plain and text/html.
#msg.attach(MIMEText(open("newfile.txt").read()))
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
