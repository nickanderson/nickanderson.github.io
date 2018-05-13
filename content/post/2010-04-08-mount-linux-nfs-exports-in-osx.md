---
title: Mount Linux NFS exports in OSX
author: Nick Anderson
type: post
date: 2010-04-08T17:36:17+00:00
url: /2010/04/08/mount-linux-nfs-exports-in-osx/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/dbiVas
categories:
  - Posts
tags:
  - linux
  - nfs
  - osx
  - sysadmin

---
I&#8217;m not a fan of OSX and I try to avoid it with the same veracity that I avoid Windows. But I recently needed to have a Linux NFS export mounted on an OSX server. A simple mount server:/export /mymountpoint didn&#8217;t work and returned &#8220;Operation not permitted&#8221;. After a bit of digging I found the solution.

I needed to instruct the client to use a privledged port by adding the &#8220;-P&#8221; option.

<pre class="brush: bash; title: ; notranslate" title="">mount -o -P nfssrv:/export /mymount
</pre>

Now to make it persistent of course its not as simple as shoving it in /etc/fstab and running &#8220;mount -a&#8221;. No OSX has to be difficult. It turned out lookupd got in the way.  To fix it I did the following after configuring my fstab.

<pre class="brush: bash; title: ; notranslate" title="">mkdir /etc/lookupd
echo "LookupOrder Cache NI FF" &gt;&gt; /etc/lookupd/mounts
kill -HUP `cat /var/run/lookupd.pid`
mount -a
</pre>

Yay that should have mounted your NFS mount and have it be persistent.