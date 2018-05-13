---
title: Dynamic Reverse Proxy with Apache, mod_rewrite, and mod_proxy
author: Nick Anderson
type: post
date: 2008-06-10T13:50:27+00:00
url: /2008/06/10/dynamic-reverse-proxy-with-apache-mod_rewrite-and-mod_proxy/
categories:
  - Posts
tags:
  - apache2
  - dynamic proxy
  - mod-proxy
  - mod-rewrite

---
Recently I found myself wanting to expose more and more internal web services to the outside. We have an internal mail caching server, ticket system, a handful of development sites, as well as several other internal web services that would be handy to access from remote locations. If you have internal dns, and your dns heirichy is sane you can probably use the same trick I did to allow any internal webservice that has a proper fqdn to work from outside your local LAN. I used Apache2, mod\_proxy, and mod\_rewrite. Only a few lines need to be altered in the default apache site install.

<!--more-->


  
<!--adsense-->

You need to aptitude install libapache2-mod-proxy-html apache2, and a2enmod proxy proxy\_connect proxy\_html proxy_http rewrite.

Then comment out the the line

`</p>
<p>RedirectMatch ^/$ /apache2-default/</p>
<p>`

from /etc/apache2/sites-available/000-default.

Then add these lines outside a Directory directive.

<pre>ProxyRequests Off
&lt;Proxy *&gt;
AddDefaultCharset off
Order deny,allow
Allow from all #
&lt;/Proxy&gt;

RewriteEngine on
RewriteRule ^(.+) $1 [P]
ProxyPassReverse / $1
</pre>

Thats basically it. So if you have a dns setup where something.lan.tld.com resolves to your main firewall from the outside. But on the inside resolves to a local webserver, and you have defaulted port 80 to this new gateway machine you should be able to access the internal machine from outside.

The thing to note is that remotely something.lan.tld.com will resolve to your public ip. And locally it will resolve to a local lan ip. That allows the rewrite and proxy rule to work correctly. Since it just rewrites the same thing and proxies for it the gateway server has to be able to resolve the internal names correctly.

Example:

ticket.lan.somecompany.com resolves to a world routable address like 151.164.1.8. (externally)

ticket.lan.somecompany.com resolves to a local ip like 192.168.1.5 (internally)

Now you can access that internal resource with the same domain name either internally or externally.

It scales well because you do not have to add a new proxy rule for each specific internal resource, all you have to do is add dns both externally and internally. On top of that you could wildcard your external dns for *.lan.somecompany.com and then all that has to be done is add internal dns for each resource you want to access.