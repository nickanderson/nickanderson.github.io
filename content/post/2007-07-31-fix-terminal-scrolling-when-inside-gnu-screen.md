---
title: Fix terminal scrolling when inside GNU Screen
author: Nick Anderson
type: post
date: 2007-07-31T17:52:56+00:00
url: /2007/07/31/fix-terminal-scrolling-when-inside-gnu-screen/
categories:
  - Posts
tags:
  - fix
  - gnu screen
  - linux
  - screen
  - scrolling
  - terminal

---
My post on <a href="http://www.cmdln.org/2007/07/20/automatic-session-logging-and-monitoring-with-gnu-screen-for-the-paranoid/" mce_href="http://www.cmdln.org/2007/07/20/automatic-session-logging-and-monitoring-with-gnu-screen-for-the-paranoid/"> Automatic session logging and monitoring with GNU screen</a> seems to have been well received. I have had more hits by far on that post today than ever before. I noticed a nagging issue with screen and a friend of mine Travis Cline pointed me to the fix. <!--more-->


   
Isnt it annoying when your in screen and cant use the scroll wheel to scroll up in your buffer? The fix does not work well when you are using multiple windows inside a single screen especially when using split mode but for the times you use one window per screen its pretty handy.

Add the following to your .screenrc.

`My post on <a href="http://www.cmdln.org/2007/07/20/automatic-session-logging-and-monitoring-with-gnu-screen-for-the-paranoid/" mce_href="http://www.cmdln.org/2007/07/20/automatic-session-logging-and-monitoring-with-gnu-screen-for-the-paranoid/"> Automatic session logging and monitoring with GNU screen</a> seems to have been well received. I have had more hits by far on that post today than ever before. I noticed a nagging issue with screen and a friend of mine Travis Cline pointed me to the fix. <!--more-->


   
Isnt it annoying when your in screen and cant use the scroll wheel to scroll up in your buffer? The fix does not work well when you are using multiple windows inside a single screen especially when using split mode but for the times you use one window per screen its pretty handy.

Add the following to your .screenrc.

`