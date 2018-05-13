---
title: ssh config wildcards
author: Nick Anderson
type: post
date: 2008-12-17T17:07:58+00:00
url: /2008/12/17/ssh-config-wildcards/
aktt_notify_twitter:
  - yes
openid_comments:
  - 'a:2:{i:0;i:682;i:1;i:683;}'
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - ssh

---
I just wanted to make sure no one forgets that wildcards can be used in your .ssh/config. This can be extremely helpful. For example say you have 100 nodes that have a simple nameing scheme of nodexxxx. You can add the following into your ssh config and pre-poplulate settings.

<pre class="brush: bash; title: ; notranslate" title="">Host node*
    User staffuser
    IdentityFile ~/.ssh/staff_key
</pre>

That would cause any ssh connection matching node* to use the user staffuser and .ssh/staff_key as the ssh key. By the same token you could do this.

<pre class="brush: bash; title: ; notranslate" title="">Host *.locallan.domin.com
    User me
</pre>

This could be useful if you have networks of machines that hook into different authentication systems. Nothing groundbreaking by any means but its useful so dont forget about it.