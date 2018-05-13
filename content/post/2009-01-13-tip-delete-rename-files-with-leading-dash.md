---
title: 'Quick tip: Delete or rename files with leading dash (-)'
author: Nick Anderson
type: post
date: 2009-01-14T05:58:26+00:00
url: /2009/01/13/tip-delete-rename-files-with-leading-dash/
aktt_notify_twitter:
  - no
openid_comments:
  - 'a:1:{i:0;s:3:"773";}'
categories:
  - Posts

---
I was restoring some files from backup today and ran into a few files that had leading slashes. Whenever I see those kind of things I rename the files since they are a pain to work with in the shell.

If you find yourself at a shell and need to work with files that have a leading dash just use the relative path and include the dashed filename in quotes.

<pre class="brush: bash; title: ; notranslate" title="">mv ./"-somefile.txt" ./somefile.txt
</pre>