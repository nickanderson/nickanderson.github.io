---
title: 'Error Msg Fail: How to enable telnet on centos/rhel'
author: Nick Anderson
type: post
date: 2010-04-06T14:46:30+00:00
url: /2010/04/06/error-msg-fail-how-to-enable-telnet-on-centosrhel/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/dnEv7N
categories:
  - Posts
tags:
  - centos
  - linux
  - sysadmin
  - telnet

---
Don&#8217;t even start with me about how telnet is horrid. Out side of my control but I recently had issues trying to enable telnet on a server. Typically its pretty straightforward.

  1. yum install telnet-server
  2. chkconfig telnet on
  3. chkconfig xinetd on
  4. service xinetd start

Unfortunately for me this was not working. Every time I tried to telnet to the host after enabling it I would get an error message.

<pre class="brush: bash; title: ; notranslate" title="">telnet host
Trying 203.0.113.10...
Connected to host (203.0.113.10).
Escape character is '^]'.
getaddrinfo: localhost Name or service not known
Connection closed by foreign host.
</pre>

I tried everything I could think of, selinux disabled, ensure localhost in /etc/hosts, connect to ip instead of hostname. Nothing was working. All of my searching was just turning up the obligatory &#8220;Don&#8217;t use telnet, use ssh&#8221;.

While that is generally good advice, in the event you are restricted to using telnet it&#8217;s not very helpful. Obviously is something related to name resolution. From both sides the fqdn was resolvable. Then it dawned on me. This environment also has the standard of not using the fqdn as the hostname as set in /etc/sysconfig/network. I had not ensured that the shorthand hostname was resolvable. I resolved the error by adding the hostname in /etc/hosts, but adding a default search domain in /etc/resolv.conf would work just as well.

This leads me back to the error message. Really it had nothing to do with &#8220;localhost&#8221; or &#8220;127.0.0.1&#8221;. Had it said &#8220;host&#8221; Name or service not known I would have chased down the issue much sooner.

[My ServerFault plea for help][1]

 [1]: http://serverfault.com/questions/129556/how-do-i-fix-getaddrinfo-localhost-name-or-service-not-found-for-telnet-server/129764#129764