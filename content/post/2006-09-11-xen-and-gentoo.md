---
title: Xen and Gentoo
author: Nick Anderson
type: post
date: 2006-09-11T14:12:41+00:00
url: /2006/09/11/xen-and-gentoo/
categories:
  - Posts
tags:
  - gentoo
  - tip
  - xen

---
I am in the process of setting up Xen on one of my new servers. Just sticking some notes here. Will clean them up later

`I am in the process of setting up Xen on one of my new servers. Just sticking some notes here. Will clean them up later

` No need for kernel level ip address in xen config file set ip =&#8221;off&#8221;;

DO NOT SET eth0 to start on boot! just add xend to the default runlevel it will start eth0 for you! If you dont let xen do it for you your networking in domUs will be fubar.

[backdated from old website]