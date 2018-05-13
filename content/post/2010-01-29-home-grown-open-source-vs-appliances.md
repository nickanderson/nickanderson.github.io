---
title: Home Grown / Open Source vs Appliances
author: Nick Anderson
type: post
date: 2010-01-29T17:52:12+00:00
url: /2010/01/29/home-grown-open-source-vs-appliances/
syntaxhighlighter_encoded:
  - 1
has_been_twittered:
  - yes
categories:
  - Posts
tags:
  - Discussions
  - spamassassin

---
The last few days I have been having a pretty good debate with a friend about the virtues of open source vs Appliances. At times its gotten pretty heated but its all in good fun. The current debate centers around email infrastructure. There are options on the table to use an appliance, or a 3rd party service to control the spam. Of course I was appalled that SpamAssassin and brethren were not on the table.<!--more-->Don&#8217;t get me wrong, I am a lazy bastard and appliances can be great. But there are budget crunches all over the place and saving money is important. Sure, implementing an open source solution can be costly in man hours. But a licensed product is guaranteed costly over the long term. The debate went into the gutter so far as to say no one uses SpamAssassin. I of course rebutted with the list of 

[commercial appliances that run SpamAssassin][1], [services that use SpamAssassin][2] that use SpamAssassin as at least one tool. I&#8217;m not saying that SpamAssassin alone will fulfill all of your filtering needs by any means. But I do believe that if someone can ship an appliance or base a service off of mail filtering, that I can build something comprised of open source tools that can do the job at least as well. Granted it may not have a slick interface but it will work, and its maintenance cost is sunk because you are already paying me to do other things.

This is a belief that permeates my being. If the tools are available I can stick them together to make something. I&#8217;m not a developer, but I can even write things myself to a limited degree. I don&#8217;t think that I could write a hypervisor, but I know I can use the opensource Xen hypervisor just as well as I can use the Citrix provided Xenserver. I don&#8217;t think I could write my own spam filter, but I know I go for weeks without getting a single spam in my inbox and I am only running SpamAssassin on my mail server.

Whats your take? Remember I love appliances because they do make life easy. The premise here is that opensource products work just as well as commercial counterparts and that in time of increasingly shrinking budgets it can make sense to maintain these infrastructures yourself.

 [1]: http://wiki.apache.org/spamassassin/CommercialNetworkAppliances
 [2]: http://wiki.apache.org/spamassassin/SpamFilteringServices