---
title: Xen installing Centos 5 domU inside debian etch dom0 with xen-tools and rinse
author: Nick Anderson
type: post
date: 2008-04-25T13:27:59+00:00
url: /2008/04/25/xen-installing-centos-5-domu-inside-debian-etch-dom0-with-xen-tools-and-rinse/
categories:
  - Posts
tags:
  - bootstrap
  - centos 5
  - rinse
  - xen
  - xen-create-image

---
At work I am just beginning the process of migrating from a hosted dedicated server to a Xen instance on a new server we have. Our dedicated server runs centos, and has WHM cpanel installed. So I figured it would be a good thing to have cpanel again as several people are familiar with it, and we do host a few random websites for people still. Cpanel does not support debian to my knowledge so Centos 5 sounds like the best way to go.<!--more-->

<!--adsense-->Centos 5 is supported by a newer xen-tools package than what is provided in etch so I added /etc/apt/sources.list.d/xen-tools.list with the content 

<pre class="brush: bash; title: ; notranslate" title="">#
#  Steve Kemp's repository:  Etch
#
deb     http://apt.steve.org.uk/etch etch main non-free contrib
deb-src http://apt.steve.org.uk/etch etch main non-free contrib
</pre>

Once that was done a simple aptitude update and aptitude dist-upgrade updated xen-tools to a newer version.
  
There is a new tool called rinse that can bootstrap rpm based distros like centos and fedora. Since I want a centos 5 domu I issue the xen-create-image with the following command

<pre class="brush: bash; title: ; notranslate" title="">xen-create-image --hostname centos5_domU --ip 192.168.1.50 --install-method rinse  --force --dist centos-5 --arch=amd64
</pre>

No errors with the command so everything looks ok, try booting the guest vm up with 

<pre class="brush: bash; title: ; notranslate" title="">xm create centos5_domU.cfg -c
</pre>

uh oh, something went wrong, the domU would not finish booting checkout the output

<pre class="brush: plain; title: ; notranslate" title="">INIT: version 2.86 booting
mount: error while loading shared libraries: libblkid.so.1: cannot open shared object file:No such file or directory
/etc/rc.d/rc.sysinit: line 31: /etc/init.d/functions: No such file or directory
/etc/rc.d/rc.sysinit: line 34: fstab_decode_str: command not found
                Welcome to  CentOS release 5 (Final)
                Press 'I' to enter interactive startup.
/etc/rc.d/rc.sysinit: line 265: update_boot_stage: command not found
Cannot access the Hardware Clock via any known method.
Use the --debug option to see the details of our search for an access method.
/etc/rc.d/rc.sysinit: line 301: action: command not found
/etc/rc.d/rc.sysinit: line 314: strstr: command not found
/etc/rc.d/rc.sysinit: line 326: strstr: command not found
/sbin/start_udev: line 36: /etc/init.d/functions: No such file or directory
Non-volatile memory driver v1.2
Floppy drive(s): fd0 is unknown type 15 (usb?), fd1 is unknown type 15 (usb?)
Failed to obtain physical IRQ 6
floppy0: no floppy controllers found
lp: driver loaded but no devices found
/etc/rc.d/rc.sysinit: line 356: strstr: command not found
/etc/rc.d/rc.sysinit: line 362: update_boot_stage: command not found
/etc/rc.d/rc.sysinit: line 395: update_boot_stage: command not found
/etc/rc.d/rc.sysinit: line 396: action: command not found
/etc/rc.d/rc.sysinit: line 408: update_boot_stage: command not found
/etc/rc.d/rc.sysinit: line 432: strstr: command not found
/etc/rc.d/rc.sysinit: line 441: strstr: command not found
/etc/rc.d/rc.sysinit: line 458: strstr: command not found
/etc/rc.d/rc.sysinit: line 466: strstr: command not found
/etc/rc.d/rc.sysinit: line 495: strstr: command not found
/etc/rc.d/rc.sysinit: line 499: strstr: command not found
/etc/rc.d/rc.sysinit: line 623: strstr: command not found
Checking filesystems
fsck: error while loading shared libraries: libblkid.so.1: cannot open shared object file: No such file or directory
/etc/rc.d/rc.sysinit: line 657: failure: command not found


*** An error occurred during the file system check.
*** Dropping you to a shell; the system will reboot
*** when you leave the shell.
Give root password for maintenance
(or type Control-D to continue):
</pre>

Now what? Well we start debugging. I quickly tried creating a centos4 domU the same way, and it booted without issue. So there must be somethng wrong with the creation of the centos5 domU. Since its bootstrapped with rinse thats a good place to start.
  
<!--adsense-->


  
A quick glance at man rinse show us how to use rinse by itself. So lets try bootstrapping a centos 5.

<pre class="brush: bash; title: ; notranslate" title="">rinse --distribution centos-5 --directory=/tmp/centos-test --arch=amd64
</pre>

and by looking at the [rinse output][1]
  
we can see that indeed our problem is bootstrapping with rinse.
  
&#8230;. and the debugging continues

 [1]: http://www.cmdln.org/images/wp-content/uploads/2008/04/rinse.log
