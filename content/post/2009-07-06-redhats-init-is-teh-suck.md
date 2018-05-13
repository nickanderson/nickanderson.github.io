---
title: 'Redhats&#8217; init is teh suck'
author: Nick Anderson
type: post
date: 2009-07-07T00:56:27+00:00
url: /2009/07/06/redhats-init-is-teh-suck/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - centos
  - initscript
  - rant
  - redhat

---
I recently had to write an init script for our continuous integration systems remote build agent. Of course this agent is a java jar and does not write its own pidfile. On debian or gentoo (yes I used to rice it) this would not have been an issue. Both have and use start-stop-daemon in their init scripts. start-stop-daemon actually understands that not every process you might want to daemonize writes its own pidfile and thus gives you the ability to daemonize a process, capture its pid, and write a pidfile.

Oh, but not on redhat/centos. No, they have daemon(), which really doesnt do much of anything. <pompus voice> Each process must write its own pidfile </pompus voice>. Well I already have a custom init script, I really don&#8217;t want to write a custom wrapper, nor do I want to add yet another dependency to what ought to be a simple task. Perhaps I just don&#8217;t see the proper way to do this so I welcome solutions. This feature lack causes lines like this to show up in init scripts.

<pre>PID=$(pgrep -n -f "$LAUNCH_CMD")</pre>

I don&#8217;t know about you but that is horribly ugly and error prone in my eyes.

## chkconfig, the other suck.

Yes its documented that the tags chkconfig and description are required or your init script will not support chkconfig. That&#8217;s all fine and dandy. I copied my init template from /usr/share/doc/initscripts-8.45.25/sysvinitfiles. It has doc at the end of the initscript after exit is run. This is perfectly valid. There is nothing that is going to cause issues with the execution of the script. I left that doc there as I was developing my script. When it came time to chkconfig &#8211;add my script it continually failed. Granted it only took me a few minutes to figure out but what fixed it? Oh yes by removing all the doc at the end of the file. Why is this conflicting with chkconfig no reason that I can see to make it just not work. It would make a bit more sense if the example tags below just overrode the ones at the top of the file.