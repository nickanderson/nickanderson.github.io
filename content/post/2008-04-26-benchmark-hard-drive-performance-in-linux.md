---
title: Benchmark hard drive performance in Linux
author: Nick Anderson
type: post
date: 2008-04-26T19:41:21+00:00
url: /2008/04/26/benchmark-hard-drive-performance-in-linux/
categories:
  - Posts
tags:
  - bash
  - bonnie

---
Bonnie is a great tool to use to benchmark your file system. Just a quick tip on using bonnie. <!--more-->You need to give bonnie how much ram you have have in your system, and when you run bonnie you should run with a size 2x as big as your ram. So using this command will help you speed up that calculation.

<pre class="brush: bash; title: ; notranslate" title="">bonnie++ -r  $(free -m | awk '/^Mem/{print $2}') -s $(echo $(free -m | awk '/^Mem/{print $2}')*2| bc)
</pre>

We use subcommands to expand and automattically use the right parameters for bonnie. Would be easy enough to stick that into a shell script to make a small wrapper and pass along any other arguments to bonnie like user and directory.