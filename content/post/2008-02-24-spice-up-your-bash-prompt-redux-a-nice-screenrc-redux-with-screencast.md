---
title: Spice up your bash prompt redux | A nice .screenrc redux with screencast
author: Nick Anderson
type: post
date: 2008-02-25T05:16:50+00:00
url: /2008/02/24/spice-up-your-bash-prompt-redux-a-nice-screenrc-redux-with-screencast/
categories:
  - Posts
tags:
  - command line
  - screen
  - screencast
  - tips

---
This is more or less going to be an addendum to my last post as well as an update to my previous screenrc post. About 5 minutes after posting I realized that my additions to my prompt broke some new additions to new screenrc settings.
  
<!--more-->


  
<!--adsense-->


  
You will want to edit your user .bashrc as well as your /root/.bashrc. For your user append this line

<pre>export PS1='\[\033k\033\\\]'
export PS1="\n[\u@\h] \w\n"$PS1'\$ '</pre>

This will give you output like this on your terminal.

<pre>[cmdln@neuron] ~/test

$ ls

file  file2[cmdln@neuron] ~/test

$</pre>

And for /root/.bashrc you will want to append

<pre>export PS1='\[\033k\033\\\]'

export PS1="\n[\[\033[1;31m\]\u\033[0m\]@\033[1;33m\]\h\033[0m\]] \w\n"$PS1'\$ '</pre>

This will give you output like this.

<pre>[<font color="#ff0000">root</font>@<font color="#ffff00">neuron</font>] /home/cmdln/test

# ls

file  file2[<font color="#ff0000">root</font>@<font color="#ffff00">neuron</font>] /home/cmdln/test

#</pre>

So you may be wondering why the small changes from the previous article? Well these changes allow you to have a fany screen hardstatus line. When you run commands in screen it will update the hardstatus line to the name of the command you are running. The magic pill here is the shelltitle directive in .screenrc.
  
/root/.screenrc

<pre class="brush: cpp; title: ; notranslate" title="">vbell off
startup_message off
hardstatus alwayslastline
hardstatus string '%{= kg}[%{G}%H%{g}][%= %{= kw}%?%-Lw%?%{=b kR}(%{W}%n-%t%?(%u)%?%{=b kR})%{= kw}%?%+Lw%?%?%= %{g}][%{Y}%l%{g}]%{g}[%{B}%d.%m.%Y %{G}%C%A%{g}]'
termcapinfo xterm|xterms|xs|rxvt ti@:te@

altscreen on
shelltitle '# |bash'
</pre>

user .screenrc

<pre class="brush: cpp; title: ; notranslate" title="">vbell off
startup_message off
hardstatus alwayslastline
hardstatus string '%{= kg}[%{G}%H%{g}][%= %{= kw}%?%-Lw%?%{=b kR}(%{W}%n-%t%?(%u)%?%{=b kR})%{= kw}%?%+Lw%?%?%= %{g}][%{Y}%l%{g}]%{g}[%{B}%d.%m.%Y %{G}%C%A%{g}]'
termcapinfo xterm|xterms|xs|rxvt ti@:te@

altscreen on
shelltitle '$ |bash'
</pre>

The screenrc displays a status line with the hostname followed by a list of running windows with () around the active window, that is followed by the current load of the system and finally the date and time. There is one little trick to the shelltitle command. It detects the last character of your prompt and it uses what you type after that to set the window title. So if you wheel up to root when your prompt character changes from $ to # the screen will be stuck with the last command you ran (sudo or su). I will demonstrate this in the screencast below.

[flash http://www.cmdln.org/wp-content/uploads/2008/02/screencast\_bashprompt\_screenrc.flv mode=0]