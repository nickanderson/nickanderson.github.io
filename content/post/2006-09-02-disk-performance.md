---
title: Disk Performance
author: Nick Anderson
type: post
date: 2006-09-02T14:05:38+00:00
url: /2006/09/02/disk-performance/
categories:
  - Posts
tags:
  - 3ware
  - hardware
  - performance
  - raid

---
So what kind of performance should people expect from a disk or raid?

How long should it take to create 100G file?

`time dd if=/dev/zero of=mako1 bs=65536 count=163840`

A customer of ours is using this to create a 10G file and its taking about 20 minutes to create the file on a 12 drive raid 5 with 3ware. After setting ra again (in case the customer did not) and I got about 18 minutes on the same command.

The customer says we should be able to create that file in about 10-20 seconds. ref (http://t2.unl.edu/ce-changelog/dcache04-performance)

[backdated article from old website]