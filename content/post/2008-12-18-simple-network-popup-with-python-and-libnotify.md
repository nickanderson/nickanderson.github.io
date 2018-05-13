---
title: Simple network popup with python and libnotify
author: Nick Anderson
type: post
date: 2008-12-18T15:13:55+00:00
url: /2008/12/18/simple-network-popup-with-python-and-libnotify/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - python

---
Im sure everyone is familiar with smb messages especially as everyone was assulted with them about 10 years ago (stupid soho routers and spammers unite!). Anyway, there are clients for linux like Linpopup. Well recently I didn&#8217;t want to use one of those to be able to send messages to my linux workstations so I cobbled together a simple network popup app with python. <!--more-->


  
It&#8217;s really simple and I can not take credit for the original multicast code though I did slightly tweak it. Most of this was taken directly from Jason R. Briggs http://www.briggs.net.nz/log/2006/05/28/python-multicast/.

Useage is simple enough. (I called this msgcast)
  
msgcast server to start the server, msgcast all some msg goes here, or msgcast hostname some msg goes here.

Enjoy, don&#8217;t bitch about my python skills I never claimed to be a programmer so eat it!

<pre class="brush: python; title: ; notranslate" title="">#!/usr/bin/env python
# Author: Nick Anderson
# http://www.cmdln.org
#
import socket
import struct
import sys
import pynotify

__multicast_network__ = '225.100.100.100'
__port__ = 6388
__version__ = 'unworthy of version number'

if __name__ == '__main__':
	pynotify.init('MsgNotification')
	Title = &quot;Notification&quot;
	if sys.argv[1] == 'server':
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('', __port__))
		mreq = struct.pack('4sl', socket.inet_aton(__multicast_network__), socket.INADDR_ANY)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

		while True:
			notification = pynotify.Notification(Title, sock.recv(10240))
			notification.set_urgency(pynotify.URGENCY_NORMAL)
			notification.set_timeout(pynotify.EXPIRES_NEVER)
			notification.show()

	else:
		DATA = &quot; &quot;.join(sys.argv[2:])

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		if sys.argv[1] == 'all':
			sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
			sock.sendto(DATA, (__multicast_network__, __port__))
		else:
			sock.sendto(DATA, (sys.argv[1], __port__))
</pre>