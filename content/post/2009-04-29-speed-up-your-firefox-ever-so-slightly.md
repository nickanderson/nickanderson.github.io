---
title: Speed up your firefox (ever so slightly)
author: Nick Anderson
type: post
date: 2009-04-29T21:40:40+00:00
url: /2009/04/29/speed-up-your-firefox-ever-so-slightly/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - firefox
  - sqlite

---
So I noticed my places.sqlite has grown to over 80M. Since Firefox 3 thats where things like bookmarks are stored. I guess favicons are stored in that same database. At any rate I am very tab happy. I have to control myself and about once every 2 weeks or so I have to sit down and close out a bunch of tabs. Its not uncommon for me to have 90ish tabs open. Boy firefox gets sluggish. Anyway you can perform a bit of maintenance on your firefox databases. I saw a significant speed improvement when opening firefox as well as opening new tabs after doing this. You have to close all firefox instances that are using the profile and it might be a good idea to just backup your profile before you do this but its pretty safe.

Note: this command will just do it for every profile you have.

<pre class="brush: php; title: ; notranslate" title="">for i in ~/.mozilla/firefox/*/*.sqlite; do sqlite3 $i VACUUM;done;
</pre>