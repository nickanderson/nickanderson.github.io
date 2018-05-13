---
title: 'XenServer License Check &#8211; Nagios NRPE Plugin'
author: Nick Anderson
type: post
date: 2010-03-08T14:51:23+00:00
url: /2010/03/08/xenserver-license-check-nagios-nrpe-plugin/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/ckq5DT
openid_comments:
  - 'a:1:{i:0;s:4:"1170";}'
categories:
  - Posts
tags:
  - nagios
  - nrpe
  - sysadmin
  - XenServer

---
If you hadn&#8217;t already guessed I am a big fan of the Xen hypervisor. Lately I have been using the Citrix XenServer release because it makes it quite palatable for my co-workers. One annoyance that I do have about XenServer is the requirement that you license it (with a free license) every year. If you fail to license it the GUI stops working. Now I hate relying on GUIs but the fact of the matter is others in my team expect to have a working GUI when they need to do something. And I dont know about you but I don&#8217;t really log onto the management console very often. Really I only log on to it if I need to provision a new server so its entirely plausible that a license would expire and I wouldn&#8217;t know about it until I really needed to do something.

I ended up writing a little Nagios plugin that checks the license expiration date using XenAPI. I don&#8217;t know that it&#8217;s 100% compliant with the plugin specification but it does work for me. I actually don&#8217;t prefer to use the warn and critical states with the Nagios (I use the performance data with Zenoss and apply thresholds there. I find that to be a bit more flexible.) but I did implement them. The plugin can be executed on the XenServer (you may want to reference [how to install nrpe on XenServer][1]) or on from your monitoring host as long as the host performing the check has the python XenAPI installed.

The plugin [check\_citrix\_xenserver_license can be found on github][2].

I hope someone can find it useful.

 [1]: http://www.cmdln.org/2010/03/04/installing-nrpe-on-xenserver/
 [2]: https://github.com/nickanderson/nagios-plugins-check_xs-license