---
title: Testing mail servers with swaks
author: Nick Anderson
type: post
date: 2009-04-16T17:45:43+00:00
url: /2009/04/16/testing-mail-servers-with-swaks/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - command line
  - email
  - testing

---
I hadn&#8217;t seen this tool before so I figured I would share. [Swaks is the swiss army knife SMTP][1] according to the homepage.

I&#8217;ve covered [testing email from the command line][2] before but this tool sure makes it easier.

<pre class="brush: php; title: ; notranslate" title="">swaks --to nick@tld --from nick@tld
*** MX Routing not available: requires Net::DNS.  Using localhost as mail server
=== Trying localhost:25...
=== Connected to localhost.
&lt;-  220 cmdln-laptop ESMTP Exim 4.69 Thu, 16 Apr 2009 12:23:24 -0500
 -&gt; EHLO cmdln-laptop
&lt;-  250-cmdln-laptop Hello localhost [127.0.0.1]
&lt;-  250-SIZE 52428800
&lt;-  250-PIPELINING
&lt;-  250 HELP
 -&gt; MAIL FROM:&lt;nick@tld&gt;
&lt;-  250 OK
 -&gt; RCPT TO:&lt;nick@tld&gt;
&lt;-  250 Accepted
 -&gt; DATA
&lt;-  354 Enter message, ending with &quot;.&quot; on a line by itself
 -&gt; Date: Thu, 16 Apr 2009 12:23:24 -0500
 -&gt; To: nick@tld
 -&gt; From: nick@tld
 -&gt; Subject: test Thu, 16 Apr 2009 12:23:24 -0500
 -&gt; X-Mailer: swaks v20061116.0 jetmore.org/john/code/#swaks
 -&gt; 
 -&gt; This is a test mailing
 -&gt; 
 -&gt; .
&lt;-  250 OK id=1LuVJ6-0007ge-Jf
 -&gt; QUIT
&lt;-  221 cmdln-laptop closing connection
=== Connection closed with remote host.
</pre>

 [1]: http://www.jetmore.org/john/code/#swaks
 [2]: http://www.cmdln.org/2008/04/06/testing-email-manually-with-telnet-spoofing-email/