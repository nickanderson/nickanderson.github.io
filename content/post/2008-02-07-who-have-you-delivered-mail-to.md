---
title: Who have you delivered mail to?
author: Nick Anderson
type: post
date: 2008-02-08T03:26:56+00:00
url: /2008/02/07/who-have-you-delivered-mail-to/
categories:
  - Posts
tags:
  - email
  - exim

---
The company I work for (<a href="http://www.absorbentprinting.com" mce_href="http://www.absorbentprinting.com">Absorbent Ink</a>) that makes <a href="http://www.absorbentprinting.com/corporate-gifts" mce_href="http://www.absorbentprinting.com/corporate-gifts">corporate gifts</a> and other <a href="http://www.absorbentprinting.com/unique\_products.php" mce\_href="http://www.absorbentprinting.com/unique_products.php">personalized products</a>. has started sending out a <a href="http://www.absorbentprinting.com/scoop.php" mce_href="http://www.absorbentprinting.com/scoop.php">newsletter</a>. Part of this newsletter process for me has been tuning one of our <a href="http://www.exim.org" mce_href="http://www.exim.org">exim</a> based mail servers.
   
<!--more-->


   
One of our mailer scripts failed the other day. Unfortunately it was not logging properly and did not handle the error and continue to send to our news letter recipients. I had to check the exim logs to figure out who had actually recieved the newsletter from us.

This one liner will check your current exim mainlog and print out all the emails that have been delivered from sender@domain.com.
   
`The company I work for (<a href="http://www.absorbentprinting.com" mce_href="http://www.absorbentprinting.com">Absorbent Ink</a>) that makes <a href="http://www.absorbentprinting.com/corporate-gifts" mce_href="http://www.absorbentprinting.com/corporate-gifts">corporate gifts</a> and other <a href="http://www.absorbentprinting.com/unique\_products.php" mce\_href="http://www.absorbentprinting.com/unique_products.php">personalized products</a>. has started sending out a <a href="http://www.absorbentprinting.com/scoop.php" mce_href="http://www.absorbentprinting.com/scoop.php">newsletter</a>. Part of this newsletter process for me has been tuning one of our <a href="http://www.exim.org" mce_href="http://www.exim.org">exim</a> based mail servers.
   
<!--more-->


   
One of our mailer scripts failed the other day. Unfortunately it was not logging properly and did not handle the error and continue to send to our news letter recipients. I had to check the exim logs to figure out who had actually recieved the newsletter from us.

This one liner will check your current exim mainlog and print out all the emails that have been delivered from sender@domain.com.
   
`