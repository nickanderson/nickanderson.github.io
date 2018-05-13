---
title: Installing NRPE on XenServer
author: Nick Anderson
type: post
date: 2010-03-04T18:05:58+00:00
url: /2010/03/04/installing-nrpe-on-xenserver/
syntaxhighlighter_encoded:
  - 1
tweetlyUpdater_bitlyUrl:
  - http://bit.ly/9ygf5z
openid_comments:
  - 'a:5:{i:0;s:4:"1126";i:1;s:4:"1129";i:2;s:4:"1131";i:3;s:4:"1132";i:4;s:4:"1134";}'
categories:
  - Posts
tags:
  - nagios
  - nrpe
  - sysadmin
  - XenServer

---
I like to have as little run in dom0 as possible. However some things you really need checked from dom0, like the status of your raid perhaps. Just some quick instructions on getting Nagios NRPE running in XenServer.

  1. Install EPEL repository and disable it by default (remember we don&#8217;t want to accidentally install unnecessary packages) <pre class="brush: bash; title: ; notranslate" title="">wget http://download.fedora.redhat.com/pub/epel/5/$(uname -i)/epel-release-5-3.noarch.rpm
rpm -hiv epel-release*.rpm
sed -i 's/enabled=1/enabled=0/g' /etc/yum.repos.d/epel.repo
</pre>

  2. Install nrpe and configure it to start on boot <pre class="brush: bash; title: ; notranslate" title="">yum install --enablerepo=epel nrpe
chkconfig nrpe on
</pre>

  3. Modify the firewall to allow NRPE connections. Add the following before the REJECT line in /etc/sysconfig/iptables <pre class="brush: bash; title: ; notranslate" title="">-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 5666 -j ACCEPT
</pre>

  4. Restart your firewall and start nrpe <pre class="brush: bash; title: ; notranslate" title="">restart your firewall , and start nrpe
/etc/init.d/iptables restart && /etc/init.d/nrpe start
</pre>

  5. Configure nrpe like normal and have fun