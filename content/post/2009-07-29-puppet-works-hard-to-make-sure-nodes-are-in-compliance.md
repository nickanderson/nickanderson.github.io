---
title: Puppet works hard to make sure nodes are in compliance
author: Nick Anderson
type: post
date: 2009-07-30T04:57:02+00:00
url: /2009/07/29/puppet-works-hard-to-make-sure-nodes-are-in-compliance/
syntaxhighlighter_encoded:
  - 1
categories:
  - Posts
tags:
  - Puppet

---
I&#8217;ve been working with puppet a lot in the last few weeks. I really enjoy this style of administration compared to &#8220;ssh in a for loop&#8221;. Its great to script things and I still do it but for maintaining configuration I don&#8217;t know if it gets much better than puppet. That being said I ran into a few issues today that had me splitting my head open on my desk, keyboard, pop cans and just about everything else I could reach.

It&#8217;s standard practice to keep your puppet configuration in version control and I am doing this with subversion. It provides a central authority with log history so we can audit why changes were made. It&#8217;s also handy for my co-workers to be able to use tortisesvn on their windows clients to update configuration. Be careful with that! I do all of my editing in vim and neglected to take into account what using various editors might do to my puppet configuration. Today as we were testing some puppet configurations and I was showing co-workers how to add new nodes to the puppet cluster this bit me right in the soft bits.

My co-worker added a new node by copy and pasting a previous node definition and updating the node name. Of course he did this with notepad in windows. We noticed when we ran puppetd &#8211;test on the new node that it failed with a parser error. It complained about a missing } at line one of our nodes.pp. This was very odd since he was editing the bottom of the file. I opened the file in vim and everything looked right. I could find no such missing curly braces. I went ahead and removed his node definition and ran puppetd &#8211;test again. Not surprisingly the node complained of having no definition (I did not have a default node setup). I re-added the node definition and again the node was successful. I initially chalked this up to some error I must have missed in the node definition. But when my co-worker added more nodes and we saw the same behavior it was obvious there was a different issue going on. Now you would think this would be an easy conclusion to draw but that was not the case for me, at least it wasn&#8217;t today.

I noticed that after he added a node if I called in with an already configured node that node would complain about the same parse error. However if I called in again it would receive its configuration just fine and it would say it was ignoring the cache. I saw nothing exceptional in the puppetmaster logs. Of course the same parser error was there the first time a node called in to get its configuration after he altered it with a windows editor but all subsequent call ins of previously configured nodes succeeded. After I noticed this pattern things started coming together. To complicate my troubleshooting I started trying to restart puppetmasterd. This at first sent me for a tail spin. After puppet master was restarted with the file that had been updated with notepad on windows ALL node call ins were failing. No longer was it only the first time. Eventually this lead me to the conclusion. Puppetmasterd works very hard to make sure that your clients get served a valid configuration. If you update the config and do not restart puppetmasterd and that new config is invalid puppetmasterd appears to serve up the previous version of the config that it knew worked. This was all well and dandy and probably a desirable behavior. My issue is that the logs didn&#8217;t appear to say &#8220;Hey by the way I see you jacked up your puppet config. This config wont work dummy, Im going to go ahead and serve up your last config since it works.&#8221;. I saw no mention of this behavior in the docs but perhaps I missed something.

The moral of the story. Don&#8217;t use windows to edit your puppet configs and if you do use vim for windows. Secondary to that test! test! and test some more. Its pretty easy to screw up some syntax and have things start breaking on you.