---
title: 'autofs: Error logging fail'
author: Nick Anderson
type: post
date: 2010-06-30T02:53:29+00:00
url: /2010/06/29/autofs-error-logging-fail/
categories:
  - Posts
tags:
  - autofs
  - fail
  - sysadmin

---
Why do applications have such horrible error messages. Non-specific errors are really not any more helpful than not logging at all.

I was recently setting up autofs for mounting home directories from an nfs server. The little buggers refused to work right. All I was seeing in the logfile was a notice that an attempt was made, and failed.

<pre class="brush: bash; title: ; notranslate" title="">attempting to mount entry /home/nanderso
failed to mount /home/nanderso
</pre>

<div>
  How helpful is that? Not very, I can tell you that for sure. I already knew it wasn&#8217;t working. Next time you setup autofs make sure to chmod 0644 /etc/auto.*
</div>