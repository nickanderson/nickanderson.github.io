---
title: Vimtip tolower a visual selection
author: Nick Anderson
type: post
date: 2010-01-20T19:58:45+00:00
url: /2010/01/20/vimtip-tolower-a-visual-selection/
syntaxhighlighter_encoded:
  - 1
categories:
  - Posts

---
Gah so I was futzing with the acl map on our subversion server. Organizing things into groups. I wasn&#8217;t thinking and started uppercasing the users ids when moving them into groups (yes i hate uppercase but its easy to highlight paste them). This of course stopped authentication from working for people who have cached auths returning a 403 error. So how to quickly lowercase a huge swath of ids?<!--more-->

Visually select the swath of text, then do &#8220;gu&#8221; for lowercase, or optionally if you are opposite of me and want to uppercase do &#8220;gU&#8221;.

Why do I even have this problem? Because this server is on a different network and I don&#8217;t have puppet controlling it yet.