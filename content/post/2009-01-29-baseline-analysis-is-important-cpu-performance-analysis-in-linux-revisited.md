---
title: Baseline Analysis is Important, CPU Performance Analysis in Linux Revisited
author: Nick Anderson
type: post
date: 2009-01-30T03:34:39+00:00
url: /2009/01/29/baseline-analysis-is-important-cpu-performance-analysis-in-linux-revisited/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - followup
  - performance analysis
  - sar
  - sysstat

---
Yesterday I wrote about <a href=http://www.cmdln.org/2009/01/28/cpu-performance-analysis-in-linux/>CPU Performance Analysis in Linux</a>. I explained how to tell if you are experiencing a CPU bottleneck. This is just a quick followup to show the effect of adding more cpu power. <!--more-->

Since this is a virtual machine it is easy to just drop in another cpu. This is the CPU utilization report from the machine at the time of the analysis.

<pre class="brush: bash; title: ; notranslate" title="">07:55:01 AM       CPU     %user     %nice   %system   %iowait    %steal     %idle
08:05:01 AM       all      3.95      0.00      2.22      0.13      0.00     93.70
08:15:01 AM       all      4.32      0.00      2.37      0.08      0.00     93.23
08:25:01 AM       all      5.70      0.00      2.79      0.06      0.00     91.44
08:35:01 AM       all      6.13      0.00      3.85      0.07      0.00     89.94
08:45:01 AM       all     10.27      0.00      6.07      0.09      0.00     83.56
08:55:01 AM       all     13.50      0.00      8.15      0.21      0.00     78.14
09:05:01 AM       all     14.53      0.00     10.39      0.30      0.00     74.78
09:15:01 AM       all     12.24      0.00      9.02      0.44      0.00     78.30
09:25:01 AM       all     12.66      0.00      8.80      0.50      0.00     78.03
09:35:01 AM       all     12.67      0.00      9.43      0.49      0.00     77.40
09:45:01 AM       all     13.51      0.00      9.62      0.44      0.00     76.43
09:55:01 AM       all     13.67      0.00     10.66      0.59      0.00     75.08
10:05:01 AM       all     14.47      0.00     10.99      0.66      0.00     73.88
10:15:01 AM       all     12.32      0.00      9.15      0.44      0.00     78.09
10:25:01 AM       all     25.71      0.00     14.17      0.51      0.00     59.61
10:35:01 AM       all     13.65      0.00     10.04      1.30      0.00     75.01
10:45:01 AM       all     12.36      0.00      8.86      0.65      0.00     78.12
10:55:03 AM       all     25.34      0.00     19.41      0.56      0.00     54.69
11:05:01 AM       all     24.10      0.00     19.04      0.67      0.00     56.19
11:15:01 AM       all     16.63      0.00     12.51      0.60      0.00     70.26
11:25:01 AM       all     25.83      0.00     22.10      1.73      0.00     50.34
11:35:01 AM       all     22.80      0.00     16.90      1.06      0.00     59.24
11:45:01 AM       all     31.48      0.00     21.74      1.08      0.00     45.69
11:55:01 AM       all     18.10      0.00     13.53      0.82      0.00     67.55
12:05:02 PM       all     19.07      0.00     14.74      0.94      0.00     65.26
12:15:01 PM       all     20.48      0.00     16.32      1.00      0.00     62.19
12:25:01 PM       all     23.83      0.00     20.03      0.80      0.00     55.33
12:35:01 PM       all     22.97      0.00     18.57      1.43      0.00     57.03
12:45:02 PM       all     25.65      0.00     20.55      0.67      0.00     53.12
</pre>

This is the CPU uitilization report today after having added another cpu to the virtual machine.

<pre class="brush: bash; title: ; notranslate" title="">07:55:01 AM       CPU     %user     %nice   %system   %iowait    %steal     %idle
08:05:01 AM       all      4.08      0.00      1.86      0.11      0.00     93.95
08:15:01 AM       all      5.67      0.00      2.31      0.10      0.00     91.92
08:25:01 AM       all     12.51      0.00      2.94      0.13      0.00     84.42
08:35:01 AM       all      7.21      0.00      2.74      0.12      0.00     89.93
08:45:01 AM       all     10.87      0.00      3.78      0.41      0.00     84.94
08:55:01 AM       all      8.41      0.00      3.58      0.13      0.00     87.88
09:05:01 AM       all     10.49      0.00      3.00      0.09      0.00     86.42
09:15:01 AM       all      5.21      0.00      2.23      0.09      0.00     92.47
09:25:01 AM       all      5.92      0.00      2.48      0.08      0.00     91.52
09:35:01 AM       all      5.79      0.00      2.57      0.13      0.00     91.52
09:45:01 AM       all      7.62      0.00      3.30      0.13      0.00     88.95
09:55:01 AM       all      9.07      0.00      4.00      0.11      0.00     86.82
10:05:01 AM       all      8.34      0.00      4.01      0.19      0.00     87.47
10:15:01 AM       all      9.16      0.00      3.74      0.17      0.00     86.92
10:25:01 AM       all      7.31      0.00      3.25      0.09      0.00     89.35
10:35:01 AM       all      7.88      0.00      3.38      0.09      0.00     88.65
10:45:01 AM       all      9.93      0.00      4.04      0.08      0.00     85.95
10:55:01 AM       all      9.98      0.00      3.84      0.07      0.00     86.11
11:05:01 AM       all      8.67      0.00      3.54      0.05      0.00     87.74
11:15:01 AM       all     11.05      0.00      4.60      0.05      0.00     84.30
11:25:01 AM       all     13.94      0.00      3.97      0.42      0.00     81.67
11:35:01 AM       all     10.69      0.00      4.22      0.45      0.00     84.64
11:45:01 AM       all      8.26      0.00      3.58      0.06      0.00     88.11
11:55:02 AM       all      7.44      0.00      3.14      0.03      0.00     89.39
12:05:01 PM       all      7.43      0.00      3.60      0.07      0.00     88.89
12:15:01 PM       all      6.55      0.00      2.91      0.03      0.00     90.50
12:25:01 PM       all      6.95      0.00      3.01      0.12      0.00     89.92
12:35:01 PM       all      8.48      0.00      3.55      0.20      0.00     87.77
12:45:01 PM       all     10.39      0.00      3.74      0.04      0.00     85.83
</pre>

As you can see the idle time is consistently higher while system and user times are consistently lower. Granted these reports are from different days but the activity on the server was similar for both days and time periods.

I hope this helps show how you can determine if your server is cpu bound and as the title says, baseline analysis is important. Always go back and verrify changes you have made had the impact you intended.