---
title: Patching vmware for 2.6.24
author: Nick Anderson
type: post
date: 2008-04-09T18:45:52+00:00
url: /2008/04/09/patching-vmware-for-2624/
categories:
  - Posts
tags:
  - 2.6.42
  - patch
  - vmmon
  - vmnet
  - vmware

---
So as I previously said I have updated to Hardy Haron and along with it comes a new kernel that does not work out of the box with vmware. You need to patch your vmnet and vmmon sources to get it working again. So I went ahead and wrote a script to make the process a bit faster.<!--more-->

<!--adsense-->


  
All you need to do is download and run this script. I hope you find this helpful

[patch-vmware_2624][1]
  
Note: patch files found linked from this [blog][2].

 [1]: http://www.cmdln.org/wp-content/uploads/2008/04/patch-vmware_2624.sh
 [2]: http://igordevlog.blogspot.com/2008/03/vmware-603-in-ubuntu-hardy-804-kernel.html