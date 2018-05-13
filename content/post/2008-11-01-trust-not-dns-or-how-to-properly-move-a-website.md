---
title: Trust not DNS or How to properly move a website
author: Nick Anderson
type: post
date: 2008-11-02T00:08:08+00:00
url: /2008/11/01/trust-not-dns-or-how-to-properly-move-a-website/
aktt_tweeted:
  - 1
openid_comments:
  - 'a:2:{i:0;s:3:"612";i:1;s:3:"880";}'
categories:
  - Posts
tags:
  - apache
  - DNS TTL
  - mod_proxy
  - website migration

---
Recently I had to move a website that gets a fair amount of traffic. I prepared for this by lowering the TTL on the domains associated several weeks in advance to 600 seconds. Originally my plan was to toss up a maintenance page on the old server, change the DNS, and figured that within a few hours max the vast majority of DNS servers would have the update being that TTL had been set at 600 seconds for several weeks and prior to that it was set at 48 hours. This was all planned for the middle of the night on a weekend (very slow traffic time). I was in for a rude awakening the next morning.
  
<!--more-->

The next morning I got a call that someone was still seeing the maintenance page. I checked, and from the DNS provided by my ISP everything acted as expected. No maintenance page, just the normal site. I checked DNS against a few other servers and all appeared normal. The DNS of the callers ISP however did not seem to have the proper update. A quick dig showed that while it even reported the TTL correctly at 600 seconds it was not obtaining an updated recored, or its upstream DNS was not.

I logged into the old server to check the apache logs and found that approximately 1/3 of traffic was still hitting the old server! Luckily this was a Sunday morning and another slow day. Now to find a solution. Obviously I cannot call all of the ISPs and complain about their mis configured DNS servers. Even if I could no one would be able to fix anything on a Sunday morning.

**The Solution**: Apache&#8217;s wonderful mod_proxy (any reverse proxy will do).

Since we have about 1/3 of traffic going the wrong place we needed to do something. Apache&#8217;s reverse proxy is easy to setup. The key is to make sure that the old server can reference the new server. What I did was drop the following into the vhost configuration for the website.

<pre class="brush: bash; title: ; notranslate" title="">ProxyRequests Off
ProxyPass / http://domain.tld/
ProxyPassReverse / http://domain.tld/
</pre>

Now that worked out great for the main website but part of the site uses ssl. There is some extra magic that needs to happen in order to proxy the ssl traffic. So in the virtual host configuration for the ssl version of the website I added the following.

<pre class="brush: bash; title: ; notranslate" title="">SSLProxyEngineOn
ProxyRequests Off
ProxyPass / https://domain.tld/
ProxyPassReverse / https://domain.tld/
</pre>

So for people with fubar dns that hit oldserver when accessing domain.tld apache answers the requests with a proxy to domain.tld as resolved from the old server. So to make sure that happens correctly either an entry in /etc/hosts or a change of nameservers in /etc/resolv.conf might be required. After that I just kept an eye on apachetop (which is a cool tool btw) to see when the requests dropped off. It ended up taking a little over 48 hours before all of the dns updated properly. Just so I don&#8217;t get a &#8220;dns propagation typically takes 48 hours&#8221; comment. Remember I was NOT changing DNS servers I only changed the DNS records to point to a new ip, and the TTL had been at 600 seconds for weeks ahead of time in preparation.

I had no idea how many DNS servers did not properly obey TTL. I&#8217;ve learned my lesson. Any future migrations will have a proxy from the get go.

If anyone cares to chime in and blow off steam on why DNS is in such a sad state feel free.