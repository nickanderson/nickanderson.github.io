---
title: Version your /etc
author: Nick Anderson
type: post
date: 2009-02-19T15:19:36+00:00
url: /2009/02/19/version-your-etc/
aktt_notify_twitter:
  - no
aktt_tweeted:
  - 1
openid_comments:
  - 'a:2:{i:0;s:3:"819";i:1;i:1297;}'
categories:
  - Posts
tags:
  - etc
  - git
  - version control

---
Seems like we are on a bit of a roll with regard to the topic of versioning lately. Yesterday [Legooolas][1] commented about using version control for your home directory. I do and I&#8217;ll cover that in a different post but I use it for a different task. Now on to todays topic.
  
Do you keep track of configuration changes? You should. Maybe your using an advanced configuration management system like puppet. Even if you are you should keep your puppet configs versioned.
  
At any rate etckeeper is a great tool to version your configuration files stored in /etc. etckeeper hooks into your package manager and updates the repo each time changes are detected.
  
Its super easy to setup. In a debian based system just install via apt.

<pre class="brush: bash; title: ; notranslate" title="">sudo aptitude install etckeeper
</pre>

Once etckeeper is installed you need to initialize the git repository and do the initial check in.

<pre class="brush: bash; title: ; notranslate" title="">sudo etckeeper init
sudo etckeeper commit
</pre>

 [1]: http://www.cmdln.org/2009/02/18/movin-in-movin-out/comment-page-1/#comment-814