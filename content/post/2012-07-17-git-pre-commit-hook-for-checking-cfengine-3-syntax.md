---
title: Git pre-commit hook for checking CFEngine 3 syntax
author: Nick Anderson
type: post
date: 2012-07-17T22:36:40+00:00
url: /2012/07/17/git-pre-commit-hook-for-checking-cfengine-3-syntax/
categories:
  - Posts
tags:
  - CFEngine
  - git

---
I was inspired by [William Orr&#8217;s][1] [svn commit hook][2] and looked up the magic needed to flesh out the [git pre-commit hook][3] I submitted to the [Design Center][4] a while back.[<img class="aligncenter size-medium wp-image-1049" title="git_cf3" src="http://www.cmdln.org/images/wp-content/uploads/2012/07/git_cf3-300x92.png" alt="" width="300" height="92" srcset="http://www.cmdln.org/images/wp-content/uploads/2012/07/git_cf3-300x92.png 300w, http://www.cmdln.org/images/wp-content/uploads/2012/07/git_cf3.png 423w" sizes="(max-width: 300px) 100vw, 300px" />][5]

Now the index is checked out to its own temporary directory and cf-promises validates promises.cf and failsafe.cf before allowing the commit to proceed. Now you won&#8217;t get syntax errors if you have forgotten to add a new policy file to the index but its already included in your body common control inputs list. If your using a generated inputs list then you might want to add a separate file that includes everything for syntax checks. Be sure to include that file in the checkfiles list.

I would like to see a pre-receive version of this some day.

 [1]: http://worrbase.com
 [2]: https://cfengine.com/forum/read.php?3,26459
 [3]: https://github.com/cfengine/design-center/tree/master/tools/git-pre-commit
 [4]: https://github.com/cfengine/design-center/
 [5]: http://www.cmdln.org/images/wp-content/uploads/2012/07/git_cf3.png
