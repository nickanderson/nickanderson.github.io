---
title: Analyzing linux system performance and finding bottle necks
author: Nick Anderson
type: post
date: 2008-04-14T02:29:17+00:00
url: /2008/04/13/analyzing-linux-system-performance-and-finding-bottle-necks/
categories:
  - Posts
tags:
  - blocks to megabytes
  - linux
  - performance analysis
  - sar
  - sysstat

---
System performance analytics seems to be a frequent question on forums and mailing lists. Finding out why something is slow is generally nontrivial as there are many factors to consider. I have found the sysstat package to be an invaluable tool when looking at system performance. Specifically the command sar gives a wealth of information.<!--more-->


  
<!--adsense-->


  
By default the output of sar lists CPU related information as that is generally the first place somone will look when a problem is suspected.  However it seems that the first command people run to see if there is an issue is top or uptime (to get load average). Load average is useful but it only gives you a small window into whats happening.

By default sar lists

<pre>06:30:01 PM       CPU     %user     %nice   %system   %iowait     %idle
06:40:01 PM       all      1.74      0.05      0.59      0.11     97.51
06:50:01 PM       all      1.25      0.05      0.44      0.12     98.13
07:00:01 PM       all      2.19      0.04      0.63      0.44     96.70
07:10:01 PM       all      1.62      0.05      0.47      0.16     97.69
07:20:01 PM       all      1.32      0.05      0.45      0.05     98.13
07:30:01 PM       all      1.52      0.50      0.50      0.35     97.14
07:40:01 PM       all      1.34      0.05      0.45      0.08     98.09
07:50:01 PM       all      1.48      0.05      0.46      0.12     97.89
08:00:01 PM       all      1.82      0.06      0.54      0.21     97.37
08:10:01 PM       all      1.99      0.04      0.77     14.38     82.82
08:20:01 PM       all      1.86      0.05      1.60     25.40     71.09
08:30:01 PM       all      1.16      0.66      0.46      1.24     96.47
08:40:01 PM       all      1.84      0.05      0.65      0.62     96.85
Average:          all      2.24      1.89      1.32     19.52     75.03</pre>

  * **%usr:** The percentage of time the CPU is spending on user processes, such as applications, shell scripts, or interacting with the user.
  * **%sys:** The percentage of time the CPU is spending executing kernel tasks. In this example, the number is high, because I was pulling data from the kernel&#8217;s random number generator.
  * **%wio:** The percentage of time the CPU is waiting for input or output from a block device, such as a disk.
  * **%idle:** The percentage of time the CPU isn&#8217;t doing anything useful.

The average listed is for the current log (which in most instances is the current day as its usually rotated each night.
  
<!--adsense-->


  
That information is great but thats not where sar stops. Interested in your disk statistics? Try sar -b

<pre>06:30:01 PM       tps      rtps      wtps   bread/s   bwrtn/s
06:40:01 PM      8.12      0.10      8.01      1.19    220.59
06:50:01 PM      7.82      0.23      7.58      6.64    194.37
07:00:01 PM      8.50      1.23      7.26     48.68    207.63
07:10:01 PM      8.78      0.17      8.61     12.55    228.92
07:20:01 PM      6.59      0.05      6.54      0.65    172.87
07:30:01 PM      8.89      1.25      7.64     68.27    271.07
07:40:01 PM      6.69      0.08      6.61      1.13    202.42
07:50:01 PM      8.05      0.14      7.90      2.55    203.75
08:00:01 PM      8.43      0.33      8.10      3.96    223.41
08:10:01 PM     28.80     20.36      8.44    199.77    236.51
08:20:01 PM     60.08     51.91      8.18    450.67    215.42
08:30:01 PM     12.84      5.27      7.56    298.62    409.79
08:40:01 PM      9.69      1.61      8.08     36.63    218.88
Average:        80.24     48.72     31.52   1625.75   1749.64</pre>

Report I/O and transfer rate statistics. This option works only with kernels older than 2.5. The following values are displayed:

  * **tps:** Total number of transfers per second that were issued to the physical disk. A transfer is an I/O request to the physical disk. Multiple logical requests can be combined into a single I/O request to the disk. A transfer is of indeterminate size.
  * **rtps:** Total number of read requests per second issued to the physical disk.
  * **wtps:** Total number of write requests per second issued to the physical disk.
  * **bread/s:** Total amount of data read from the drive in blocks per second. Blocks are equivalent to sectors with 2.4 kernels and newer and therefore have a size of 512 bytes. With older kernels, a block is of indeterminate size.
  *  **bwrtn/s:** Total amount of data written to the drive in blocks per second.

<!--adsense-->


  
Ok so blocks per second may not be the most intuitive way to measure something. I sure cant make sense when thinking in blocks. So this wouldn&#8217;t be a good cmdln.org article without a good command line tip. How do you convert blocks/s into something more readable like megabytes/s? Its pretty easy, all you need to do is break out your good old friend bc. You might need to install (aptitude install bc) it. Lets take the block writes/s from above 1737.20. Enter the bc shell by typing bc. Then enter scale=3 then the blocks/s / 1024. That will output megabytes per second.

<pre>$ bc
bc 1.06
Copyright 1991-1994, 1997, 1998, 2000 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
scale=3
1737.20/1024
1.696</pre>

So on that machine I have about 1.69 Megabytes/s write access to my disks. Not too bad, modern drives should be able to sustain a much higher write throughput. Its an important thing to know especially if you are venturing down the road I am with virtual machines and network based file systems to support live migration. mmmmm live migration &#8230; I love [Xen][1].

The -W switch reports swapping statistics. High paging is a sign of memory starvation. In particular, the `-w` argument shows the number of process switches: A high number can mean too many things are running on the computer, which is spending more time switching. I hope you can use this information to keep your servers running as smoothly as possible and more quickly narrow down performance issues.

 [1]: http://xen.org/ "Xen Community site"