---
title: pre-commit hook for git to check CFEngine syntax
author: Nick Anderson
type: post
date: 2012-02-16T17:01:38+00:00
url: /2012/02/16/pre-commit-hook-for-git-to-check-cfengine-syntax/
categories:
  - Posts
tags:
  - cf-promises
  - CFEngine
  - git
  - pre-commit
  - sysadmin

---
[<img class="alignleft  wp-image-946" title="git-logo" src="http://www.cmdln.org/wp-content/uploads/2012/02/git-logo-97x150.png" alt="" width="58" height="90" />][1]Sometimes I am not so disciplined to run cf-promises on my policy before I commit it. I make a small change and I think I&#8217;m golden, but inevitably that breaks things. I wrote a simple commit hook to check policy syntax and stop you from shooting yourself in the foot. You can find  the [pre-commit][2]{#a71b90d9d3bb7e4d1f4be225eb124c42527855a3} script over on [my github account][3]. I hope you find it useful.

 [1]: http://www.cmdln.org/wp-content/uploads/2012/02/git-logo.png
 [2]: https://github.com/nickanderson/nickanderson-cfengine-library/blob/master/pre-commit
 [3]: https://github.com/nickanderson