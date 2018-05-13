---
title: NetworkManager funkyness (knetworkmanager)
author: Nick Anderson
type: post
date: 2008-04-06T04:38:29+00:00
url: /2008/04/05/networkmanager-funkyness-knetworkmanager/
categories:
  - Posts
tags:
  - knetworkmanager
  - kubuntu
  - NetworkManager
  - ubuntu
  - wireless

---
Ok so this is the opposite of what I generally use but its been annoying me and I just figured out what was causing it so I figured I would share it. I am currently running Kubuntu Hardy Haron but this problem was present when I installed my first Ubuntu varient Gutsy Gibbon. <!--more--> Knetworkmanager worked when I first installed. Then at some point it just stopped detecting my wireless card. Its not that it could not see my network card because I could go through manual configuration and connect to wireless without issue, I could also just use iwconfig and dhclient at the commandline (which is what I did). Anyway the fact that it would not show the signal strengh was irritating me. I found that if you make sure any entries in your /etc/network/interfaces that relate to wireless it starts working. So try commenting out any wlan0 entries and restart both networking and knetworkmanager. When you right click on knetwork manager if your lucky like me you will have the option to connect to various wireless networks, and once connectedyou will have your signal display back.

Note: thinkpad t61p,  Intel Pro 4965 AGN card (iwl driver)