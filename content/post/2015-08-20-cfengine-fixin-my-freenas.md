---
title: CFEngine fixin my FreeNAS
author: Nick Anderson
type: post
date: 2015-08-21T04:51:59+00:00
url: /2015/08/20/cfengine-fixin-my-freenas/
categories:
  - Posts
tags:
  - CFEngine
  - FreeBSD
  - FreeNAS

---
I recently built a new file server and I based it on the well renowned <a href="http://www.freenas.org/" target="_blank">FreeNAS</a> by <a href="https://www.ixsystems.com/" target="_blank">iXsystems</a>. It&#8217;s been pretty solid over the past few weeks but today I ran into an issue. The web ui stopped responding. Actually it turned out that the django service had stopped. Well, that was the perfect opportunity to use CFEngine to make sure I never have the issue again.

<img class="alignright size-full wp-image-1210" src="http://www.cmdln.org/wp-content/uploads/2015/08/cfenginefreebsd.png" alt="cfenginefreebsd" width="900" height="600" srcset="http://www.cmdln.org/wp-content/uploads/2015/08/cfenginefreebsd.png 900w, http://www.cmdln.org/wp-content/uploads/2015/08/cfenginefreebsd-300x200.png 300w" sizes="(max-width: 900px) 100vw, 900px" />

I grabbed the [cfengine community 3.7.0 package][1] for Freebsd 9.3 package from <a href="http://www.cfengineers.net" target="_blank">CFEngineers.net</a> (thanks guys!) and it installed without issue.

<pre>wget http://www.cfengineers.net/files/packages/cfengine-community/3.7.0/cfengine-community-3.7.0_1-freebsd_9.x_amd64.tbz
pkg_add cfengine-community-3.7.0_1-freebsd_9.x_amd64.tbz</pre>

I just wanted to experiment locally instead of bootstrapping to a policy server so I grabbed the [masterfiles source tarball for 3.7.0][2] and installed the masterfiles policy framework.

<pre>tar zxvf cfengine-masterfiles-3.7.0-2.tar.gz
cd cfengine-masterfiles-3.7.0/
./configure
make install</pre>

Since I am only going to have local policy for now I went ahead and linked inputs to masterfiles.

<pre>rm -rf /var/cfengine/inputs
ln -s /var/cfengine/masterfiles /var/cfengine/inputs</pre>

And then I enabled cfengine.

<pre>cfengine3_enable="YES" &gt;&gt; /etc/rc.conf
service cfengine3.sh start</pre>

I enabled autorun for convenience.

<pre>sed -i 's/.*services_autorun.*expression.*/      "services_autorun" expression =&gt; "any";/' /var/cfengine/masterfiles/controls/3.7/def.cf</pre>

And then I installed [this policy][3] into services/autorun.

<pre data-wpview-marker="https%3A%2F%2Fgist.github.com%2Fnickanderson%2Fa46fdf764da3370e2bce">wget https://gist.githubusercontent.com/nickanderson/a46fdf764da3370e2bce/raw/a9116f64f8cf6158738a82e136de676325ab0a0e/freenas.cf -O /var/cfengine/masterfiles/services/autorun/freenas.cf</pre>

Now any time django decides to die, CFEngine will come along and fix it up.

<pre>[root@freenas] ~# service django stop
Stopping django.
Waiting for PIDS: 17087.
[root@freenas] ~# cf-agent -K
[root@freenas] ~# service django status
django is running as pid 17203.
[root@freenas] ~# tail /var/log</pre>

Maybe I&#8217;ll do some Software Defined Storage :-p

 [1]: http://www.cfengineers.net/files/packages/cfengine-community/3.7.0/cfengine-community-3.7.0_1-freebsd_9.x_amd64.tbz
 [2]: https://cfengine-package-repos.s3.amazonaws.com/tarballs/cfengine-masterfiles-3.7.0-2.tar.gz
 [3]: https://gist.github.com/nickanderson/a46fdf764da3370e2bce