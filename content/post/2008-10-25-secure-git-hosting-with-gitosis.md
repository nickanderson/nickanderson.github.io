---
title: Secure git hosting with gitosis
author: Nick Anderson
type: post
date: 2008-10-26T05:50:59+00:00
url: /2008/10/25/secure-git-hosting-with-gitosis/
aktt_tweeted:
  - 1
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - git
  - gitosis
  - hosting

---
I hope you are already using ssh keys, but just in case your not go ahead and generate one with ssh-keygen -t rsa (you should do this on your local box)
  
You may as well go ahead and copy your publick key to your git server now as well.

<pre class="brush: bash; title: ; notranslate" title="">scp ~/.ssh/id_rsa.pub gitserver:/tmp/
</pre>

Log into your gitosis server

<pre class="brush: bash; title: ; notranslate" title="">ssh gitserver
</pre>

* Make sure setuptools is installed

sudo aptitude install python-setuptools

git clone git://eagain.net/gitosis.git
  
cd gitosis
  
sudo python setup.py install

sudo adduser &#8211;system &#8211;shell /bin/bash &#8211;gecos &#8216;git version control&#8217; &#8211;group &#8211;disabled-password &#8211;home /home/git git

sudo -H -u git gitosis-init < /tmp/id\_rsa.pub \[/code] We need to fix up a few things that don't seem to get proper permissions. [code='bash'] sudo -H -u git chmod 600 ~/.ssh/authorized\_keys sudo -H -u git chmod 755 ~/repositories/gitosis-admin.git/hooks/post-update sudo rm /tmp/id_rsa.pub [/code] Thats all for now on your git server. You manage gitosis with git of course and you can do that from your local machine or any machine that you have the match to the public key you installed with gitosis. [code='bash'] git clone git@gitserver:gitosis-admin.git cd gitosis-admin [/code] Creating new repositories New repositories are created by authorizing a user to write and pushing to it. [code='bash'\] \[group someproject\] members = jack jill writeable = someproject \[/code] This definition would create the group someproject and allow jack and jill write access to the repository someproject (which you would reference as someproject.git) For a bit more explanation ... [code='bash'\] \[group developers\] members = jack john frank writable = project1 project2 project3 [/code] This definition would create the group developers, and allow jack, john, and frank write access to the repositories project1, project2, and project3 Once you have defined your repositories commit and push your changes to gitosis admin. [code='bash'] git commit -a -m "Created inital gitosis config" git push [/code] Now if you have an existing repository that you would like to add to your git server simply change into the repository and do [code='bash'] git remote add origin git@gitserver:repo.git git push [/code] That will push the current branch of the repo over to the repo you set up on your git server. So thats about it. Anonymous access To allow anonymous read access touch git-daemon-export-ok inside ~/repositories/repo.git of each repo you wish to allow anonymous access (read only) to. Once you have done that launch git-daemon with base path /home/git/repositories.