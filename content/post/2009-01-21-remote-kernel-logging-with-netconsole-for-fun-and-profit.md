---
title: Remote kernel logging with netconsole for fun and profit
author: Nick Anderson
type: post
date: 2009-01-21T16:36:19+00:00
url: /2009/01/21/remote-kernel-logging-with-netconsole-for-fun-and-profit/
aktt_notify_twitter:
  - no
aktt_tweeted:
  - 1
openid_comments:
  - 'a:1:{i:0;s:3:"781";}'
categories:
  - Posts
tags:
  - logging
  - netconsole

---
Have you ever experienced hard lockups and seen no trace of the cause in your log files? Those situations can be even more of a pain if you do not have physical access to the machine since you will not be able to look for kernel oops on the console. You could buy a serial console or an ip kvm but if you don&#8217;t have the need for remote control, but would really like to be able to debug without being physically present you need to check out netconsole. Netconsole sends printk messages over UDP. <!--more-->

Setting up netconsole is not difficult but the syntax can be a bit tiresome. Netconsole needs several bits of information in order to function properly.

  * **dev_name** &#8211; Local network interface name
  * **local_port** &#8211; Source UDP port to use
  * **remote_port** &#8211; Remote agent&#8217;s UDP port
  * **local_ip** &#8211; Source IP address to use
  * **remote_ip** &#8211; Remote agent&#8217;s IP address
  * **local_mac** &#8211; Local interface&#8217;s MAC address
  * **remote_mac** &#8211; Remote agent&#8217;s MAC address
Of those remote_mac tends to be the tricky one. Not because its hard to get but because it is slightly mis-leading. If the remote agent is in the same subnet its the mac of the remote agent, but if the remote agent is not in the same subnet (think logging over internet) then you really need the mac address of the gateway that will handle the traffic (if you have multiple wans). Typically your looking for the mac of your default gateway.

Find MAC of remote agent in same subnet

<pre class="brush: bash; title: ; notranslate" title="">REMOTE_AGENT=172.16.0.1
MAC=$(ping -c 1 $REMOTE_AGENT &gt; /dev/null ; arp -n $REMOTE_AGENT | grep ^$REMOTE_AGENT | awk '{print $3}')
echo Remote MAC: $MAC
</pre>

Find MAC of default gw

<pre class="brush: bash; title: ; notranslate" title="">GATEWAY=$(netstat -rn | awk '/^0.0.0.0/ {print $2}')
MAC=$(ping -c 1 $GATEWAY &gt; /dev/null ; arp -n $GATEWAY | grep ^$GATEWAY | awk '{print $3}')
echo Remote MAC: $MAC
</pre>

Initialize netconsole
  
Now you should have enough information to go ahead and initalize netconsole so lets give it a test

<pre class="brush: bash; title: ; notranslate" title="">modprobe netconsole netconsole=local_port@local_ip/dev_name,remote_port@remote_ip/remote_mac
</pre>

Now we still need to get something listening on the remote and test if it actually works. Log into your remote machine and run

<pre class="brush: bash; title: ; notranslate" title="">nc -l -p remote_port -u | tee  somelogfile.log
</pre>

For a more permanent setup you might want to use syslog but this will suffice for now. If it&#8217;s a short term but long running test you might be well advised to run that from a screen session.

Good now we have the remote listening on udp with netcat. We should make sure that the messages are getting logged. Log back into the machine thats running netconsole (local_ip) and run the following.

<pre class="brush: bash; title: ; notranslate" title="">dmesg -n 8
</pre>

This will increase the number of things that get logged.
  
Now find an innocuous kernel module that you can load and unload (i like to use floppy)

<pre class="brush: bash; title: ; notranslate" title="">rmmod floppy (in case its already loaded)
modprobe floppy
</pre>

You should have seen some output on your remote machine that looks something like

<pre class="brush: bash; title: ; notranslate" title="">Floppy drive(s): fd0 is 1.44M
FDC 0 is a post-1991 82077
</pre>

Great now you have netconsole working! If you get kernel oops your remote box should display it and log it to a file as well.

Want to make netconsole active through reboots? No problem we just need to edit a few files.

First lets get netconsole loading on boot by adding the module to /etc/modules

<pre class="brush: bash; title: ; notranslate" title="">echo "netconsole" &gt;&gt; /etc/module
</pre>

That was easy enough, but we need to make sure it has the proper options as well so lets add the module options to /etc/modprobe.d/netconsole

<pre class="brush: bash; title: ; notranslate" title="">echo "options netconsole netconsole=local_port@local_ip/dev_name,remote_port@remote_ip/remote_mac" &gt; /etc/modprobe.d/netconsole
</pre>

That should do it. Go ahead and try rebooting the machine running netconsole and watch your remote to see the boot msgs that happen after netconsole loads.

Note: there is a dynamic way to specify how netconsole is configured but you need to have CONFIG\_NETCONSOLE\_DYNAMIC in your kernel and since debian etch does not have this by default I wont cover it here. For more information check out the netconsole doc in the kernel source /usr/src/linux/Documentation/networking/netconsole.txt.

Now if you would like to make the remote side a bit more permanent thats pretty easy as well. Lets install and configure syslog-ng.

<pre class="brush: bash; title: ; notranslate" title="">aptitude install syslog-ng
</pre>

append the following to your /etc/syslog-ng/syslog-ng.conf
  
Note: make sure your set remote_port as you did above

<pre class="brush: bash; title: ; notranslate" title="">source net { udp(ip("0.0.0.0") port(remote_port)); };
destination netconsole { file("/var/log/$HOST/netconsole.log"); };
log { source(net); destination(netconsole); };
</pre>

Now restart syslog-ng

<pre class="brush: bash; title: ; notranslate" title="">/etc/init.d/syslog-ng restart
</pre>

Now you should be able to find the logs in /var/log/local\_ip/netconsole.log on your remote machine. Note: local\_ip is the ip of the machine that was running netconsole