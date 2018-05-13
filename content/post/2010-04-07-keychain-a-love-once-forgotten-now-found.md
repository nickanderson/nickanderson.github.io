---
title: 'Keychain: a love once forgotten now found'
author: Nick Anderson
type: post
date: 2010-04-07T15:04:03+00:00
url: /2010/04/07/keychain-a-love-once-forgotten-now-found/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/cAfbD7
categories:
  - Posts
tags:
  - debian
  - gentoo
  - gpg-agent
  - keychain
  - ssh-agent
  - sysadmin

---
I don&#8217;t know how many of you know that I am a recovering gentoo user. One of the staples of my desktop used to be [keychain][1]. Keychain is a simple wrapper for ssh-agent and gpg-agent. It eases the use of a single long running agent per system instead of per login session. For some reason this tool had fallen out of my basket when I switched to debian several years ago. I&#8217;m glad to have it back.

It&#8217;s easy to install in debian based systems, simply

<pre class="brush: bash; title: ; notranslate" title="">aptitude install keychain
echo "keychain ~/.ssh/id_rsa" &gt;&gt; ~/.bashrc
</pre>

 [1]: http://www.gentoo.org/proj/en/keychain/