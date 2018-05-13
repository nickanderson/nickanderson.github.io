---
title: Secure Hard Drive Wipe
author: Nick Anderson
type: post
date: 2009-08-26T06:00:44+00:00
url: /2009/08/26/secure-hard-drive-wipe/
syntaxhighlighter_encoded:
  - 1
openid_comments:
  - 'a:5:{i:0;s:3:"961";i:1;s:3:"963";i:2;s:3:"964";i:3;s:3:"965";i:4;s:3:"971";}'
categories:
  - Posts
tags:
  - erase
  - shred

---
I&#8217;ve been wiping a lot of hard drives recently. I use shred to do the job.

<pre class="brush: bash; title: ; notranslate" title="">shred -n6 -z -v /dev/sdx
</pre>

What do you do to your drives before disposing of them?