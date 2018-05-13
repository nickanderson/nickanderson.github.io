---
title: Match string and print preceding line
author: Nick Anderson
type: post
date: 2008-04-10T19:59:52+00:00
url: /2008/04/10/match-string-and-print-preceding-line/
categories:
  - Posts
tags:
  - bash
  - grep
  - oneliner
  - pattern matching
  - previous line
  - sar
  - scripting

---
Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
`Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
` 
  
Great for using in scripts to collect bits of information you might need.

Oh and for good measure if I wanted to do this before I would have done this.

<pre class="brush: bash; title: ; notranslate" title="">sar | grep -B1 ^Average: | grep -v ^Average
</pre>

And look at how much time I saved by not having the extra pipe!
  
``Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
`Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
` 
  
Great for using in scripts to collect bits of information you might need.

Oh and for good measure if I wanted to do this before I would have done this.

<pre class="brush: bash; title: ; notranslate" title="">sar | grep -B1 ^Average: | grep -v ^Average
</pre>

And look at how much time I saved by not having the extra pipe!
  
`` 
  
vs
  
```Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
`Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
` 
  
Great for using in scripts to collect bits of information you might need.

Oh and for good measure if I wanted to do this before I would have done this.

<pre class="brush: bash; title: ; notranslate" title="">sar | grep -B1 ^Average: | grep -v ^Average
</pre>

And look at how much time I saved by not having the extra pipe!
  
``Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
`Text processing is fun. Well, fun if you like to beat your head against a wall. Most of the time I just string a few things together to get whatever I am doing done. Its much better to find the shortest way to do something, it spawns less processes, is more efficient and generally a good idea. So if you have ever wanted to match a string from some given output and only print the preceding line here you go.<!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">awk '/pattern/{print x};{x=$0}'
</pre>

You might also wonder why you might want to do that. Well the reason I wanted to do it was to pull the sar output of the last run. Sar output ends in ^Average: but I just wanted the line before that so this is what I came up with.

<pre class="brush: bash; title: ; notranslate" title="">sar | awk '/^Average:/{print x};{x=$0}'
</pre>

That just spits out the last recorded sar information like this.
  
` 
  
Great for using in scripts to collect bits of information you might need.

Oh and for good measure if I wanted to do this before I would have done this.

<pre class="brush: bash; title: ; notranslate" title="">sar | grep -B1 ^Average: | grep -v ^Average
</pre>

And look at how much time I saved by not having the extra pipe!
  
`` 
  
vs
  
```