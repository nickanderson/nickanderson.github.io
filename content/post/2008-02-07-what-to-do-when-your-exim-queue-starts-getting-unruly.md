---
title: What to do when your exim queue starts getting unruly.
author: Nick Anderson
type: post
date: 2008-02-08T03:22:20+00:00
url: /2008/02/07/what-to-do-when-your-exim-queue-starts-getting-unruly/
categories:
  - Posts
tags:
  - email
  - exim
  - exiqgrep
  - queue

---
Our exim mail server has been getting a bit flakey in the past several weeks. As far as I could tell it was being caused by junk mail getting caught in the queue. After a bit of research I believe I have found a combination of solutions that seems to do the trick (at least for me)  
<!--more-->

  
First of all you can get rid of all the null senders in your queue that are older than 12 hours.  
exiqgrep -io43200 -f &#8216;^<>$&#8217; | xargs exim -Mrm  
The sender address is null if the message is a delivery failure report. This can happen from others sending as someone from your domain on an account that does not exist. (at least thats my understanding of it)

Then you can make sure all mail has an account associated with it via sender callouts. More information on sender callouts can be found below. This has been a big benefit as far as the size of my mail queue is concerned. After enabling sender verify my queue immediately dropped down to 100 from about 1800!

<a href="http://www.mbrando.com/2007/05/11/white-list-for-exim-sender-verify-callout/" mce_href="http://www.mbrando.com/2007/05/11/white-list-for-exim-sender-verify-callout/">Michael Brandonisio » White list For Exim Sender Verify Callout</a>