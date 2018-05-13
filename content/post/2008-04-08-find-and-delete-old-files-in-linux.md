---
title: Find and delete old files in linux
author: Nick Anderson
type: post
date: 2008-04-08T23:47:58+00:00
url: /2008/04/08/find-and-delete-old-files-in-linux/
categories:
  - Posts
tags:
  - cleanup
  - find
  - maintainance

---
I have a few of those directories that files tend to pile up in. I don&#8217;t need the files but I also don&#8217;t take the time to delete them. Pruning these old files is a good thing to keep your used disk space under control as well as your sanity. Find is a great tool to do this, its extremely flexible I recommend you read the man page next time your bored.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">find /directory/with/old/files -mtime +120 -exec rm {} \;</pre>

Here we use find to find files that are older than 120 days. The &#8220;older&#8221; here being the key word. So they might actually be older than 120 days but we are using mtime and mtime is the time when the actual contents of a file was last modified.