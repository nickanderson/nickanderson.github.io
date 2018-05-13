---
title: Gnu Screen workflow management (change working directory)
author: Nick Anderson
type: post
date: 2008-12-05T18:01:20+00:00
url: /2008/12/05/gnu-screen-workflow-management-change-working-directory/
aktt_notify_twitter:
  - no
openid_comments:
  - 'a:2:{i:0;s:4:"1200";i:1;s:4:"1201";}'
categories:
  - Posts
tags:
  - gnu screen

---
I was recently asked how to change screens working directory. It took me a few minutes to realize the benefit of this as I typically have different screen sessions for different purposes. But after thinking about it for a few minutes I have been in situations where what I was doing in a screen session morphed and it would have been nice for new windows to be opened to a different working directory than where I started my session.

A few minutes of grepping around in man -a screen gave the answer.

<pre>C-a:chdir /path/to/new/dir</pre>