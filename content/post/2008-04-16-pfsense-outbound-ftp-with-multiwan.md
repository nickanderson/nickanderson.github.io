---
title: Pfsense outbound ftp with multiwan
author: Nick Anderson
type: post
date: 2008-04-16T23:19:00+00:00
url: /2008/04/16/pfsense-outbound-ftp-with-multiwan/
openid_comments:
  - 'a:1:{i:0;s:4:"1118";}'
categories:
  - Posts
tags:
  - firewall
  - ftp
  - pfsense

---
If you use multiwan with pfsense and like me you have issues making outbound ftp connections try disabling the userland FTP-Proxy application on the LAN interface. It may stop you from being able to do active ftp connections but at least you can use ftp. With it enabled I was unable to make any outbound ftp connections active or passive.