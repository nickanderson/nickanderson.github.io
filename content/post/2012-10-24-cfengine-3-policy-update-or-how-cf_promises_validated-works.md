---
title: CFEngine 3 Policy Update or How cf_promises_validated Works
author: Nick Anderson
type: post
date: 2012-10-25T02:07:09+00:00
url: /2012/10/24/cfengine-3-policy-update-or-how-cf_promises_validated-works/
categories:
  - Posts
tags:
  - CFEngine
  - cf_promises_validated
  - failsafe.cf
  - update.cf

---
Over the past <del>several months</del> 2 years (since 3.1.2 release, wow time flys when your having fun. I checked and <a href="https://cfengine.com/cftimes/articles/0000000047.html" target="_blank">3.1.2</a>[<img class="alignright size-medium wp-image-1098" title="Little question" src="http://www.cmdln.org/images/wp-content/uploads/2012/10/question-mark-240x300.jpg" alt="" width="240" height="300" srcset="http://www.cmdln.org/images/wp-content/uploads/2012/10/question-mark-240x300.jpg 240w, http://www.cmdln.org/images/wp-content/uploads/2012/10/question-mark.jpg 310w" sizes="(max-width: 240px) 100vw, 240px" />][1] <a href="https://cfengine.com/cftimes/articles/0000000047.html" target="_blank">was released</a> on Dec 9th 2010.) I have <a href="https://groups.google.com/forum/?hl=en&fromgroups=#!topic/help-cfengine/MD0w02t4dQc" target="_blank">seen</a> <a href="https://cfengine.com/forum/read.php?3,27307" target="_blank">a</a> <a href="https://cfengine.com/forum/read.php?6,26918,27451#msg-27451" target="_blank">few</a> <a href="https://cfengine.com/forum/read.php?3,26246,26259#msg-26259" target="_blank">questions</a> regarding how the default CFEngine policy update works, and more specifically how cf\_promises\_validated plays into the update process. This is my stab at describing the history and behaviour. I welcome any corrections.

The default failsafe.cf update policy is simple in nature. (We could probably debate what is <a title="Strangeloop 2011 - Rich Hickey - Simple Made Easy" href="http://www.infoq.com/presentations/Simple-Made-Easy" target="_blank">simple</a> or <a title="Complex vs Complicated" href="http://www.cmdln.org/2012/07/13/complex-vs-complicated/" target="_blank">complex</a>, but I am comfortable with the label in this case.) Agents copy policy from /var/cfengine/masterfiles on the policy hub, to /var/cfengine/inputs. This is the same for all agents, even the agent that runs on the policy hub, the only difference is that since the files are already local on the policy hub they don&#8217;t have to go over the network, but they are still copied from the same source, to the same destination.

The 3.1.2 release was an efficiency related release. One of the enhancements was the introduction of cf\_promises\_validated. <a title="Meet the CFEngine Team - Eystein Måløy Stenberg" href="http://cfengine.com/blog/meet-the-cfengine-team-eystein" target="_blank">Eystein</a> wrote a <a title="3.1.2 Extended Change Log" href="http://www.blogcompiler.com/2010/12/29/cfengine-3-1-2-extended-change-log/" target="_blank">great extended change log</a> on his blog covering the release including a section on cf\_promises\_validated which is where I first learned of the feature and how to use it. Again, the cf\_promises\_validated mechanism is simple in nature. From his post &#8220;this file (/var/cfengine/masterfiles) is created by `cf-agent` or any other CFEngine component after it has successfully verified the policy with `cf-promises`.&#8221; What I think is missing from this description is that /var/cfengine/masterfiles is created/updated when policy has been verified **<span style="text-decoration: underline;">after</span>** the policy has changed (so it&#8217;s not supposed to update this file every execution, there <a href="https://cfengine.com/bugtracker/view.php?id=1258" target="_blank">seems to be a bug</a> with this but that is not expected behaviour). I do not know what constitutes change but I suspect it&#8217;s some variation of a tripwire policy similar to the following. Remember this is a simple mechanism and is the same for <span style="text-decoration: underline;"><strong>any</strong></span> agent, policy hub or not.

<pre style="padding-left: 30px;">files:
  any::
    "/var/cfengine/masterfiles"
      changes      =&gt; detect_all_change,
      depth_search =&gt; recurse("inf"),
      classes      =&gt; if_repaired("cf_promises_validated");

  cf_promises_validated::
    "/var/cfengine/masterfiles/cf_promises_validated"
      create =&gt; "true",
      touch  =&gt; "true";</pre>

