---
title: Command Line Ticketing System
author: Nick Anderson
type: post
date: 2008-04-11T18:53:16+00:00
url: /2008/04/11/command-line-ticketing-system/
categories:
  - Posts
tags:
  - command line
  - console
  - ruby
  - terminal
  - ticketing system
  - todo

---
As I have said before life at the terminal is a joy. I constantly struggle with keeping myself organized. I actually work pretty well keeping most things in my head. But one of these days I&#8217;m going to fall down and hit my head and forget everything. So try and try again to keep myself organized and documented do I. I was recently pointed to [TicGit][1] its a ticketing system that is meant to integrate right into your repository. Well I&#8217;m not a developer but I can see the benefit for a terminal todo list and general ticketing for myself as well as my little script repository that is actually maintained in git. Well ok maybe maintained is a bit strong of a word. Anyway on to the good stuff.<!--more-->

<!--adsense-->


  
This is how I got ticgit installed and working for mysef.

<pre class="brush: bash; title: ; notranslate" title="">sudo aptitude install git-core rubygems rake
sudo gem update --system
sudo gem install git
git clone git://github.com/schacon/ticgit.git ticgit.git
cd ticgit.git
rake
sudo gem install pkg/ticgit-0.2.0.gem
cd
</pre>

Not to bad eh? Well we are not quite done. ticgit needs a git repository so if your going to use this for a simple todo list you need to go ahead and get a git repo setup for it.

<pre class="brush: bash; title: ; notranslate" title="">mkdir ticgit
cd ticgit
git init
echo 'please use ti command to view the todos' | tee  readme.txt
git add readme.txt
git commit -m 'initial commit'
</pre>

Now you can use ticgit in this directroy. You should like the ti command to something in your path.

<pre class="brush: bash; title: ; notranslate" title="">sudo ln -s  /var/lib/gems/1.8/bin/ti /usr/local/bin/ti
</pre>

Now you can use the ti commands list, show, new, checkout, state,. comment, and tag to update your simple ticketing system.
  
What? &#8230;. Yeah so I remember most thing but remembering those options isn&#8217;t one of them. Plus I don&#8217;t like to type any more that I have to. So I wrote a bash\_completion stub for ti. All you have to do is drop it in your /etc/bash\_completion.d/ as ti_completion

<pre class="brush: bash; title: ; notranslate" title=""># Author: Nick Anderson
# http://www.cmdln.org
# Description: Simple Bash Completion for ticgit

_ti()
{
local cur prev opts
COMPREPLY=()
cur="${COMP_WORDS[COMP_CWORD]}"
prev="${COMP_WORDS[COMP_CWORD-1]}"
opts="list show new checkout state comment tag"

case "${prev}" in
list)
local list_opts="--order --tag --state --assigned --saveas --list"
COMPREPLY=( $(compgen -W "${list_opts}" -- ${cur}) )
return 0
;;
ti)
COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
return 0
;;
state)
local state_opts="open resolved invalid hold"
COMPREPLY=( $(compgen -W "${state_opts}" ${cur}) )
return 0
;;
*)
return 0
;;
esac

}
complete -F _ti ti

</pre>

I also made up a quick screencast of ticgit so you can see it in all of its glory. Watch the [TicGit Screencast][2].

 [1]: http://github.com/schacon/ticgit/tree/master
 [2]: http://www.cmdln.org/wp-content/uploads/2008/04/ticgit_howto1.ogg "Ticgit Screencast"