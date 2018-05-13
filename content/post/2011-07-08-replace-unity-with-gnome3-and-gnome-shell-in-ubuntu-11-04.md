---
title: Replace unity with gnome3 and gnome-shell in ubuntu 11.04
author: Nick Anderson
type: post
date: 2011-07-08T12:53:16+00:00
url: /2011/07/08/replace-unity-with-gnome3-and-gnome-shell-in-ubuntu-11-04/
categories:
  - Posts
tags:
  - gnome 3
  - gnome-shell
  - sysadmin
  - ubuntu
  - unity

---
Well I gave unity the [old college try][1] in ubuntu 11.04. But last night I just couldn&#8217;t take it any more. There were some small rendering issues occasionally plus some tray programs like [workrave][2] had no place to go, at least that I could find anyway and I really need workrave to remind me to change from sitting to standing positions every so often.

At any rate I decided to try gnome3 and gnome-shell. Its pretty easy to install

<pre class="brush: bash; title: ; notranslate" title="">sudo add-apt-repository ppa:gnome3-team/gnome3
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install gnome-shell
sudo apt-get install gnome-tweak-tool
</pre>

Then I dont know what process needed killed but just restarting X didnt seem to work for me, I rebooted and selected &#8220;Gnome&#8221; from the session selection bar.

My first impressions so far &#8230; much better. I think its a cleaner look. I use [synapse][3] a gnome-do like launcher any time i want to launch a program so for me an application dock is mostly a waste of time. Its clear that unity and gnome-shell have many ideas in common, I just think gnome-shell looks better and stays out of my way more out of the box.

And if you want to remove gnome-shell try the following

<pre class="brush: bash; title: ; notranslate" title="">sudo apt-get install ppa-purge
sudo ppa-purge ppa:gnome3-team/gnome3
</pre>

 [1]: http://www.urbandictionary.com/define.php?term=old%20college%20try
 [2]: http://www.workrave.org/
 [3]: http://mhr3.blogspot.com/2010/11/introducing-synapse-acetylcholine.html