---
title: Bundles of Bundles with CFEngine 3
author: Nick Anderson
type: post
date: 2012-02-16T07:05:53+00:00
url: /2012/02/16/bundles-of-bundles-with-cfengine-3/
categories:
  - Posts
tags:
  - CFEngine
  - createrepo
  - password management
  - redhat
  - routes
  - selinux
  - sysadmin
  - yum

---
[<img class="alignleft size-thumbnail wp-image-936" title="Bundles of Bundles" src="http://www.cmdln.org/images/wp-content/uploads/2012/02/Extrusion-Bundles2-150x150.jpg" alt="" width="150" height="150" />][1]I&#8217;ve been working more and more with CFEngine lately and I have been slowly building a [tiny library][2]. These are all pretty much redhat specific but I welcome patches and comments. Most of the bundles have comments that show usage, if there is interest I may post some example usage later.

&nbsp;

&nbsp;

&nbsp;

<!--more-->

&nbsp;

I have recently added these bundles to my library

## [lib_rh.cf][3]{#1547a55e9c7f237eb46ab06a01bb5d7a8ca13f88}

  * <pre>rh_add_interface_routes - manage routes on an interface</pre>

  * <pre>create_update_yum_repo - create a yum repo and update the metadata if files change</pre>

  * <pre>set_selinux_disabled - disable selinux, yes its sad but its common</pre>

  * config\_yum\_client_repos &#8211; configure yum client configs in /etc/yum.repos.d/

<pre></pre>

## [lib\_local\_user_management.cf][4]{#2588f5f1173110449ece0d6ec54c90c8c84351d7}

  * local\_users\_enforce_password &#8211; enforce a local users password, supports updating last day changed for password expiration

&nbsp;

 [1]: http://www.cmdln.org/images/wp-content/uploads/2012/02/Extrusion-Bundles2.jpg
 [2]: http://www.laurand.net/images/Extrusion%20Bundles2.jpg
 [3]: https://github.com/nickanderson/nickanderson-cfengine-library/blob/master/lib_rh.cf
 [4]: https://github.com/nickanderson/nickanderson-cfengine-library/blob/master/lib_local_user_management.cf
