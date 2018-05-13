---
title: What webserver shell function
author: Nick Anderson
type: post
date: 2008-12-05T17:34:01+00:00
url: /2008/12/05/what-webserver-shell-function/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - shell

---
This is lifted from http://bashcurescancer.com/shell-function-which-webserver-does-that-site-run.html.

Handy shell function you can put in your .bashrc. Quickly find out what server a host is running.

<pre class="brush: bash; title: ; notranslate" title="">what-http-server() { curl -s -I $(for h in "$@"; do printf "http://%s " "$h"; done) | awk -F': ' '/^Server:/ {print $2}'; }
</pre>

Now try what-http-server kernel.org google.com hotmail.com.