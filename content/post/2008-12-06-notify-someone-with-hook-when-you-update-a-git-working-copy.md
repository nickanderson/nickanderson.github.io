---
title: Notify someone with hook when you update a git working copy
author: Nick Anderson
type: post
date: 2008-12-07T05:19:26+00:00
url: /2008/12/06/notify-someone-with-hook-when-you-update-a-git-working-copy/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - bash
  - code
  - email
  - git
  - script

---
Some projects have production code that runs off of a git cloned repository. There may be a case in which you want to notify others when that clone pulls. It is a pretty easy feat with gits post-merge hook. The post-merge hook will run after a merge (think git pull). All you have to do it create a project/.git/hooks/post-merge shell script and chmod +x it. Next time you pull successfully that script will run. Here is an example.

<pre class="brush: bash; title: ; notranslate" title="">#!/bin/bash
TEMPLOG=$(mktemp)
echo "Sending email notification of update"
git log --reverse --no-merges --stat @{1}.. &gt; $TEMPLOG
sendEmail -u "Production code update notification" -t recipient@domain.com &lt; $TEMPLOG
rm $TEMPLOG
</pre>