---
title: ctime, atime, and mtime
author: Nick Anderson
type: post
date: 2008-04-07T23:16:44+00:00
url: /2008/04/07/ctime-atime-and-mtime/
categories:
  - Posts
tags:
  - atime
  - ctime
  - file times
  - linux times
  - mtime
  - unix times

---
It is important to distinguish between a file or directory&#8217;s change time (ctime), access time (atime), and modify time (mtime).<!--more-->

<!--adsense-->

**ctime** &#8212; In UNIX, it is not possible to tell the actual creation time of a file. The ctime&#8211;change time&#8211;is the time when changes were made to the file or directory&#8217;s inode (owner, permissions, etc.). It is needed by the dump command to determine if the file needs to be backed up. You can view the ctime with the ls -lc command.
  
**atime** &#8212; The atime&#8211;access time&#8211;is the time when the data of a file was last accessed. Displaying the contents of a file or executing a shell script will update a file&#8217;s atime, for example. You can view the atime with the ls -lu command.
  
**mtime** &#8212; The mtime&#8211;modify time&#8211;is the time when the actual contents of a file was last modified. This is the time displayed in a long directory listing (ls -l).