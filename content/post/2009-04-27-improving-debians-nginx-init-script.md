---
title: Improving debians nginx init script
author: Nick Anderson
type: post
date: 2009-04-27T17:14:36+00:00
url: /2009/04/27/improving-debians-nginx-init-script/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - nginx

---
nginx is a high performance HTTP and mail proxy server written by [Igor Sysoev][1].

I&#8217;m not sure what the init scripts do for other distros but it seems a bit of an oversight to leave out checking the config file when running the init script. 

Add this line to your nginx init script right after the text -x $DAEMON line to make it check the config before proceeding to start stop or restart the service.

<pre class="brush: php; title: ; notranslate" title="">$DAEMON -t &gt; /dev/null 2&gt;&1 
if [ $? -ne 0 ]; then
        echo "Configuration file has errors, try $DAEMON -t"
        exit 0
fi
</pre>

 [1]: http://http://sysoev.ru/en/