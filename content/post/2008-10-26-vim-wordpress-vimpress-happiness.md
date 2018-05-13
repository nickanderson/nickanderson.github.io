---
title: Vim + wordpress == vimpress, happiness
author: Nick Anderson
type: post
date: 2008-10-26T15:37:48+00:00
url: /2008/10/26/vim-wordpress-vimpress-happiness/
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - blog
  - vim
  - wordpress

---
I recently found a vim plug-in for WordPress. [Vimpress][1] allows your to write and edit your blog posts directly from vim. Sure it has its limitations. There does not appear to be support for future data publishing or drafts. But overall its a much better experience to write in vim than the built in editor.
  
<!--more-->

One highly annoying omission was support for the more tag. By default when opening old posts will only display content before the more tag. And when posting at least from my brief testing would insert the more tag as plain text. Luckily Manuel Pégourié-Gonn wrote a small patch to address that issue. As of yet it does not appear he has actually published the patch though he does have a post about Vimpress that mentions it <http://weblog.elzevir.fr/2008/07/wordpress-a-ma-sauce-partie-1/>.

Here is the [vimpress][2] [][2][more tag patch thanks to Manuel][2]. And a [full patched version of vimpress.vim aka blog.vim.][3]

 [1]: http://friggeri.net/blog/2007/07/13/vimpress
 [2]: http://www.cmdln.org/wp-content/uploads/2008/10/vimpress.patch
 [3]: http://www.cmdln.org/wp-content/uploads/2008/10/vimpress.vim