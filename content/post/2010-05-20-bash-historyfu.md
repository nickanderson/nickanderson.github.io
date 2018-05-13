---
title: bash history-fu
author: Nick Anderson
type: post
date: 2010-05-20T15:14:41+00:00
url: /2010/05/20/bash-historyfu/
categories:
  - Posts
tags:
  - bash
  - sysadmin

---
I came across a new blog (seems to have come on-line in March) <http://www.epoxyjournal.com>. One of the entries was about [how to clear command history][1]. Everyone has inadvertently pasted or typed something into the wrong shell. Sometimes its worthwhile to clean up after yourself and sometimes its not. I figured I would offer a suggestion for the times you want to avoid having your embarrassing moments in your ~/.bash_history.

Instead of blowing away your entire current buffer with history -c you can redirect it to another file, flush the buffer to the file, clean it up then append it to your ~/.bash_history. Sure its more work then abandoning your history but insert [Godwin&#8217;s Law][2].

So it might look something like this.

<pre class="brush: bash; title: ; notranslate" title="">$ echo some long one liner you want to preserver
$ echo something embarrassing
$ export HISTFILE=~/tmphistfile
$ history -a
$ grep -v embarrassing ~/tmphistfile &gt;&gt; ~/.bash_history
# re-point your history file to the right one, or just exit the shell
</pre>

[Matt Simmons][3] thought a little oops utility would be nice. So here is my shoot from the hip attempt, haven&#8217;t extensively tested it but I think it works.

<pre class="brush: bash; title: ; notranslate" title="">#!/bin/bash
# wipe your history of lines that match the input
# Usage: oops &lt;embarrassing string&gt;

TEMPHIST=$(mktemp)
export HISTFILE=$TEMPHIST
history -a
grep -v $1 $TEMPHIST &gt;&gt; ~/.bash_history
history -c
rm $TEMPHIST
HISTFILE=~/.bash_history
history -r
</pre>

 [1]: http://www.epoxyjournal.com/2010/05/how-to-clear-command-history-in-linux.html
 [2]: http://en.wikipedia.org/wiki/Godwin%27s_law
 [3]: http://www.standalone-sysadmin.com/blog