---
title: 'Howto: Remove PDF passwords and encryption'
author: Nick Anderson
type: post
date: 2009-02-23T14:45:04+00:00
url: /2009/02/23/howto-remove-pdf-passwords-and-encryption/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - decrypt
  - pdf

---
Have you ever gotten a pdf with one of those annoying passwords? A while back I bought an e-book and it came with a password. Its really annoying especially if I want to read it on a mobile device. Anyway if you are annoyed as much as I am fear no more.

Install qpdf

<pre class="brush: bash; title: ; notranslate" title="">aptitude install qpdf
</pre>

Decrypt your pdf

<pre class="brush: bash; title: ; notranslate" title="">qpdf --password=password --decrypt input.pdf output.pdf
</pre>