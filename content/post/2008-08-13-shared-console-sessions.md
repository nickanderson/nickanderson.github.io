---
title: Shared console sessions
author: Nick Anderson
type: post
date: 2008-08-14T01:14:34+00:00
url: /2008/08/13/shared-console-sessions/
categories:
  - Posts
tags:
  - screen
  - shared command line
  - shared console
  - shared session
  - shared terminal

---
I have had several posts regarding screen. Hopefully you have already realized the greatness of screen. Screen has a great feature that allows screen sessions to be shared. To my knowledge there are two ways to use this feature. First you can connect to a screen multiple times as the same user. Second you can use the multiuser mode of screen.<!--more-->

Obviously the first option is less helpful in a multi user environment as one has to wheel up to a different user to share a screen. At first glance screens multiuser mode seems to be a great option. However multiuser mode requires that screen be setuid. Hopefully you are well aware of the dangers of running setuid processes. I will not drive the point home any more. If you still wish to use multiuser mode on screen by all means proceed.

I assume you have already installed screen. To enable multiuser mode log in to your machine

`sudo setuid /usr/bin/screen<br />
sudo chmod 755 /usr/bin/screen`

now run screen as your normal user. Then enable multi user mode with C-a :multiuser on. And allow the user joe to connect to your session with C-a :addacl joe (optional password)

Now user joe can see what screens you have available with
  
`screen -ls youruser/`
  
and joe could connect to a screen with
  
`screen -x youruser/(optional name of session)`

For those of you who yearn for a better way to share a session without the setuid stay tuned for the next post where we actually address this issue.