---
title: Revision your home directory with git using gibak
author: Nick Anderson
type: post
date: 2009-02-20T14:56:53+00:00
url: /2009/02/20/revision-home-directory-git-gibak/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - gibak
  - git

---
Over the last couple days I&#8217;ve briefly talked about [revisioning configs][1] and [making your home directory portable][2]. It seems to have stirred up a bit of discussion over at [Matt Simmons Standalone Sysadmin][3], and [Hugh Browns mentioned he uses mercurial][4] for this task.. As I noted in the post about [managing /etc with version control][1] I do revision my home directory, or at least pieces of it.<!--more-->


  
I consider this to be a different problem than [making my environment portable][2]. For example I want my configs to have a full revision history, even things like my ssh config or my private keys. I want that history as a backup, I do not want to distribute all of that information to other machines. [gibak][5] is a great wrapper for git to help with this.
  
Installation is not hard but you will need to install a few dependencies.

<pre class="brush: bash; title: ; notranslate" title="">aptitude install ocaml omake git-core
git clone http://eigenclass.org/repos/git/gibak/.git/
cd gibak
omake
cp find-git-files ~/bin
cp find-git-repos ~/bin
cp gibak ~/bin
cp ometastore ~/bin
</pre>

Now that its installed you just need to initialize your git repo, make adjustments to your .gitignore (you probably don&#8217;t want \_everything\_ in your repo).

<pre class="brush: bash; title: ; notranslate" title="">gibak init
vim ~/.gitignore
gibak commit
</pre>

I don&#8217;t have everything in my home directory revisioned. Mainly I revision configuration files and my Documents. Here is what my .gitignore looks like.

<pre class="brush: bash; title: ; notranslate" title=""># I am selective about what I want to revision, you may not want this.
/*
# You probably want to ignore all the "dot" files in your home
# directory, since they mostly contain local application state data.
/.*
# but... some dot files you probably do *not* want ignored are
# listed here:
!/.bash*
!/.gnupg
!/.ssh
!/.vimrc
!/.mutt
/.mutt/profile.d/*/cache
!/.gitignore
!/.todocycle
!/Documents
</pre>

Now depending on what files you want in your repo and if they change frequently or not you may want to have a cron job to automatically commit changes to your repo. I would suggest an entry similar to this.

<pre class="brush: bash; title: ; notranslate" title="">0 0 * * * gibak commit  "Automatic Commit - $(date +%m.%d.%Y)"
</pre>

To manually commit changes just run gibak commit after making changes.

Now you can deal with your revisioned files just like any other git repo. You can clone it to a remote location to back it up, revert commits or whatever else suits your fancy.

 [1]: http://www.cmdln.org/2009/02/19/version-your-etc/
 [2]: http://www.cmdln.org/2009/02/18/movin-in-movin-out/
 [3]: http://standalone-sysadmin.blogspot.com/2009/02/ideas-on-maintaining-customized-shelll.html
 [4]: http://saintaardvarkthecarpeted.com/blog/2009-02/mercurial_for_dotfiles.html
 [5]: http://eigenclass.org/hiki/gibak-backup-system-introduction