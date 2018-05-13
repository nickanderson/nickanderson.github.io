---
title: Digging up bundles and bodies
author: Nick Anderson
type: post
date: 2013-10-29T14:26:52+00:00
url: /2013/10/29/digging-up-bundles-and-bodies/
categories:
  - Posts
tags:
  - CFEngine

---
You never know when the Zombie or Cloud Apocalypse is coming. It&#8217;s good to be able to locate those buried bodies quickly and easily. OK, enough bad jokes, but haven&#8217;t you ever looked at some CFEngine policy and wondered to yourself, exactly what does &#8220;delete => tidy&#8221; or some other body or bundle do?[<img class="alignright size-full wp-image-1199" alt="4e5d6fc8" src="http://www.cmdln.org/wp-content/uploads/2013/10/4e5d6fc8.jpg" width="215" height="260" />][1]

I have. [I even wrote a crappy little perl script][2] to locate the files that contained a specific body or bundle and then print out the single body or bundle. This past week my old script [got some love][3]. [Ted Zlatanov][4] and [Bishwa Shrestha][5] reworked it a bit so that it is no longer a hackjob, and its now [included in contrib][6] of the [CFEngine core repository][7].

I know I have found the script useful, and it&#8217;s nice to see that other people think its useful enough to put in contrib. I want to know if you think its useful enough to be installed in your $PATH (like the CFEngine binaries) when a package is installed. [I started a thread here][8] on the [help-cfengine mailing list/google group/forum][9]. If it&#8217;s something you would find useful speak up (Here, or in the thread, or email, or whatever)! If you hate it speak up, or better yet submit a pull request to add the functionality you want :).

 [1]: http://www.cmdln.org/wp-content/uploads/2013/10/4e5d6fc8.jpg
 [2]: https://groups.google.com/d/msg/help-cfengine/i_ZNFA_SaAs/T62p2lY__HgJ
 [3]: https://github.com/cfengine/core/commits/master/contrib/cf-locate
 [4]: https://github.com/tzz
 [5]: https://github.com/awsiv
 [6]: https://github.com/cfengine/core/tree/master/contrib/cf-locate
 [7]: https://github.com/cfengine/core
 [8]: https://groups.google.com/forum/?hl=en#!topic/help-cfengine/89VENZTA5fA
 [9]: https://groups.google.com/forum/?hl=en#!forum/help-cfengine