---
title: Support Fail
author: Nick Anderson
type: post
date: 2009-08-24T19:12:51+00:00
url: /2009/08/24/support-fail/
syntaxhighlighter_encoded:
  - 1
openid_comments:
  - 'a:3:{i:0;s:3:"954";i:1;s:3:"955";i:2;s:3:"977";}'
categories:
  - Posts
tags:
  - fail

---
I am a big fan of chat support. I don&#8217;t have to drain my battery waiting on hold until its my turn in the queue. Plus when dealing with error messages its infinitely more helpful to be able to copy/paste to the agent. Sadly finding competent help is still an issue. Here is an excerpt from a recent chat support experience.

> <span>(8:39:41 PM) <strong> Sheldon He:</strong> The SSL will need to be re-issued, since they are IP specific.</span>
  
> <span>(8:40:06 PM) <strong> Nick Anderson:</strong> ssl certificates are not tied to ip addresses</span>
  
> <span>(8:40:56 PM) <strong> Sheldon He:</strong> Actually they are. They are domain and IP specific. That&#8217;s why it needs a dedicated IP.</span>
  
> <span>(8:43:06 PM) <strong> Nick Anderson:</strong> ssl is just tied to a name, but you can only run one ssl cert per ip without the Server Name Indicator tls extension to openssl</span>
  
> <span>(8:43:20 PM) <strong> Sheldon He:</strong> Well, according to our SSLs in the past, the SSL needs to be re-issued when you move from a Shared to a Reseller.</span>
  
> <span>(8:45:40 PM) <strong> Sheldon He:</strong> I&#8217;m unable to change the settings here, this will require an admin. Please email them at support@hostgator.com and we&#8217;ll be able to help you with this issue.</span>

<p style="text-align: left;">
  Luckily his final answer was correct and whoever answers the support emails was able to complete the ssl cert migration.
</p>

<p style="text-align: left;">
  On a side note, its things like this that make me tell people to not use shared hosting accounts. Get yourself a VPS or a dedicated server if you want to do anything worth while.
</p>

<span><br /> </span>