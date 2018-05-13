---
title: Install git on CentOS cpanel server
author: Nick Anderson
type: post
date: 2010-05-08T03:05:12+00:00
url: /2010/05/07/install-git-on-centos-cpanel-server/
aktt_tweeted:
  - 1
openid_comments:
  - 'a:9:{i:0;s:4:"1103";i:1;s:4:"1121";i:2;s:4:"1124";i:3;s:4:"1149";i:4;s:4:"1156";i:5;s:4:"1182";i:6;s:4:"1184";i:7;s:4:"1193";i:8;s:4:"1197";}'
categories:
  - Posts
tags:
  - cpanel
  - git
  - sysadmin

---
I have a love/hate relationship with cpanel. On one hand it makes low end hosting a breeze, on the other its a huge pita if you want to do anything &#8220;outside the box&#8221;. Perhaps it&#8217;s not such a pain if you work with cpanel frequently. But I find cpanel beneficial because it aids in tasks that I don&#8217;t do frequently, and can offload many of those tasks to less technical people.

I was recently setting up a cpanel instance for someone and had the need to install git for version control. I configured the epel repository for use as usual and went to yum install git only to be met with a nasty error.

> <pre>git-1.5.5.6-2.el5.i386 from epel has depsolving problems
  --&gt; Missing Dependency: perl(Error) is needed by package 
git-1.5.5.6-2.el5.i386 (epel)
git-1.5.5.6-2.el5.i386 from epel has depsolving problems
  --&gt; Missing Dependency: perl-Git = 1.5.5.6-2.el5 is needed by package 
git-1.5.5.6-2.el5.i386 (epel)
git-1.5.5.6-2.el5.i386 from epel has depsolving problems
  --&gt; Missing Dependency: perl(Git) is needed by package 
git-1.5.5.6-2.el5.i386 (epel)
Error: Missing Dependency: perl(Git) is needed by package 
git-1.5.5.6-2.el5.i386 (epel)
Error: Missing Dependency: perl(Error) is needed by package 
git-1.5.5.6-2.el5.i386 (epel)
Error: Missing Dependency: perl-Git = 1.5.5.6-2.el5 is needed by package 
git-1.5.5.6-2.el5.i386 (epel)
</pre>

I was pretty surprised as I have installed git without issue before on CentOS boxes before. A bit of digging showed that installing cpanel actually made some modifications to my /etc/yum.conf.

> exclude=apache\* bind-chroot courier\* dovecot\* exim\* httpd\* mod_ssl\* mysql\* nsd\* perl\* php\* proftpd\* pure-ftpd\* ruby\* spamassassin\* squirrelmail*

So cpanel has blocked all perl packages from being installed or updated because they don&#8217;t want updates to break or conflict with their packages. Thankfully yum provides a nice one time workaround for this kind of situation.

> &#8211;disableexcludes=[repo]
  
> disable exclude from main, for a repo or for
  
> everything

So one command later and I now have git installed.

<pre class="brush: bash; title: ; notranslate" title="">yum --disableexcludes=main install git</pre>