---
title: 'CFEngine 3 by Example &#8211; Vagrant Project'
author: Nick Anderson
type: post
date: 2012-07-14T20:02:17+00:00
url: /2012/07/14/cfengine-3-by-example-vagrant-project/
categories:
  - Posts
tags:
  - CFEngine
  - Vagrant

---
I updated the [CFEngine 3 by example vagrant][1] project so that [<img class="size-full wp-image-1042 alignright" title="CFEngine3 inside Vagrant" src="http://www.cmdln.org/images/wp-content/uploads/2012/07/vagrant_cf3.png" alt="" width="183" height="200" />][2]/var/cfengine/masterfiles is a git clone (kept in sync with [VCS::vcs_mirror][3]) of the generated bare repository from the seed files. I found during a presentation that it would just be easier to have everyone start of with the typical workflow instead of going through the process of getting there. I hope it makes it easier for people to get a working test env up in a few minutes.

 [1]: https://github.com/nickanderson/CFEngine-3-by-example-vagrant
 [2]: http://www.cmdln.org/images/wp-content/uploads/2012/07/vagrant_cf3.png
 [3]: https://github.com/cfengine/design-center/tree/master/sketches/utilities/vcs_mirror
