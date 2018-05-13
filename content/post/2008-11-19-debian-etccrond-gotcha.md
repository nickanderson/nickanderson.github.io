---
title: Debian /etc/cron.d/ gotcha
author: Nick Anderson
type: post
date: 2008-11-19T14:57:53+00:00
url: /2008/11/19/debian-etccrond-gotcha/
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - cron
  - debian

---
I typically use /etc/cron.d to store all of my system crontabs. I recently ran into an issue that I had either not run into before, or fixed and paid no attention to. Files stored in /etc/cron.d/ or any /etc/cron.* directory need to adhear to the run-parts Debian cron script namespace which consists is

<pre class="brush: bash; title: ; notranslate" title="">(^[a-z0-9][a-z0-9-]*$)
</pre>

for the regex impared this does not include the dot character. If you have a file in /etc/cron.d/ that has a dot in it it will not be evaluated by cron. I have seen mention of underscore not being valid but in my testing underscore was not an issue, only dots.