---
title: Maintenance mode with apache mod_rewrite
author: Nick Anderson
type: post
date: 2008-12-12T19:41:00+00:00
url: /2008/12/12/maintenance-mode-with-apache-mod_rewrite/
aktt_notify_twitter:
  - no
openid_comments:
  - 'a:1:{i:0;i:674;}'
categories:
  - Posts
tags:
  - apache
  - mod_rewrite

---
With small websites sometimes you need to put up a maintenance page while you are making some modifications. Typically you should have some staging enviornment but sometimes infrastructure does not allow for this. If you find your self in this situation you might like this tip. <!--more-->


  
It is not sufficient to just replace your index with a maintenance page for multiple reasons. First what about sub pages? Without a redirect on those people will be able to access other areas of your site which may of may not be desireble. 

Using mod_rewrite you can be friendly to search engines, and your users.

Try this in your .htaccess

<pre class="brush: bash; title: ; notranslate" title="">ErrorDocument 404 /maint.html
RewriteEngine on
RewriteCond %{REQUEST_URI} !/maint.html$
RewriteCond %{REQUEST_URI} !/maint.jpg$
RewriteRule $/maint.html$ [R=302,L]
</pre>

This will give a 302 (Moved Temporarily) msg to clients and serve
  
maint.html. maint.html can have content similar to this.

<pre class="brush: bash; title: ; notranslate" title="">&lt;img src="/maint.jpg" alt="We are currently undergoing maintenance. We will be back shortly"&gt;'
</pre>

The leading slash on the image is important as it will serve the image even if someone accesses http://yourdomain/somethig/somethingelse.

Its also important to set your 404 as your maint.html so anyone accessing pages that do not exist get the same maintenance content.

You might want to add a condition like the following if you want to be able to browse your website normally while in maintenance mode.

<pre class="brush: bash; title: ; notranslate" title="">RewriteCond %{REMOTE_HOST} !^123\.123\.123\.123
</pre>

Be sure to replace 123.123.123.123 with your ip address. This will cause apache to not apply the rule to the specifed ip.

Hope someone finds this useful. I know I have used it several times in the past.