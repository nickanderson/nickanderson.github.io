---
title: Backdoor corporate sabotage with DNS
author: Nick Anderson
type: post
date: 2008-07-10T01:07:45+00:00
url: /2008/07/09/backdoor-corporate-sabotage-with-dns/
categories:
  - Posts
tags:
  - corperate sabatoge
  - dns
  - dnsmadeeasy
  - ultradns

---
I&#8217;m not really certain how common corporate sabotage is. Sure there are DOS attacks daily on this or that network or this or that server but what percentage of those are script kiddies and what percentage are well thought out planned attacks designed to cripple a competitor even if only for a short time. Typically DOS attacks are dealt with by Server and Network Admins adding black holes to offending networks. Recently while doing some research I stumbled on what seems to be a neglected DNS attack. One that the target may not become aware of until the next billing cycle or if carried out methodically months.<!--more-->

<!--adsense-->

Ultradns and Dnsmadeeasy are two leading hosted DNS providers. The model is simple. You pay to have your dns hosted on their network and servers. They ensure DNS propagation between their servers is fast and they have the capacity to protect against DOS attacks. Typically you get some base package of queries per month. For example the Business Membership is 59.95/yr and you get 10 million queries/month. That is a lot of queries when you consider that many queries for your domain will be served by caching servers. And overage charges are minimal at $6.00/ 1 million queries (if you don&#8217;t purchase blocks ahead of time). I was thinking boy I hope there is some kind of throttling in place to prevent some unsavory competitor from looping a dig against their name servers for my domain. So on a whim i looked around and actually found a domain (on the first try I might add) which uses Dnsmadeeasy. Oh in case you were wondering how I found out, I just did a whois and looked at the authoritative name servers and wow ns0.dnsmadeeasy.com was listed. So I ran a quick loop for 100 lookups on the domain.

`time for i in $(seq 100);do dig redacted.tld @ns0.dnsmadeeasy.com;done`

While I expected to get off a few lookups and then just wait for some throttle timeout to shut me down I was supprised to get all 100 lookups done in 11 seconds, subsequent tests showed similar times mostly faster. So conservativly say you can do 10 lookups a second. If my math serves me correct you can do 10 million lookups in just about 5 hours. After that you have broken the 10 million limit for the month. Holding steady at the same rate thats 864000 queries in 24 hours and 25920000 in 30 days. Yeah so not a bank breaker at $6/ million but this was from a single PC and I doubt network was the bottle neck. A distributed attack could end up costing a company thousands upon thousands. Refusal to pay could result in DNS being shut off, and effectively creating a DOS. For fun I tried 100 lookups against Ultradns for some of their banner customers and also received no throttling. Still a bit surprised at this seemingly overlooked hole I called Dnsmadeeasy and asked the sales department what protections were in place to prevent or mitigate malicious lookups. His response was do you mean DOS? When I explained the issue he said we can not block that, as we do not know if there are 1000 people behind your company firewall that are really interested in that website.

It does not seem unreasonable to provide a throttling mechanism. Oh you queried 10 times in the last 2 seconds? I think I will block you for 5 mintues. Happens again within x time increase block time to 10 minutes and so on. So who wants to loop while true dig amazon @udns1.ultradns.net for a month or so and see what happens. Will they report being hacked? Will the cops bust down your door? Will amazon just eat the cost (probably). But why not just provide simple throttling for obviously either misconfigured or malicious lookups?