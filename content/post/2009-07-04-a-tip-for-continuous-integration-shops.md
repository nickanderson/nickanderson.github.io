---
title: A tip for continuous integration shops
author: Nick Anderson
type: post
date: 2009-07-04T23:28:42+00:00
url: /2009/07/04/a-tip-for-continuous-integration-shops/
aktt_notify_twitter:
  - no
categories:
  - Posts

---
Recently I have been working on cleaning up our continuous integration enviornment. Continuous integration is pretty cool but don&#8217;t shoot yourself in the foot by making bad build plans and not being very specific about your build requirements. If you have a package dependancy for a build make sure you put it in your requirements. If you need specific access to a database to do fixture tests SPECIFY it.

In the short term you can see the benefits of continuous integration  without doing these things. But as people cycle in and out of your orginization having a clear record of all the requirements for a build is crucial.