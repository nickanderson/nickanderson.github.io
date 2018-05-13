---
title: Automate Sun iLOM settings
author: Nick Anderson
type: post
date: 2010-03-31T17:11:06+00:00
url: /2010/03/31/automate-sun-ilom-settings/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/aov9JS
categories:
  - Posts
tags:
  - python
  - sun
  - sysadmin

---
I recently had a need to push out a few settings to a group of iLOMs on new Sun servers. I really despise using a web interface for everything so I took the ssh route. The first thing I tried to do after determining the commands I needed was to shove the commands in with ssh directly.  I quickly became apparent that route just wasn&#8217;t going to work.

When you log into the iLOM &#8220;daemons&#8221; need to initialize. Based on the errors that I got while trying to shove the commands in with ssh I assume these &#8220;daemons&#8221; have something to do with access controls. It became apparent that I needed to use expect if I wanted to automate over the ssh connection. I used the pexpect module in python and wrote a simple script to push a batch of commands to a list of hosts.

It was written from the point of view that most of these settings need to happen when you receive a new box so it defaults to the iLOM default username and password (root/changeme). I&#8217;m not sure how often I will use this tool but I will be sure to keep my command snippets in version control as its highly likely I will be using the same settings over and over again or with slight permutations.

[iLOM-commander can be found in my github][1] (patches accepted)

 [1]: http://github.com/nickanderson/iLOM-commander