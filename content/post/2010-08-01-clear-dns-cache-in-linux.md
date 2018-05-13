---
title: Clear DNS Cache in Linux
author: Nick Anderson
type: post
date: 2010-08-01T18:42:29+00:00
url: /2010/08/01/clear-dns-cache-in-linux/
categories:
  - Posts
tags:
  - dns
  - nscd
  - sysadmin

---
Had a slightly vexing issue the other day. During a migration the destination host ended up caching some stale DNS entries. I tried a quick restart of nscd to no avail, rebooted the VM, again no joy. Even overriding the host in /etc/hosts wasn&#8217;t working. Took a few minutes of digging but what did work was 

<pre class="brush: plain; title: ; notranslate" title="">nscd -i hosts</pre>

. Just something to remember if you ever seem to have a stubborn caching issue, rebooting/restarting wont always solve the issue.

Also happy late sysadmin day! Unfortunately I missed the festivities being stuck in the hospital. Oh well, there is always next year.