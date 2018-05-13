---
title: 'Migrating to Google Apps: changing mailto link'
author: Nick Anderson
type: post
date: 2010-09-24T03:42:57+00:00
url: /2010/09/23/migrating-to-google-apps-changing-mailto-link/
categories:
  - Posts
tags:
  - firefox
  - google apps
  - sysadmin
  - tip

---
At $work we are in the process of migrating to Google Apps. Of course I am an early adopter to work out bugs and be a resource for others as they make the migration. One of the issues identified is mailto links pointing to google apps. Its not hard to make the change in firefox.

First you need to set ﻿﻿gecko.handlerService.allowRegisterFromDifferentHost to true in about:config (type about:config into your address bar).

Then login to your Google Apps account and paste the following into your address bar.

<pre class="brush: plain; title: ; notranslate" title="">javascript:window.navigator.registerProtocolHandler("mailto","https://mail.google.com/a/example.com/mail/?extsrc=mailto&url=%s","Example Google Apps")

</pre>

Just be sure to swap out example.com with your domain, and Example with your company.