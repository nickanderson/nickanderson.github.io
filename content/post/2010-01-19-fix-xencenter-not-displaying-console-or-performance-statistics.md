---
title: Fix XenCenter not displaying console or performance statistics
author: Nick Anderson
type: post
date: 2010-01-19T18:07:28+00:00
url: /2010/01/19/fix-xencenter-not-displaying-console-or-performance-statistics/
syntaxhighlighter_encoded:
  - 1
categories:
  - Posts
tags:
  - citrix
  - virtualization
  - xen
  - XenCenter
  - XenServer

---
I am sure you are aware of my affinity for the Xen hypervisor. In the last year I have switched over to Citrix Xenserver. With other people managing VMs as well having a nice GUI is helpful. One of my complaints is that the GUI (XenCenter) is a windows only app. C&#8217;mon, Citrix, please release a cross platform management console. I&#8217;ve got to run a windows VM just to use the GUI (granted I don&#8217;t have to use the gui, there is a nice API and console utilities). At any rate today I noticed that I could no longer pull up the console for a windows VM nor could I pull up the performance metrics available in XenCenter. A few searches turned up [Kenneth Hunts blog][1] and a post that showed me where to fix it. <!--more-->The windows box running XenCenter has a cache folder located in %AppData%\Citrix\XenCenterMain.exe\_Url\_xxxxxxxxxx. If you remove the cache you should be able to see the console and performance graphs again. If by chance you remove the entire folder you will need to re-add all dom0s back into XenCenter.

 [1]: http://kennethhunt.com