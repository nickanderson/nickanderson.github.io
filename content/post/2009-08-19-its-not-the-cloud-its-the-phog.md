---
title: 'It&#8217;s not &#8220;the cloud&#8221; it&#8217;s &#8220;the phog&#8221;'
author: Nick Anderson
type: post
date: 2009-08-20T02:47:22+00:00
url: /2009/08/19/its-not-the-cloud-its-the-phog/
syntaxhighlighter_encoded:
  - 1
openid_comments:
  - 'a:1:{i:0;s:3:"938";}'
categories:
  - Posts
tags:
  - cloud
  - phog
  - rant
  - vmware
  - xen

---
I am so very tired of hearing about &#8220;the cloud&#8221;. Over lunch the other day a co-worker decided we should just call it the phog instead since the phog does a better job of describing exactly what is meant by the cloud.

Why is phog a better description? The phog has no defined shape, you can&#8217;t see clearly in it, its different everywhere you go, and once your in the middle of it you can&#8217;t find your way out (due to marketing fluf).

You cant have escaped all of the cloud stories in the past year or so. The one that just sent me over the edge was a press release about Vmware buying SpringSource. It is basically Vmwares approach to supplant Xen as the major phog platform. I&#8217;m not sure exactly what rubbed me wrong and sent me off into this tirade. Its very possible that I just don&#8217;t like Vmware and the first article I read used the more popular term for phog putting me in this tizzy. It&#8217;s also possible that I was already on edge about Vmware after my recent discussions with one of their sales people.

For a bit of background Vmwares sales goons are spreading the F.U.D. hard core. One sales goon recently told me &#8220;Xen is dead in the water&#8221;, &#8220;No one is using Xen&#8221;, &#8220;With all of Citrix&#8217;s advertising about Hyper-V  they don&#8217;t seem commited to the Xenserver product&#8221;. That along with &#8220;Everyone is going to KVM&#8221;, and some other slams about Xen not having dom0 support in mainline. Of course its fine that I don&#8217;t even have the option of running the Vmware hypervisor on the distribution of my choice, and no mention of the fact that dom0 support being mainline really has nothing to do with a Citrix products future. [It&#8217;s not just a sales guy, I saw a similar slide against Citrix for their work with Hyper-V in a Vmware pdf][1] (See bottom right corner). Anyway, on with the original rant.

As I was saying I was already on edge, and one more phog article shows up. What is the phog? Really? Its hosted applications, no more. Maybe a more programmatic way to define what services you would like and when you would like them available, but its nothing more than paying someone else to host your application servers.

This brings me to another point, and another thing that I wish developers would learn from system administrators ([see my comment on Matt Simmons blog for context][2]). Many of my developer friends think its perfectly fine to host everything on someone else&#8217;s equipment out in the phog. I feel it is one of my responsibilities to keep data safe. How can you keep data safe when its all out floating around in the phog. I have nothing against scaling out to the phog especially for high volume times but I still think that your core infrastructure should be managed on your own equipment where you can walk up to it and touch it if you want (even if its in someone else&#8217;s data-center).

I even had a conversation with a new co-worker recently who thinks <span style="text-decoration: underline;"><em><strong>everything</strong></em></span>, your data, downloaded content, desktop etc &#8230; will all move to the phog eventually. Ewwwww I can&#8217;t fathom letting my data slip that far from my hands.

Do you really think the phog will take off long term? What do you think about most of my developers friends points of view that putting \_everything\_ in the phog is acceptable or even a good idea?
  
~

 [1]: http://www.cmdln.org/wp-content/uploads/2009/08/RequestProcessorAwareAction-1.pdf
 [2]: http://www.standalone-sysadmin.com/blog/2009/08/the-future-of-system-administration/#comment-3222