---
title: Convert maildir to mbox
author: Nick Anderson
type: post
date: 2009-03-13T16:52:32+00:00
url: /2009/03/13/convert-maildir-to-mbox/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - bash

---
Note, there is a short story before the main course.

I recently had a customer leave. It&#8217;s never good to lose a customer. They left not because of any service issues but because its hard for them to understand that I am not a web designer. I provided hosting service for them, and I tried to make it clear that they should find a web desinger and someone to maintain their site because that is not something I specialize in or have any interest in doing. At any rate this of course leads to them finding a designer who wants to move their site to some other host. I have no problems with that whatever makes the maintainer happy since he is the one <!--more-->who will have to support it.

My issue comes when I am asked to handle things like mail. The webdeveloper seems to not understand how mail works and appears to not be comfortable with migration. I reminded the customer to make sure he had a plan in place for their mail (it&#8217;s not my responsibility). I switched the dns on my end and changed the nameservers with the registrar so the cut would be as quick as possible. Days later after sorting the mail issue on their end I was asked about their old email. I had just the day prior terminated their accounts so I had to dig through some backups to find the mail. I obliged and sent a tar.gz of the entire maildir. Now their new guy says he isnt comfortable restoring the mail probably because he has no clue how to deal with maildir on the new host (network solutions). Mind you I am taking some liberty here because he complained to me I didnt tell him how to migrate the mail. I had just assumed he would use a tool like imapsync or even hook up both accounts in a mail client and manually transfer the mail from the old server to the new one. So that being the case I say he doesn&#8217;t understand how mail works, and its his fail for accepting responsibility to migrate a site and hosting services without planning how to do so.

That brings us to the main course or as I look at all the text above perhaps it should be desert.

I converted the maildir to mbox for the customer in the hopes the new guy can figure out how to load the mbox into a mail client and upload the mail to the new server for the customer. Perhaps I am being a bit petty making him do it. I don&#8217;t feel too bad I have already gone way past normal customer service with this customer, and even gave them several months of hosting for free (I forgot to bill them and told them not to worry about it). Not to mention the time I have spent going to their office to troubleshoot a workstation because &#8220;the internet was broken&#8221; which I also did not charge for. So maybe I am just inflicting a bit of pain on the new guy, but I hope he learns from the experience.

So how did I convert the maildir to mbox? I used formail which is provided by procmail.

<pre class="brush: php; title: ; notranslate" title="">for i in maildir/cur/*;do formail -I "Status: RO" &lt;"$i" &gt;&gt;mbox;done
for i in maildir/new/*;do formail -I Status: &lt;"$i" &gt;&gt;mbox;done
</pre>

You will want to do that for each maildir (don&#8217;t forget the .Subfolder directories). And remember each &#8220;folder&#8221; or maildir would be a different mbox file. So if you wanted to save sent mail as well &#8230;

<pre class="brush: php; title: ; notranslate" title="">for i in maildir/.Sent/cur*;do formail -I "Status: RO" &lt;"$i" &gt;&gt;sent;done
for i in maildir/.Sent/new/*;do formail -I Status: &lt;"$i" &gt;&gt;sent;done
</pre>