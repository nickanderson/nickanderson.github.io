---
title: Archive creation fail
author: Nick Anderson
type: post
date: 2010-05-19T18:19:27+00:00
url: /2010/05/19/archive-creation-fail/
openid_comments:
  - 'a:1:{i:0;s:4:"1069";}'
categories:
  - Posts
tags:
  - emc
  - networker
  - sysadmin

---
I just downloaded EMC Networker client for a 32bit linux box. The file I downloaded was nw74sp5\_linux\_x86.tar.gz. Of course when I go to extract it &#8230;.

<pre class="brush: bash; title: ; notranslate" title=""># tar zxvf ../nw74sp5_linux_x86.tar.gz
gzip: stdin: not in gzip format
tar: Child returned status 1
tar: Error exit delayed from previous errors
</pre>

Umm not in gzip format &#8230;.

<pre class="brush: bash; title: ; notranslate" title=""># tar xvf ../nw74sp5_linux_x86.tar.gz
linux_x86/
linux_x86/lgtoclnt-7.4.5-1.i686.rpm
linux_x86/lgtolicm-7.4.5-1.i686.rpm
linux_x86/lgtoman-7.4.5-1.i686.rpm
...</pre>

🙂