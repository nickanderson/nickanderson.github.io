---
title: Purge previously uninstalled packages in debian
author: Nick Anderson
type: post
date: 2008-04-19T05:33:14+00:00
url: /2008/04/18/purge-previously-uninstalled-packages-in-debian/
categories:
  - Posts
tags:
  - cleanup
  - debian
  - purge
  - tasksel

---
Recently I ordered a server with Debian etch. Unfortunately during testing I noticed that startx was on the system, along with a whole slew of other junk that I don&#8217;t generally want on a fresh server. I wanted to remove all of the cruft but I didn&#8217;t have the exact package list.<!--more-->

<!--adsense-->


  
The solution was to run tasksel. I then saw that Desktop, Mail, and Print server were all selected. I deselected all of them but then I still had all the crufty config files lying around. Whats the best way to remove all those config files from packages you don&#8217;t exactly know were on there?

<pre class="brush: bash; title: ; notranslate" title="">aptitude purge ~c
</pre>