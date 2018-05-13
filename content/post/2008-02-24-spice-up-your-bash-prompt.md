---
title: Spice up your bash prompt
author: Nick Anderson
type: post
date: 2008-02-25T03:59:17+00:00
url: /2008/02/24/spice-up-your-bash-prompt/
categories:
  - Posts
tags:
  - bash
  - bash prompt
  - command line

---
I spend a lot of my time sitting in front of terminals if you have not yet guessed. When dealing with different user accounts across different systems and a plethora of terminals open its nice to have a bit of information about who you are, and where you are. I also like to be able to easily differentiate output from different commands. If your interested read on.
  
<!--more-->


  
<!--adsense-->


  
You will want to edit your user .bashrc as well as your /root/.bashrc. For your user append this line

<pre>PS1="\n[\u@\h] \w\n$ "</pre>

This will give you output like this on your terminal.

<pre>[cmdln@neuron] ~/test
$ ls
file  file2

[cmdln@neuron] ~/test
$</pre>

And for /root/.bashrc you will want to append

<pre>PS1="\n[\[033[1;31m\]\u\033[0m\]@\033[1;33m\]\h] \w\n$ "</pre>

This will give you output like this.

<pre>[<font color="#ff0000">root</font>@<font color="#ffff00">neuron</font>] /home/cmdln/test
# ls
file  file2

[<font color="#ff0000">root</font>@<font color="#ffff00">neuron</font>] /home/cmdln/test
#</pre>