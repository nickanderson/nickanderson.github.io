---
title: Sphinx init script for RHEL3
author: Nick Anderson
type: post
date: 2008-04-14T23:36:07+00:00
url: /2008/04/14/sphinx-init-script-for-rhel3/
categories:
  - Posts
tags:
  - init
  - redhat
  - rhel3
  - sphinx

---
Had some planned maintenance on one of our servers this weekend. After bringing the server back up I forgot to start searchd for sphinx. Don&#8217;t want that to happen again so I wrote a quick init script for searchd. <!--more-->

<!--adsense-->

<pre class="brush: bash; title: ; notranslate" title="">#!/bin/sh
#
# searchd      Start/Stop searchd.
#
# chkconfig: - 62 38
# description: sphinx searchd
#
# processname: searchd
#
# By: Nick Anderson - nick@anders0n.net
#
# Based on freshclam init by:
# (c) 2004/05/17 Petr@Kristof.CZ under GNU GPL 2.0+
#
# Updated 4/14/2008 to accomodate searchd
# 

# Source function library
. /etc/init.d/functions

# Get network config
. /etc/sysconfig/network

RETVAL=0

start() {
    echo -n $&amp;amp;quot;Starting searchd: &amp;amp;quot; 
    # Start me up!
    daemon --user root /usr/local/bin/searchd --config /usr/local/etc/sphinx.conf
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] &amp;amp;amp;amp;&amp;amp;amp;amp; touch /var/lock/subsys/searchd
    return $RETVAL
}

stop() {
    echo -n $&amp;amp;quot;Stopping searchd: &amp;amp;quot; 
    killproc searchd
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] &amp;amp;amp;amp;&amp;amp;amp;amp; rm -f /var/lock/subsys/searchd
    return $RETVAL
}    

restart() {
      stop
    start
}    

reload() {
    stop
    start
}

case &amp;amp;quot;$1&amp;amp;quot; in
  start)
      start
    ;;
  stop)
      stop
    ;;
  status)
    status searchd
    ;;
  restart)
      restart
    ;;
  condrestart)
      [ -f /var/lock/subsys/searchd ] &amp;amp;amp;amp;&amp;amp;amp;amp; restart || :
    ;;
  reload)
    reload
    ;;
  *)
    echo $&amp;amp;quot;Usage: $0 {start|stop|status|restart|condrestart|reload}&amp;amp;quot; 
    exit 1
esac

exit $?
</pre>

Then of course after I write it and get it working I notice there is a red hat init script in contrib in the src package. But mine works for me, feel free to use it if for some reason the one in contrib does not work for you.