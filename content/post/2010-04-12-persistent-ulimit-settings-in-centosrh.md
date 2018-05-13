---
title: Persistent ulimit settings in Centos/RH
author: Nick Anderson
type: post
date: 2010-04-12T15:47:43+00:00
url: /2010/04/12/persistent-ulimit-settings-in-centosrh/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/dvKoCo
categories:
  - Posts
tags:
  - centos
  - linux
  - sysadmin
  - ulimit

---
Recently a developer came to me and said they are starting to see failed builds apparently due to open file handle limitations on the build server. In case your not aware, by default there are limitations on users to ensure they don&#8217;t hog the entire resources of a system. Sometimes these limitations need to be adjusted.

In my case the &#8220;bamboo&#8221; user needed more than 1024 open files on occasion. I determined my system had a maximum number of open files of 1572928.

<pre class="brush: bash; title: ; notranslate" title="">$ cat /proc/sys/fs/file-max
1572928
</pre>

And my bamboo user has a limit of 1024 based on the output of the ulimit -a command run as the bamboo user.

<pre class="brush: bash; title: ; notranslate" title="">$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 139264
max locked memory       (kbytes, -l) 32
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 10240
cpu time               (seconds, -t) unlimited
max user processes              (-u) 139264
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
</pre>

It seems to be an intermittent problem so I&#8217;m pretty sure just doubling the number of open files the bamboo user can have will resolve the issue. To make the change you just need to edit /etc/security/limits.conf I added new hard and soft limits by adding these lines.

<pre class="brush: bash; title: ; notranslate" title="">bamboo        hard    nofile    2048
bamboo        soft    nofile    2048
</pre>

Now lets just make sure the new limits are in place. No need to reboot just log in as the bamboo user again and run &#8220;ulimit -a&#8221;.

<pre class="brush: bash; title: ; notranslate" title="">$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 139264
max locked memory       (kbytes, -l) 32
max memory size         (kbytes, -m) unlimited
open files                      (-n) 2048
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 10240
cpu time               (seconds, -t) unlimited
max user processes              (-u) 139264
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
</pre>

As you can see open files is now 2048.