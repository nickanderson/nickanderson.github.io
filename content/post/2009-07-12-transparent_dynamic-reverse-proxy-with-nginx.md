---
title: Transparent dynamic reverse proxy with nginx
author: Nick Anderson
type: post
date: 2009-07-12T17:29:21+00:00
url: /2009/07/12/transparent_dynamic-reverse-proxy-with-nginx/
syntaxhighlighter_encoded:
  - 1
openid_comments:
  - 'a:1:{i:0;s:4:"1151";}'
categories:
  - Posts
tags:
  - nginx
  - proxy

---
A while back I wrote about using [Apache as a dynamic reverse proxy][1]. Anyone who has done even minimal research into web servers knows that Apache is the swiss army knife. It trys to be everything for everyone, and like a swiss army knife may not be as good as a more refined too at least as far as efficiency is concerned.

Here is the situation. You have a single pinhole into your private network. You have a single ip at your gateway. You want to serve multiple websites on your lan that may be running on multiple physical servers. Rather than opening up multiple ports and pinholling to all the different spots you want to serve, or getting more external ips and doing 1to1 NAT you can use a reverse proxy to be your single entrance point. The reverse proxy will fetch the content from the backend server and serve it up.

nginx is a HTTP server and mail proxy server. One of its features basic HTTP features is accelerated reverse proxying.

nginx should be available through your package manager so just aptitude (or whatever your package manager is yum, emerge, pacman) install it.

The config file paths shown are Debian specific but the config itself should work on any distro.

Edit /etc/nginx/sites-available/default and make it look like this

<pre class="brush: plain; title: ; notranslate" title="">server {
     listen  :80;
     server_name  _;
     access_log  /var/log/nginx/proxy.access.log;

     location / {
     resolver        127.0.0.1;
     proxy_pass      http://$host$uri;
     proxy_redirect off;
     proxy_set_header        Host    $host;
     proxy_set_header        X-Real-IP $remote_addr;
     proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
     }

     error_page   500 502 503 504  /50x.html;
     location = /50x.html {
          root   /var/www/nginx-default;
     }
}
</pre>

So this config causes nginx to listen on all interfaces/ips. server\_name \_; matches on anything so essentially this is a catchall now. You can tail proxy.access.log in order to see the requests are they come in and are served.

The location section is where the actual proxying happens. Since this is a dynamic configuration you need to set a resolver where the requested names can be looked up (and overridden for the local lan address). dnsmasq reads is dns configuration right out of /etc/hosts. It&#8217;s easy to install and configure so I reccomend using it. We will install and configure it shortly but for now just leave resolver as 127.0.0.1. proxy\_pass does the requesting of the page we are proxying. Since this is a transparent dynamic proxy we just have it request the same thing that was requested of the proxy. proxy\_redirect should be set to off since we are just passing on the same request. We need to set a few headers for logfiles on the backend servers as well as making sure that Host is set to the requesting host in case your using name based virtual hosts on your backend servers. I have left the error page in the default config (at least on debian its default). This provides a nice error message in case your proxy is working but one of the backend servers is not. It just serves the index.html that is located in /var/www/nginx-default. Feel free to change that path to something else, modify the index.html or omit the error_page and error page location section all together as they aren&#8217;t needed for this to work.

Now we need to get that local resolver (dnsmasq) installed so we can take our reverse proxy for a spin. Go ahead and aptitude (or whatever) install dnsmasq.

At least on debian dnsmasq comes out wanting to serve dhcp. You probably do not want this behavior. There is also the question of needing access to these same services by the same name on your LAN. If you need this you might need to do some slight adjusting of your dns. I might reccomend pointing your main dns to this dnsmask proxy or pointing all of your clients at this dnsmasq install since it will look up other requested names other than those in /etc/hosts. For this example I will assume you will be wanting to access these same web services internally with the same names and bypass the proxy. So I will assume you have either changed your primary dns cacher/resolver (think soho router or whatnot) to the address of the proxy server (since its running dnsmasq as well), or set all of your clients to point directly at the proxy server for dns. We need to edit the dnsmasq config to disable dhcp.

Edit /etc/dnsmasq.conf and add no-dhcp-interface=ethx. Do that for every interface on your system so that your not accidentally serving out dhcp to anyone. If somone has a more generic way to disable dhcp in dnsmasq without specifying each interface I would love to know but from reading the man this was the only way I could find. So you may have something like the following in you /etc/dnsmasq.conf.

<pre class="brush: plain; title: ; notranslate" title="">no-dhcp-interface=eth0
no-dhcp-interface=eth1
</pre>

After making the change you should be ready to add entries to the proxy servers /etc/hosts for dnsmasq to use and then test your reverse proxy.

Lets say you have www.test.com served off of a machine with the ip 192.168.1.2 and you have tickets.office.test.com served off of 192.168.1.3. Lets also assume that your world routeable ip is 123.123.123.123. You will need to make sure that your authoritative dns (the real one that servs for test.com has A records for both www.test.com and tickets.office.test.com pointing to 123.123.123.123. Now on the machine running dnsmasq (in this example also your proxy server) add the following entries to /etc/hosts.

<pre class="brush: plain; title: ; notranslate" title="">192.168.1.2 www.test.com
192.168.1.3 tickets.office.test.com
</pre>

Go ahead and restart dnsmasq (from making changes to the config, subsequent changes to /etc/hosts should not require dnsmasq restart to pick up changes) and nginx.

Now tail your proxy.access.log file and start making requests to www.test.com and tickets.office.test.com from both the inside of your lan as well as outside against your world ip. It should all magically serve up the same content.

This type of config can be useful in many situations. You have a small office and budget that reflects that not being able to afford multiple ips but needing to provide web services behind the firewall. You work in a large corporation where someone else manages the firewall and you would like to bring up more web services without waiting for the other person to make the necessary changes to the firewall.

One of the other benefits this provides is being relatively self documenting  with regard to what web services you host behind the firewall. (you should be able to see all of them in /etc/hosts since you have to override the dns)

 [1]: http://www.cmdln.org/2008/06/10/dynamic-reverse-proxy-with-apache-mod_rewrite-and-mod_proxy/