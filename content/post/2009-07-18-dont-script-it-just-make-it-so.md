---
title: 'Don&#8217;t script it, just make it so'
author: Nick Anderson
type: post
date: 2009-07-18T06:00:21+00:00
url: /2009/07/18/dont-script-it-just-make-it-so/
syntaxhighlighter_encoded:
  - 1
openid_comments:
  - 'a:3:{i:0;s:3:"902";i:1;s:3:"936";i:2;s:3:"937";}'
categories:
  - Posts
tags:
  - Puppet
  - structured systems management

---
[Matt Simmons][1] recently had another post that mentioned structured systems management. I find myself re-reading [Ad-Hoc vs Structured Systems Management][2] from time to time and I figure its time for me to chime in.

First off, <a rel="nofollow" href="http://www.blogger.com/profile/00357905802460949707">Michael Janke</a>s&#8217; post is one of my favorite blog post reads. Few posts do I ever re-read unless its tutorialesque. For a quick sidetrack one of those posts that I do return to when I deal with developers is [The Joel Test: 12 Steps to Better Code][3]. Back on subject &#8230;

One of the most frequent things that comes up when people start talking about good administration practices is scripting things. [If you can&#8217;t script it make a checklist][4] is a common sentiment. It&#8217;s not that I don&#8217;t think that scripting things is a good idea because I do. I would go so far to say that scripting things is an important part of documentation. You should be able to reproduce a system from documentation. Any configuration that can be done programatically should be and it should be in your documentation so in case of catastrophic failure someone can reproduce your work relatively easily. If I like scripting so much why is this post titled &#8220;Don&#8217;t script it&#8221;?

I think there is a better way. Use a configuration management system. Declare your configuration and allow the configuration management system to make it happen. This has many advantages over simply scripting something. Configuration can be enforced over time. I know I have been guilty of making small changes to configurations to see how things go. While those small changes seem to trickle into production systems they never (or at least rarely) seem to trickle into the documentation. Before you know it you have a pile of undocumented small changes that really encompass an entirely different configuration from what you started with.

A well placed configuration management system helps avoid these issues. Store your configuration in version control. I might even go so far as to say to automate the update of the checkout your configuration management server uses so that you don&#8217;t allow yourself to make small changes to the management system configuration without checking it into your version control. A few tweaks being automatically removed will go a long way to drive home the point that your changes need to be in version control. Placing your config in version control also allows you to see your changes over time. You can look back through the log and your comments to see when and why changes were made. This can be especially important if you are not the only person making changes to configuration (ah hem Matt, I know your hiring someone you better version your config before your no longer the lone admin).

This all comes up because I have been doing more work with [puppet][5] recently. It takes a while to wrap your head around but I don&#8217;t really think I have heard any arguments against that type of system being the &#8220;right&#8221; way to do systems administration. If I have they sure didn&#8217;t register. I like puppet because it works on a variety of systems and abstracts things like package management. I just tell my configuration system to make sure nodeX has package x installed and the puppet client figures out if its RH or Debian or SUSE or Solaris or whatever and runs the proper commands to get the package installed.

I am interested in [spacewalk][6] as well. But right now it only runs on Oracle databases so until it runs on postgresql there really isn&#8217;t even a point in me looking as the places I would be able to use it would be very limited.

 [1]: http://www.standalone-sysadmin.com/
 [2]: http://lastinfirstout.blogspot.com/2008/04/ad-hoc-verses-structured-system.html
 [3]: http://www.joelonsoftware.com/articles/fog0000000043.html
 [4]: http://www.standalone-sysadmin.com/blog/2009/07/if-you-cant-script-it-use-a-checklist/
 [5]: http://reductivelabs.com/products/puppet/
 [6]: http://www.redhat.com/spacewalk/