---
title: Google like unit conversion on the console
author: Nick Anderson
type: post
date: 2008-12-05T05:14:20+00:00
url: /2008/12/04/google-like-unit-conversion-on-the-console/
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - conversion
  - math
  - units

---
For those of you who are horrid at math like I am googles unit conversion is a great help. Want to know how many GB 1Mbps is in a month? Simple just ask google. Well I like to have the ability even when I am not online and I found units. Its in the debian repository and oh so easy to use.

<pre class="brush: bash; title: ; notranslate" title="">units -t '1Mbps' 'GB/month'
328.71798
units -t '1hour' 'seconds'
3600
</pre>