---
title: 'Quick Tip: Drilling into zenoss data with zendmd'
author: Nick Anderson
type: post
date: 2012-12-06T15:01:13+00:00
url: /2012/12/06/quick-tip-drilling-into-zenoss-data-with-zendmd/
categories:
  - Posts
tags:
  - devops
  - sysadmin
  - zendmd
  - zenoss

---
Sometimes you want to know what value zenoss has for something. The numbers sent in alerts seem to be the value that zenoss has, but the graphs are usually formatted to make more sense. 1394606080 might come in an alert, but on the graph it would show as 1.3 or 1.4G. It can cause some slight confusion when other people expect 90% of 1.4G instead of 90% of 1394606080 to be an alert threshold.

Any way, log in to your zenoss box as the zenoss user at a terminal and run zendmd. We will select a device, and then get a value from one of the RRDs.

<pre class="brush: plain; title: ; notranslate" title="">d = dmd.Devices.findDevice('myjavaserver')
d.getRRDValue('HeapMemory_max')

1394606080.0

</pre>

You can look up other things from here as well for example zproperties, try d.zDeviceTemplates or d.zCommandCycleTime.