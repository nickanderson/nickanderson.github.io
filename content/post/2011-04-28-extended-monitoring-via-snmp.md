---
title: Extended monitoring via snmp
author: Nick Anderson
type: post
date: 2011-04-29T03:57:28+00:00
url: /2011/04/28/extended-monitoring-via-snmp/
categories:
  - Posts

---
Monitoring systems utilize agents running on the monitored system in order to provide a consistent access mechanism to get at host and application data. Hypric has an agent, Zabbix has an agent, Nagios has NRPE as an agent option, collectd has an agent. Maybe its just my flawed perception but when I think of agent based monitoring SNMP isn&#8217;t one of the first things that comes to mind. Apparently I am not alone, [in his blog on it.toolbox.com Andrew Kramer][1] goes so far as to call SNMP &#8220;agentless&#8221; monitoring. 

Really though, I consider SNMP the most ubiquitous agent. I think it gets overlooked because it is so ubiquitous. SNMP is on network hardware, and ships by default in many operating systems and distributions. Just because its installed by default doesn&#8217;t diminish the fact that its a daemon that facilitates data collection in a unified standard way. I mostly run Linux, so I&#8217;ll only speak to the [net-snmp/ucd-snmp][2] package. 

In addition to the standard OIDs that provide access to the process table, memory, and network usage net-snmp provides the exec and the more modern extend options to provide extended capabilities. Exec and extend parameters both execute custom commands. &#8220;Note that the &#8220;relocatable&#8221; form of the &#8216;exec&#8217; directive (exec OID &#8230;.) produces MIB output that is not strictly valid. For this reason, support for this has been deprecated in favour of extend OID &#8230; , which produces well-formed MIB results (as well as providing fuller functionality)&#8221; [[1][3]]. 

At any rate, its pretty easy to use. Just add a line like one of the following to your /etc/snmp/snmpd.conf or equivalent.

<pre class="brush: plain; title: ; notranslate" title="">extend yesterday /bin/date --date=yesterday
extend sayhi    /bin/echo hi
extend check_load /usr/lib64/nagios/plugins/check_load  -w 2,2,2 -c 4,4,4
</pre>

If we make these extend commands output in nagios plugin format they can easilybe integrated into nagios, or zenoss. I am sure that other monitoring frameworks support the nagios plugin output format as well.

At one point in the past I had found a nagios check script that was supposed to make it easy to query these extend monitors but I cant remember what I found, or why for whatever reason I couldn&#8217;t get it working. Well last night I [found a new script (check\_snmp\_extend.py) on the centreon.com][4] forums (random google result). It&#8217;s slightly annoying that registration was required to download the script, but I grabbed it. Luckily I don&#8217;t mind hacking on python. I went ahead and created a [github repository for check\_snmp\_extend][5] and fixed up a few things in it. Right now it only works with snmp extend, but adding snmp exec support would be a fairly easy addition I think.

The script makes extending snmp easy to deal with because you don&#8217;t need to manage the namespace for unique OIDs since it looks up values based on the name set for the snmp extend command. Based on the above example additions here is some example usage and output.

<pre class="brush: bash; title: ; notranslate" title="">$ ./check_snmp_extend.py -H test.example.org 
OK - ok objects: 3, not ok objects: 0 - check_load=OK, echohi=OK, yesterday=OK, 
$ ./check_snmp_extend.py -H test.example.org -e check_load
OK - load average: 0.01, 0.12, 0.07|load1=0.010;2.000;4.000;0; load5=0.120;2.000;4.000;0; load15=0.070;2.000;4.000;0; 
$ ./check_snmp_extend.py -H test.example.org -e yesterday
Wed Apr 27 22:58:20 CDT 2011
</pre>

Of course it would be best if all of your snmp extends output in the nagios plugin format.

 [1]: http://it.toolbox.com/blogs/network-mgt/agents-vs-agentless-redux-9810
 [2]: http://en.wikipedia.org/wiki/Net-SNMP#History
 [3]: http://www.net-snmp.org/wiki/index.php/FAQ:Agent_07
 [4]: http://forum.centreon.com/showthread.php/11216-check-snmp-extend-exec-%28check-custom-exec-snmp-return-values%29
 [5]: https://github.com/nickanderson/check_snmp_extend