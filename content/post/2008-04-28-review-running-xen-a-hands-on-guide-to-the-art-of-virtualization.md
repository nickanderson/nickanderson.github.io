---
title: 'Review: Running Xen a Hands-On guide to the Art of Virtualization'
author: Nick Anderson
type: post
date: 2008-04-28T23:32:23+00:00
url: /2008/04/28/review-running-xen-a-hands-on-guide-to-the-art-of-virtualization/
categories:
  - Posts
tags:
  - book
  - review
  - xen

---
A few days ago I finally got my copy of Running Xen. I was anxious to see how the information would be presented. I can tell you I was not disappointed. <!--more--> I am by no means a Xen master. I have tinkered with it a few times over the past several years but as I am getting ready to use it full time in production I need as much information as I can get. The books authors include Eli Dow, and Todd Deshane who worked on 

[Xen and the Art of Repeated Research][1], as well as [Quantifying the Performance Isolation Properties of Virtualization Systems][2].

Running Xen is an easy read. Easy in that it can actually be read cover to cover without becoming tired of mundane drivel. However it is not a glossy overview of Xen. Its 500 plus pages cover everything from using prebuilt images that can be downloaded from jailtime.org, rpath, virtualappliances.net as well as other resources. I do believe this is the first book I have come across that actually explains how to use the different image types (disk and partition). Ok so there are not many Xen books around, and I have not actually read Xen Virtualization: A Practical Handbook or Virtualization with Xen but I will not be surprised if they cover what prebuilt images are in less detail than Running Xen.

65 pages are dedicated to networking, covering bridging, routing, and Nat modes of operation. If you want to include the pages on fire walling there are more than 65 pages of networking related material. Storage backends including LVM, file, partition, nfs, and iscsi are also covered in detail. I was particularly impressed with the coverage of LVM being that many authors would consider it beyond the scope of the book. It is a great resource for any new Xen administrator, and I can wager that it will be valuable for mid-level Xen administrators as well. I defiantly will be revisiting several sections as I get deeper into Xen (read more hardware to test with). For those of you wanting to virtualize Windows, you have not been forgotten. The first several pages of chapter 7 Populating Guest Images shows how to install a windows (or linux) system using an iso or physical rom drive.

What was missing? One backend that was omitted was DRDB. I found this to be somewhat disappointing as live migration can be obtained with less than 3 machines and for those of us on a budget like me scrimping pennies while trying to make a scalable system is a prime directive. Also there was no mention of how to use multiple iso files for installing, how to change them out or if its possible. I have seen that question several times in the #Xen channel on freenode so I know its something people want to do. Other than that I am streched to think of something I would like to do with Xen that is not in some way shape or form covered. Perhaps a section on backups would be a good addition. How to save state and image the operating system with little downtime. I say little because to my knowledge its not yet possible to do hot backups. (if your wondering how to do it think xm save; lv snapshot, xm restore; dd snapshot to image file).

What is the verdict? If you are a new Xen administrator, or thinking about heading down the Xen path this book will be well worth your dime. If you have read The Definitive Guide to the Xen Hypervisor and felt overwhelmed not to worry, this book was written for us mere mortals. (The Definitive Guide to Xen Hypervisor, was a good book but most of it went over my head)

<!--adsense-->

 [1]: http://www.usenix.org/events/usenix04/tech/freenix/full_papers/clark/clark.pdf
 [2]: http://www.usenix.org/events/expcs07/papers/6-matthews.pdf