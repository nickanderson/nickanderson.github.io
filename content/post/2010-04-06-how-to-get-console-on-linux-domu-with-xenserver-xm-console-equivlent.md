---
title: How to get console on linux domU with XenServer (xm console equivlent)
author: Nick Anderson
type: post
date: 2010-04-06T17:53:36+00:00
url: /2010/04/06/how-to-get-console-on-linux-domu-with-xenserver-xm-console-equivlent/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/a9GfdL
categories:
  - Posts
tags:
  - cli
  - sysadmin
  - XenServer

---
Besides the gui/vnc consoles you can still use the equivlent of xm console in Citrix XenServer.

On the host console:

  * xe vm-list to get the list of domins running (just note the uuid of the domain you want).
  * list\_domains will list the domain name and the uuid of the domains. Match up your uuid so you get the proper dom\_id
  * xm console equivlent is /usr/lib/xen/bin/xenconsole dom_id

Its not in the root users $PATH though I think it ought to be. Of course you can symlink it or alter your path yourself but it would be a sensible default.

Example:

xen01 = dom0

knox = linuxpv domU

Say I want to connect to knox (a linux domU)

<pre class="brush: bash; title: ; notranslate" title="">[root@xen01 ~]# xe vm-list
uuid ( RO)           : 8258a6d4-23f6-003d-30d7-65bd13086863
name-label ( RW): knox
power-state ( RO): running

uuid ( RO)           : 1a191475-a99d-7a77-6550-b30a0038fd92
name-label ( RW): Windows Server 2008 SP2 x86
power-state ( RO): halted

uuid ( RO)           : ffd95724-d818-4f15-b4b4-159b7ff41df4
name-label ( RW): Control domain on host: xen01
power-state ( RO): running
</pre>

Now get domain ids

<pre class="brush: bash; title: ; notranslate" title="">[root@xen01 ~]# list_domains
id |                                 uuid |  state
0 | ffd95724-d818-4f15-b4b4-159b7ff41df4 |     R
1 | bc150966-8c21-7ad9-c329-839d5823041d |    B H
7 | baa3699b-95dd-eea0-ccc4-51e8972857f5 |    B
11 | 8258a6d4-23f6-003d-30d7-65bd13086863 |    B
</pre>

You can see the domain ID that matches the UUID of knox is 11. So we use xenconsole.

<pre class="brush: bash; title: ; notranslate" title="">[root@xen01 ~]# /usr/lib/xen/bin/xenconsole 11
(press enter)
You have new mail in /var/spool/mail/root
[root@knox ~]#
</pre>

`Besides the gui/vnc consoles you can still use the equivlent of xm console in Citrix XenServer.

On the host console:

  * xe vm-list to get the list of domins running (just note the uuid of the domain you want).
  * list\_domains will list the domain name and the uuid of the domains. Match up your uuid so you get the proper dom\_id
  * xm console equivlent is /usr/lib/xen/bin/xenconsole dom_id

Its not in the root users $PATH though I think it ought to be. Of course you can symlink it or alter your path yourself but it would be a sensible default.

Example:

xen01 = dom0

knox = linuxpv domU

Say I want to connect to knox (a linux domU)

<pre class="brush: bash; title: ; notranslate" title="">[root@xen01 ~]# xe vm-list
uuid ( RO)           : 8258a6d4-23f6-003d-30d7-65bd13086863
name-label ( RW): knox
power-state ( RO): running

uuid ( RO)           : 1a191475-a99d-7a77-6550-b30a0038fd92
name-label ( RW): Windows Server 2008 SP2 x86
power-state ( RO): halted

uuid ( RO)           : ffd95724-d818-4f15-b4b4-159b7ff41df4
name-label ( RW): Control domain on host: xen01
power-state ( RO): running
</pre>

Now get domain ids

<pre class="brush: bash; title: ; notranslate" title="">[root@xen01 ~]# list_domains
id |                                 uuid |  state
0 | ffd95724-d818-4f15-b4b4-159b7ff41df4 |     R
1 | bc150966-8c21-7ad9-c329-839d5823041d |    B H
7 | baa3699b-95dd-eea0-ccc4-51e8972857f5 |    B
11 | 8258a6d4-23f6-003d-30d7-65bd13086863 |    B
</pre>

You can see the domain ID that matches the UUID of knox is 11. So we use xenconsole.

<pre class="brush: bash; title: ; notranslate" title="">[root@xen01 ~]# /usr/lib/xen/bin/xenconsole 11
(press enter)
You have new mail in /var/spool/mail/root
[root@knox ~]#
</pre>

`