---
title: 'Xen installing Centos 5 domU inside debian etch dom0 with xen-tools and rinse: the patch to fix it'
author: Nick Anderson
type: post
date: 2008-04-25T18:12:51+00:00
url: /2008/04/25/xen-installing-centos-5-domu-inside-debian-etch-dom0-with-xen-tools-and-rinse-the-patch-to-fix-it/
openid_comments:
  - 'a:1:{i:0;s:3:"996";}'
categories:
  - Posts
tags:
  - centos
  - rinse
  - xen
  - xen-create-image
  - xen-tools

---
After more testing I have narrowed the issue that I left off with to a problem with the yum conf inside of the chroot.<!--more-->


  
I just got the patch working to the centos-5 postinstall script that does fix this issue. So to clarify I did add to /etc/rinse/centos-5.packages
  
Those package were
  
e2fsprogs-libs
  
authconfig

That was early in the debugging and after I found the real issue I removed those packages without causing issues.
  
So what do you need to do to bootstrap centos5 with rinse? All you need to do is apply a small patch to the post install script. Here is the patch [rinse-centos5.patch][1].

Here is how you apply it.
  
As root:

cd /usr/lib/rinse/centos-5
  
wget http://www.cmdln.org/images/wp-content/uploads/2008/04/rinse-centos5.patch
  
patch -p0 < rinse-centos5.patch [/bash] <!--adsense-->

 [1]: http://www.cmdln.org/images/wp-content/uploads/2008/04/rinse-centos5.patch
