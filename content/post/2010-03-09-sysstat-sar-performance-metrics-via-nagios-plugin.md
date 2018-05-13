---
title: Sysstat Sar Performance Metrics Via Nagios Plugin
author: Nick Anderson
type: post
date: 2010-03-09T15:42:06+00:00
url: /2010/03/09/sysstat-sar-performance-metrics-via-nagios-plugin/
syntaxhighlighter_encoded:
  - 1
categories:
  - Posts
tags:
  - cacti
  - nagios
  - sysadmin
  - sysstat
  - zenoss

---
I know I&#8217;ve mentioned how much I love the sysstat package before. I use sar regularly to help with performance diagnostics (<a title="Permanent Link to Analyzing linux system performance and finding bottle necks" rel="bookmark" href="http://www.cmdln.org/2008/04/13/analyzing-linux-system-performance-and-finding-bottle-necks/">Analyzing Linux System Performance And Finding Bottle Necks</a>, <a title="Permanent Link to CPU Performance Analysis in Linux" rel="bookmark" href="http://www.cmdln.org/2009/01/28/cpu-performance-analysis-in-linux/">CPU Performance Analysis In Linux</a>, <a title="Permanent Link to Baseline Analysis is Important, CPU Performance Analysis in Linux Revisited" rel="bookmark" href="http://www.cmdln.org/2009/01/29/baseline-analysis-is-important-cpu-performance-analysis-in-linux-revisited/">Baseline Analysis Is Important, CPU Performance Analysis In Linux Revisited</a>). I wrote this little Nagios plugin to collect the performance metrics that sar collects.

I use this plugin with Zenoss and I set any performance thresholds there, more important to me was collecting the information for historical graphing. I searched around and didn&#8217;t really find any existing solutions thats why anyone wanting to do similar perhaps with cacti is stuck with my craptastic code (or please point me to a better implementation).  Anyway if you want to grab the plugin and check it out its on github.

[check\_sar\_perf][1]

 [1]: http://github.com/nickanderson/check-sar-perf