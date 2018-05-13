---
title: Nginx stub_status Zenpack
author: Nick Anderson
type: post
date: 2010-07-09T23:41:53+00:00
url: /2010/07/09/nginx-stub_status-zenpack/
openid_comments:
  - 'a:1:{i:0;s:4:"1092";}'
categories:
  - Posts
tags:
  - nginx
  - sysadmin
  - zenoss
  - zenpack

---
Nginx is a great little web server. I have posted previously about using it as a reverse proxy. Weather your using it as a reverse proxy or as a normal webserver you will probably eventually want to know what its doing over time so you can adjust resources as necessary.

The other day I threw together a Zenpack to make it easier to setup monitoring on new Zenoss instances. It contains a command data source &#8220;check\_nginx\_ng&#8221; which is a slightly modified version of [Chris Kellys][1] [check\_nginx\_ng][2] which in turn was based on [check_nginx][3] by [Mike Adolphs][4]. So thanks to them for doing the majority of the work! If your interested you can pick it up over on github. **[ZenPacks.community.NginxStatus][5]**

 [1]: http://ckdake.com
 [2]: http://ckdake.com/content/2009/monitoring-nginx-with-zenoss.html
 [3]: http://exchange.nagios.org/directory/Plugins/Web-Servers/nginx/check_nginx-2Esh/details
 [4]: http://www.matejunkie.com/
 [5]: http://github.com/nickanderson/ZenPacks.community.NginxStatus/tree/master