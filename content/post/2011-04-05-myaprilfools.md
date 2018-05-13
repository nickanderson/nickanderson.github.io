---
title: My April Fools
author: Nick Anderson
type: post
date: 2011-04-05T18:17:28+00:00
url: /2011/04/05/myaprilfools/
categories:
  - Posts
tags:
  - backups
  - fail
  - sysadmin
  - win

---
[<img src="http://www.cmdln.org/wp-content/uploads/2011/04/april-fool-illus-253x300.jpg" alt="" title="april fools" width="253" height="300" class="alignleft size-medium wp-image-832" srcset="http://www.cmdln.org/wp-content/uploads/2011/04/april-fool-illus-253x300.jpg 253w, http://www.cmdln.org/wp-content/uploads/2011/04/april-fool-illus.jpg 300w" sizes="(max-width: 253px) 100vw, 253px" />][1]April 1st. I had a fairly eventful day, first I found that the phone system at $work has been mis-configured since it was installed. Second I got a call from someone I had worked with a few years back about a system that did not have backups that had a raid hiccup tanking the system a few days ago needing help with a restore.

# The phone system

Several months back a new phone system was installed at my office. It has been a small nightmare ever since. Little issues seem to constantly pop up with it. I&#8217;ve had reports of people being unable to make long distance calls, but the error I recently found out is the default phone system error &#8220;Not enough lines&#8221;. So its unhelpful and misleading to say the least. We finally noticed that the errors were specific to long distance numbers with the same area code. So there seemed to be some issue with intralata calling.

I contacted the voice support team, provided them some testing phone numbers and got a ticket opened with the carrier. We all finally got on a conference call to troubleshoot the issue. The carrier said they weren&#8217;t getting the +1 and asked if 272 was in the local calling table to which voice support answered &#8220;Yes&#8221;. Everyone pretty much glazed over that statement because I had to point out that that is a long distanccd tme number. Thats when voice support said, &#8220;Yeah it looks like there are over 600 numbers in the local calling table.&#8221; Well, here in Lawrence KS there is no way that there are 600 nxx local numbers (nxx is the second set of digits, new info to me). So voice support removed the 272 number from the local calling table and now my test number started working. 

Naturally I asked the carrier to provide us a list of local nxx numbers so that we can fix our local calling table. I was surprised that between all the people on the phone from the carrier, none could provide the list. In fact they all seemed to think it would be extraordinarily difficult to get that list. Finally they provided me a link to a form on their website that should spit this info out for me. But of course this form was broken, and every number I tried said that no information was available in the database. Upon relaying that information the carrier proceeded to give me another website to use http://www.localcallingguide.com. Now I don&#8217;t know about you, but I don&#8217;t know how authoritative the data provided by Raymond Chow from Ontario Canada is. Luckily he does provide an xml query interface so I was able to figure out how to get the list I needed, and told the carrier I would use that for now, but they needed to provide an authoritative list by EOD Monday, its Tuesday and voice support says they still haven&#8217;t received the list. If the carrier cant tell you what numbers are local, then they have no business billing you for any long distance!

# What? No Backups?

My second April Fools day fun was the old &#8220;I have no backups, can you save me?&#8221; routine. 

[<img src="http://www.cmdln.org/wp-content/uploads/2011/04/PityTheFool-300x240.jpg" alt="" title="PityTheFool" width="300" height="240" class="alignright size-medium wp-image-834" srcset="http://www.cmdln.org/wp-content/uploads/2011/04/PityTheFool-300x240.jpg 300w, http://www.cmdln.org/wp-content/uploads/2011/04/PityTheFool.jpg 500w" sizes="(max-width: 300px) 100vw, 300px" />][2]The company I used to work for was sold and I helped them migrate to the new companies equipment. They had Xen installed on one dell server, and it ran several virtual machines to run the e-commerce website. Well that dell server has a PERC 6i controller, and 4 drives in a raid 5 (no spare). I know your probably thinking they dropped two drives, but no. They just dropped a single drive. I am pretty sure I have heard of rare data loss on those controllers with just a degraded set. Well thats what appears to have happened to them. The box went into a reboot loop, each time coming up it would kernel panic and reboot again. Did I mention there were NO backups?

We were able to bring up a recovery environment on a bootable USB key and we were able to salvage each virtual disk. Just had to go back through and re-assemble the virtual machines and do a few fix-ups to get everything working again. Unfortunately this consumed the majority of my weekend doing various imports and exports to and from the recovery environment and then the rebuilt production server. Hopefully the close call and several days of downtime even before I got involved will be enough to convince them its time to have backups and verify they work. 

I should point out one important thing. Backups are no good unless they are verified. During the recovery I exported three re-assembled virtual machines, all three exported without error but two of the three failed to import. I&#8217;m glad I tested them because if I had not no one would know the backups were faulty until they went to restore.

 [1]: http://www.cmdln.org/wp-content/uploads/2011/04/april-fool-illus.jpg
 [2]: http://www.cmdln.org/wp-content/uploads/2011/04/PityTheFool.jpg