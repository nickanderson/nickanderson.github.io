---
title: Cpanel WHM inside Centos 5.1 domU
author: Nick Anderson
type: post
date: 2008-05-02T00:19:53+00:00
url: /2008/05/01/cpanel-whm-inside-centos-51-domu/
categories:
  - Posts
tags:
  - Add new tag
  - centos
  - cpanel
  - rinse
  - xen-tools

---
I needed to install cpanel inside of one of my Centos 5.1 domU. The centos install was bootstrapped by the default rinse configuration (see [xen-tools][1] with my [patch][2] that you can see from a [previous post][3]). If you follow the [install docs][4] you will have tried to uninstall openldap etc &#8230;.<!--more-->

<!--adsense-->

I can tell you from experience don&#8217;t even try. The install docs are not that great. All you need to do (if you have bootstrapped with rinse) is install a few packages so that the cpanel installer can complete successfully. I had to install tar, gzip, wget, and perl. The error that I got when first trying to install was related to uncompressing. I contacted Cpanel about the issue and one of their techs logged into my vm to see what was going on. All we did was install the above packages then run the installer. We did not remove any other packages, and I have yet to have an issue (granted its been hours, and it is cpanel, so I expect something to rear its ugly head). But if anyone else is trying to get cpanel installed on a fresh xen-create-image with rinse and centos 5.1 is having issues try installing the above packages before doing anything else to your system and see how you fair.

 [1]: http://www.xen-tools.org/software/xen-tools/
 [2]: http://www.cmdln.org/wp-content/uploads/2008/04/rinse-centos5.patch
 [3]: http://www.cmdln.org/2008/04/25/xen-installing-centos-5-domu-inside-debian-etch-dom0-with-xen-tools-and-rinse-the-patch-to-fix-it/
 [4]: http://www.cpanel.net/docs/vps/