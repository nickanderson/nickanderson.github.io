---
title: Bind Stats in Centos/RHEL5
author: Nick Anderson
type: post
date: 2010-08-02T16:21:42+00:00
url: /2010/08/02/bind-stats-in-centosrhel5/
categories:
  - Posts
tags:
  - bind
  - named
  - stats
  - sysadmin

---
Just a little tip, if your looking for bind stats and your chrooted 

<pre class="brush: plain; title: ; notranslate" title="">rndc stats</pre>

will give you 

<pre class="brush: plain; title: ; notranslate" title="">rndc: 'stats' failed: permission denied</pre>

All you have to do is 

<pre class="brush: plain; title: ; notranslate" title="">touch /var/named/chroot/var/named/named.stats
chown named:named /var/named/chroot/var/named/named.stats</pre>

Now after you run rndc stats your named.stats fill will be populated with information.