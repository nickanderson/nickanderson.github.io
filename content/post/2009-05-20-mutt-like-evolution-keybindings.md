---
title: Mutt like evolution keybindings
author: Nick Anderson
type: post
date: 2009-05-21T02:44:29+00:00
url: /2009/05/20/mutt-like-evolution-keybindings/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - evolution
  - mutt

---
In preparation for connecting to (im guessing here) an Exchange server at my new job I am switching from my beloved Mutt to Evolution. The absolute first thing I noticed about Evolution that I disliked was the keybindings for things like deleting messages, replying to messages and creating a new message. After some digging in the UI I could not find any place to change them. Some more sleuthing turned up some XML files down in /usr/share/evolution/$VERSION/ui.<!--more-->

You can easily edit these files to your liking but be ware the changes are global. Either I have missed how you can override these settings on a per user basis or there have been some major oversights from the evolution development team. At any rate I&#8217;ve only made a few changes so far but I wanted to share them for anyone else who would prefer to use Mutt but is stuck connecting to an Exchange server.

@@ -58,6 +58,7 @@

<cmd name="MessageDelete" _tip="Mark the selected messages for deletion" + accel="d" pixtype="pixbuf"/>

<cmd name="MessageFollowUpFlag" @@ -67,7 +68,7 @@ <cmd name="MessageForward" _tip="Forward the selected message to someone" - accel="\*Control\*f" + accel="f" pixtype="pixbuf"/>

<cmd name="MessageForwardAttached" @@ -98,12 +99,12 @@ <cmd name="MessageMarkAsJunk" _tip="Mark the selected messages as junk" - accel="\*Control\*j" + accel="j" pixtype="pixbuf"/>

<cmd name="MessageMarkAsNotJunk" _tip="Mark the selected messages as not being junk" - accel="\*Control\*\*Shift\*j" + accel="J" pixtype="pixbuf"/>

<cmd name="MessageFilterJunk" @@ -113,7 +114,7 @@ <cmd name="MailCompose" _tip="Open a window for composing a mail message" pixtype="pixbuf" - accel="\*Control\*\*Shift\*m"/>
  
+ accel=&#8221;m&#8221;/>

<cmd name="MessageMove" _tip="Move selected messages to another folder" @@ -136,11 +137,11 @@ <cmd name="MessageRedirect" _tip="Redirect (bounce) the selected message to someone" - accel=""/>
  
+ accel=&#8221;b&#8221;/>

<cmd name="MessageReplyAll" _tip="Compose a reply to all of the recipients of the selected message" - accel="\*Control\*\*Shift\*r" + accel="g" pixtype="pixbuf"/>

<cmd name="MessageReplyList" @@ -149,7 +150,7 @@ <cmd name="MessageReplySender" _tip="Compose a reply to the sender of the selected message" - accel="\*Control\*r" + accel="r" pixtype="pixbuf"/>

<cmd name="MessageSaveAs" [/code]