---
title: Testing Email Manually with Telnet (spoofing email)
author: Nick Anderson
type: post
date: 2008-04-06T17:15:35+00:00
url: /2008/04/06/testing-email-manually-with-telnet-spoofing-email/
categories:
  - Posts
tags:
  - command line
  - email
  - manual
  - smtp
  - spoof
  - telnet
  - testing

---
Being able to send email manually seems to be a bit of a lost art. It is extremely handy to know how to use telnet to send email for testing procmail filters, and any other part of your mail system. It can also be fun to spoof email to a friend or co-worker. Read on for a quick run down.<!--more-->

<!--adsense-->


  
Open a connection to the mail server.
  
`telnet mail.server.com 25`
  
Now initiate the SMTP session. The host connecting to the remote SMTP server identifies itself by it&#8217;s fully qualified DNS host name, so be sure to replace localhost.localdomain with your sending servers FQDN.
  
``Being able to send email manually seems to be a bit of a lost art. It is extremely handy to know how to use telnet to send email for testing procmail filters, and any other part of your mail system. It can also be fun to spoof email to a friend or co-worker. Read on for a quick run down.<!--more-->

<!--adsense-->


  
Open a connection to the mail server.
  
`telnet mail.server.com 25`
  
Now initiate the SMTP session. The host connecting to the remote SMTP server identifies itself by it&#8217;s fully qualified DNS host name, so be sure to replace localhost.localdomain with your sending servers FQDN.
  
`` 
  
MAIL indicates who is sending the mail. Any returned mail will be sent back to this address.
  
```Being able to send email manually seems to be a bit of a lost art. It is extremely handy to know how to use telnet to send email for testing procmail filters, and any other part of your mail system. It can also be fun to spoof email to a friend or co-worker. Read on for a quick run down.<!--more-->

<!--adsense-->


  
Open a connection to the mail server.
  
`telnet mail.server.com 25`
  
Now initiate the SMTP session. The host connecting to the remote SMTP server identifies itself by it&#8217;s fully qualified DNS host name, so be sure to replace localhost.localdomain with your sending servers FQDN.
  
``Being able to send email manually seems to be a bit of a lost art. It is extremely handy to know how to use telnet to send email for testing procmail filters, and any other part of your mail system. It can also be fun to spoof email to a friend or co-worker. Read on for a quick run down.<!--more-->

<!--adsense-->


  
Open a connection to the mail server.
  
`telnet mail.server.com 25`
  
Now initiate the SMTP session. The host connecting to the remote SMTP server identifies itself by it&#8217;s fully qualified DNS host name, so be sure to replace localhost.localdomain with your sending servers FQDN.
  
`` 
  
MAIL indicates who is sending the mail. Any returned mail will be sent back to this address.
  
``` 
  
RCPT indicates who will be receiving the mail. You can indicate more than one user by issuing multiple RCPT commands.
  
 `rcpt to: someguy@hisdomain.com`
  
DATA indicates that you are about to send the text (or body) of the message. The message text must end with the following five letter sequence: &#8220;\r\n.\r\n.&#8221;
  
 `data<br />
From: Your Name<br />
Subject: Very important<br />
This is the first line<br />
This is the second line<br />
.`
  
QUIT ends the SMTP session.
  
`quit`
  
<!--adsense-->