---
title: Infrastructure monitoring with Zabbix
author: Nick Anderson
type: post
date: 2008-02-08T23:01:17+00:00
url: /2008/02/08/infrastructure-monitoring-with-zabbix/
openid_comments:
  - 'a:1:{i:0;s:4:"1044";}'
categories:
  - Posts
tags:
  - monitoring
  - self-healing
  - zabbix

---
[Zabbix][1] is an opensource network monitoring application somewhat akin to [Nagios][2] and [Cacti][3]. I have been using Zabbix for about 8 months, and I am pleased with its results.
  
<!--more-->


  
<!--adsense-->


  
It is an easy application to install and use. In fact I will be posting a howto in the near future. The most powerful thing I think zabbix has going for it is its template structure. It is easy to create a template (time consuming but easy). Zabbix even provides some common templates for you to build on. Rather than build on their standard linux template I stripped it down to a minimal linux template that all of my linux servers have in common. Then I created templates for common stacks that reside on a server. For example a MySQL template and an Apache2 template. I differentiated Apache2 from Apache 1.3 because it affects a process that I look for. Zabbix can also notify you when trigger are set off. Notifications are done in the form of an action. Currently SMS, email, and external script actions are available. This even makes it possible to have a trigger for self recovery if you so choose. I have not looked into a self-healing system yet but its on my list of things to do. Puppet may also have the ability to fill the self-healing role.

 [1]: www.zabbix.com
 [2]: http://www.nagios.org/
 [3]: http://www.cacti.net