---
title: Monitoring A/B PDU Load with Zenoss
author: Nick Anderson
type: post
date: 2010-06-13T01:19:18+00:00
url: /2010/06/12/monitoring-ab-pdu-load-with-zenoss/
openid_comments:
  - 'a:1:{i:0;s:4:"1095";}'
categories:
  - Posts
tags:
  - zenoss

---
Redundant power is a necessity for any highly available system. Most servers have redundant power supplies and the common design pattern is to have each power supply plugged into a power distribution units that are on separate circuits. One challenge with this type of dealing with this type of design is monitoring the power load.

Monitoring A/B power is not as easy as monitoring the individual PDUs. Some servers will draw power from both power supplies, other will draw from one or the other. That being the case the circuits are almost never all or nothing, and they are almost never perfectly balanced. In order to effectively monitor the whole picture you need to monitor the aggregate power consumption of both circuits.

I&#8217;ve not really seen direct support in any Network Monitoring System that I have ever looked at. Zenoss is the NMS I have been using recently and while it has many rules for alerting it does not support alerts based on multiple data points. To solve my issue I ended up writing a small script that would query the SNMP OID for the total power load on a single PDU for two specified hosts and return the aggregate as well as the individual PDU loads in Nagios plugin format. That gave me a single data point that I could use for thresholds and alerts.

I have created a ZenPack that includes the script as well as the templates for graphing and thresholds. The thresholds and graphs are specific to a 20A circuit but could easily be modified for others.

The aggregateAPCpduAB ZenPack can be found on my github profile.

<http://github.com/nickanderson/ZenPacks.community.aggregateAPCpduAB>