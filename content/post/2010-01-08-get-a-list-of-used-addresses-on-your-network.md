---
title: Get a list of used addresses on your network
author: Nick Anderson
type: post
date: 2010-01-08T14:54:46+00:00
url: /2010/01/08/get-a-list-of-used-addresses-on-your-network/
syntaxhighlighter_encoded:
  - 1
categories:
  - Posts

---
This comes up from time to time for me. Either myself or someone else needs to see what address are either in use or not in use (at least as far as ping is concerned). So here are a few oneliners to hopefully make your day brighter.

<!--more-->

Assuming your network is 192.168.1.0/24 (thats 192.168.1.0-255 255.255.255.0).

#### Use nmap to ping scan your network

<pre class="brush: bash; title: ; notranslate" title="">nmap -v -sP 192.168.1.0/24

</pre>

#### Use nmap and grep to scan your network and filter for hosts that are &#8220;up&#8221;

<pre class="brush: bash; title: ; notranslate" title="">nmap -v -sP 192.168.1.0/24 | grep up

</pre>

#### Use nmap and grep to scan your network and filter for ips that are unused or non-responsive

<pre class="brush: bash; title: ; notranslate" title="">nmap -v -sP 192.168.1.0/24 | grep down

</pre>

Many times you just want the list of addresses because you are going to do some other processing on them.

#### Use nmap,  and awk to get only the list of ips that are unresponsive

<pre class="brush: bash; title: ; notranslate" title="">nmap -v -sP 192.168.1.0/24 | awk '/down/ {print $2}'

</pre>

Of course you can add some file redirection here if you need to save the output.

<pre class="brush: bash; title: ; notranslate" title="">nmap -v -sP 192.168.1.0/24 | awk '/down' {print $2}' &gt; iplist.txt

</pre>