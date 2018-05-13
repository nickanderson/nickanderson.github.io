---
title: Console sharing without setuid gnu screen
author: Nick Anderson
type: post
date: 2008-08-25T21:34:33+00:00
url: /2008/08/25/console-sharing-without-setuid-gnu-screen/
categories:
  - Posts
tags:
  - kibitz
  - screen
  - shared console

---
I mentioned in my last post [Shared console sessions][1] that I would have an update to get near same functionality without setuid of the screen binary. Well here it is. Hopefully you are aware of expect and how it can be used to automate interactive programs like telnet. Expect is has many more uses that people are exploiting. Enter kibitz. <!--more-->


  
Kibitz allows two (or more) people to interact with one shell. Kibitz comes along buried in the examples of expect (in Debian see package libexpect-perl). Its fairly easy to use but one note any person expecting to use it should have messaging enabled as it also uses talk.

`mesg y`

To initiate a shared session just run 

`/usr/share/doc/libexpect-perl/examples/kibitz user`

where user is the user that you would like to share a session with. Kibitz will then prompt that user to run a kibitz command that will connect them to the shared session.

 [1]: http://www.cmdln.org/2008/08/13/shared-console-sessions/