The difference between a policy hub (am\_policy\_hub) and a non policy hub as I understand it is determined by comparing the contents of /var/cfengine/policy\_server.dat to the ips/hostnames associated with the interfaces on the system. If the policy server found in policy\_server.dat file resolves to an ip on the current system, it raises the am\_policy\_hub class. This am\_policy\_hub class is used in the default failsafe.cf update policy to determine when to copy files from /var/cfengine/masterfiles on the policy hub to /var/cfengine/inputs (locally to the executing agent).

Initially cf\_promises\_validated was an empty file, and mtime was used to determine if the file was newer. This was problematic for hosts that had time skews and a time stamp was introduced in <a title="CFEngine 3.3.0 Release Notes" href="https://cfengine.com/blog/cfengine-330-release-notes" target="_blank">3.3.0</a> so that digest could be used to determine difference more accurately. The fact that a time value is now stored in the file is only relevant to a human reading the file.

Spend a few minutes reading this snippet from the default update policy.

<pre>01 files:
02  
03  !am_policy_hub::  # policy hub should not alter inputs/ uneccessary
04
05   "$(inputs_dir)/cf_promises_validated"
06        comment =&gt; "Check whether a validation stamp is available for a new policy update to reduce the distributed load",
07         handle =&gt; "update_files_check_valid_update",
08      copy_from =&gt; u_rcp("$(master_location)/cf_promises_validated","$(sys.policy_hub)"),
09         action =&gt; u_immediate,
10        classes =&gt; u_if_repaired("validated_updates_ready");
11 
12   "$(modules_dir)"
13          comment =&gt; "Always update modules files on client side",
14           handle =&gt; "update_files_update_modules",
15        copy_from =&gt; u_rcp("$(modules_dir)","$(sys.policy_hub)"),
16     depth_search =&gt; u_recurse("inf"),
17            perms =&gt; u_m("755"),
18           action =&gt; u_immediate;
19
20  am_policy_hub|validated_updates_ready::  # policy hub should always put masterfiles in inputs in order to check new policy
21
22   "$(inputs_dir)"
23           comment =&gt; "Copy policy updates from master source on policy server if a new validation was acquired",
24            handle =&gt; "update_files_inputs_dir",
25         copy_from =&gt; u_rcp("$(master_location)","$(sys.policy_hub)"),
26      depth_search =&gt; u_recurse("inf"),
27      file_select  =&gt; u_input_files,
28            action =&gt; u_immediate,
29           classes =&gt; u_if_repaired("update_report");</pre>

The first thing that happens is for non policy hubs (line 3 starts the context class restriction, and line 5 begins the promiser). /var/cfengine/inputs/cf\_promises\_validated is checked against /var/cfengine/masterfiles/cf\_promises\_validated on the policy hub. If the file is different it is copied down and the validated\_updates\_ready class is defined. Skipping down to line 20 a new context class is defined for policy hubs or for agents which have validated that updates are ready (their cf\_promises\_validated in /var/cfengine/inputs was different from the cf\_promises\_validated file in /var/cfengine/masterfiles on the policy hub). If either of those classes are defined the agent recursively scans /var/cfengine/masterfiles on the policy hub and copies files that are different to /var/cfengine/inputs locally on the executing agent.

So, policy hubs <span style="text-decoration: underline;"><strong>always</strong></span> perform this update and copy files that are different from /var/cfengine/masterfiles to /var/cfengine/inputs. and non policy hubs only update /var/cfengine/inputs from /var/cfengine/masterfiles on the policy hub if cf\_promises\_validated has changes. The hub must always perform this update if you recall how cf\_promises\_validated is created/updated. New policy that successfully validates in /var/cfengine/inputs triggers cf\_promises\_validated to be updated in /var/cfengine/masterfiles. Agents need to see that file be different from the cf\_promises\_validated file in /var/cfengine/inputs in order to trigger a full policy update.

If its still not clear, read it a few more times. Things are usually pretty hard until they aren&#8217;t :). I recall reading the extended change log from 3.1.2 several times, as well as the example policy until I thought I had a good grasp on the flow. I hope you find this useful and I expect that this post will become less useful in the near future. I have filed a <a href="https://cfengine.com/dev/issues/1541#change-5063" target="_blank">bug</a> requesting better documentation coverage of the default update policy.

 [1]: http://www.cmdln.org/images/wp-content/uploads/2012/10/question-mark.jpg