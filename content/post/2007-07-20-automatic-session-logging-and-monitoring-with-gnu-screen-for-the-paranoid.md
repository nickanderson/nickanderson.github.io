---
title: Automatic session logging and monitoring with GNU screen for the paranoid.
author: Nick Anderson
type: post
date: 2007-07-20T14:07:53+00:00
url: /2007/07/20/automatic-session-logging-and-monitoring-with-gnu-screen-for-the-paranoid/
categories:
  - Posts
tags:
  - logging
  - screen
  - security
  - session
  - tip

---
Yes its been a while since I have checked in. Sorry I&#8217;ve just been too busy. But I have a great tip this time. Recently I had the need to do automatic session logging. A 3rd party was going to be logging into one of my servers to check out some software glitches that were happening. I love using GNU Screen for many shell tasks so using it for monitoring was logical. Screen is great for several reasons. First you can detach from it so you can leave the office, go home and re-attach and not have lost your place. Second, you can share another screen. It can be shared input or you can just watch what someone else is doing. Finally screen can do native logging. I wanted to automattically launch a screen session when somone logged in so if I happened to be on the server I could monitor them in real time. I also wanted a log of the session in case I wanted to look over it later or if I was not able to monitor the session live.
  
<!--more-->


  
<!--adsense-->


  
I ended up adding the following to my .bashrc

<pre># -- if $STARTED_SCREEN is set, don't try it again, to avoid looping
# if screen fails for some reason.
if [[ "$PS1" &&; "${STARTED_SCREEN:-No}" = No && "${SSH_TTY:-No}" != No ]]; then
STARTED_SCREEN=1 ; export STARTED_SCREEN
if [ -d $HOME/log/screen-logs ]; then
sleep 1
screen -RR && exit 0
echo "Screen failed! continuing with normal bash startup"
else
mkdir -p $HOME/log/screen-logs
fi
# [end of auto-screen snippet]</pre>

Lets go through that &#8230;..

<pre>if [[ "$PS1" && "${STARTED_SCREEN:-No}" = No && "${SSH_TTY:-No}" != No ]]</pre>

If I have some title at my terminal and if STARTED\_SCREEN is set and non-null, (expands to $STARTED\_SCREEN. Otherwise, expands to No.) and if SSH_TTY is set and not null, then we can attempt to create the screen.
  
$SSH_TTY is set when you ssh in, it should not be tripped by scp or sftp logins either.
  
<code lang="bash">&lt;br />
then&lt;br />
STARTED_SCREEN=1 ; export STARTED_SCREEN&lt;br />
</code>
  
Here STARTED_SCREEN is set so that we dont loop on login creating a ton of screens.

<pre>if [ -d $HOME/log/screen-logs ]; then</pre>

if the directory is present

<pre>#sleep 1
screen -RR && exit 0
# normally, execution of this rc script ends here...
echo "Screen failed! continuing with normal bash startup"</pre>

Attempt to reattach any unattached screens. If there are no screens to be attached then make one and attach to it.

And I added the following to my .screenrc

<pre># support color X terminals
termcap xterm 'XT:AF=\E[3%dm:AB=\E[4%dm:AX'
terminfo xterm 'XT:AF=\E[3%p1%dm:AB=\E[4%p1%dm:AX'
termcapinfo xterm 'XT:AF=\E[3%p1%dm:AB=\E[4%p1%dm:AX:hs:ts=\E]2;:fs=\007:ds=\E]2;screen\007'
termcap xtermc 'XT:AF=\E[3%dm:AB=\E[4%dm:AX'
terminfo xtermc 'XT:AF=\E[3%p1%dm:AB=\E[4%p1%dm:AX'
termcapinfo xtermc 'XT:AF=\E[3%p1%dm:AB=\E[4%p1%dm:AX:hs:ts=\E]2;:fs=\007:ds=\E]2;screen\007'

# detach on hangup
autodetach on
# no startup msg
startup_message off
# always use a login shell
shell -$SHELL

# auto-log
logfile $HOME/log/screen-logs/%Y%m%d-%n.log
deflog on</pre>

Most of this is self explanatory the log file for auto logging and deflog on are what give you your fun logs to look over later.

You might also want to do some logrotate on the logs or some script to expire logs that are x days old. If you forget about them over time they may try to eat your file system.

Note: I picked this up somewhere else a while back i just don&#8217;t remember exactly where. I modified it slightly to make it more readable but the credit goes to the original author. I think it was http://taint.org/wk/RemoteLoginAutoScreen.