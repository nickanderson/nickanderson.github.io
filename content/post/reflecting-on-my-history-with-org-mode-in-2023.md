+++
title = "Reflecting on my history with org-mode in 2023"
date = 2023-03-13
tags = ["org-mode"]
draft = false
author = "Nick Anderson"
+++

I think I started getting interested in org-mode in 2007[^fn:1]. I definitely was making serious attempts to integrate it into my workflow by 2010. By 2016 it became my primary tool. By primary tool, I mean that most of my daily work is either done from within or at least I've probably written down something about what I've done in org-mode.

Early on, maybe 2009 I found Bernt Hansens [Organize you life in plain text!](http://doc.norang.ca/org-mode.html) guide, it was, and still is an amazing document. I found the title so inspiring. At the time I was heavily focused on GTD and I recall setting up Emacs specifically for managing tasks using org agenda. Unfortunately, being treated like a standalone app, I couldn't make it stick in my workflow. I was uncomfortable without modal editing and vi keybindings. Constantly pasting and editing org files in the background with vim just wasn't efficient. I drifted into some scripts to manage todos from the command line[^fn:2] and then to the opposite end of the spectrum with Evernote[^fn:3].

In 2013 I was traveling a lot, meeting many different people and taking copious notes about challenges people were facing and what they wanted to achieve. The Evernote service was pretty OK, but I hated the thought that my precious notes were in someone else's locker. So, when I'm running on Linux in some place with low or no Internet, power etc .... And wanting to work on my notes what am I to do? Well, Nixnote[^fn:4] was ok. But it would crash and get slow, and when things blew up I was short of stranded until I got it fixed. I longed for the simplicity of plain text, where I could just use vim when things were burning around me.

Orgmode remained in the back of my mind and around 2015 I made an effort to migrate my notes into `org-mode`. I got evil mode working pretty well and managed to transition from Evernote.

By 2016 I found Spacemacs[^fn:5]. This was a huge accelerator. Evil mode worked out of the box, plus `cfengine-mode` in Emacs was significantly better than `vim_cf3`&nbsp;[^fn:6]. Not only did it provide highlighting, it also provided function prototypes as I typed via eldoc, syntax checking via fly check, and projectile made it easy to test a full policy set. Things quickly progressed from there as I kept finding more ways to avoid leaving org-mode (ok, yeah, it's Emacs, but in my head org-mode is the focus) making it easier to wrangle text and weave things into my notes.

I started making presentations in org-mode, with the help of org-reveal exporting to reveal.js[^fn:7].

Next I added email via `mu4e`[^fn:8]. Which really facilitated authoring email responses in org-mode. It became easy to email notes to colleagues and construct highly technical responses. I could see the potential for not organizing my life in plain text, but living my work life in plain text.

I started making more use of `org-babel` and cobbled together `ob-cfengine3`[^fn:9] which let me author and run snippets of CFEngine policy directly in my notes. Along this path I found [Howard Abrams](https://howardism.org/) post about literate DevOps[^fn:10] which was very similar to what I was doing. He echos many of my values in his post.

So, I could get an email with a question, select the interesting part of the email that I wanted to respond to and trigger a capture bringing that text with a link that I could follow back to that email right into org-mode. I could author and run code blocks illustrating something and respond without ever breaking stride.

It was easy to create detailed logs investing something with a trail of src blocks with output along the way. I could easily take that text and export it to the bespoke markup for a ticketing system (Jira, with ox-jira before it transitioned to markdown, and Markdown after). I was even using org-jira to directly interface with the ticketing system, posting comments directly from the comfort of org-mode.

By 2021 I had run into various performance issues that really centered around large files. Large files that have high churn (eg. As the result of large results from src blocks that are sometimes rerun many times) made my environment slow and sent me in search of new strategies which is when I came across org-roam[^fn:11].

Org-roam uses the zettelkasten method of organization. It provides some functions that facilitate a methodology built around many smaller interlinked files. I started making heavy use of `org-roam-dailies-capture` which brings me to how I org in 2023.

[^fn:1]: Seems right, Linux Journal had an article about org-mode in 2007. <https://www.linuxjournal.com/article/9116>
[^fn:2]: I had written my own todo manager based off of Tom Limoncellies Cycle from Time Management for Systems Administrators and I had been trying out todo.txt (which is still around and has a nice little Android app) <http://todotxt.org/>.
[^fn:3]: I loved the Evernote motto, remember everything

    At least in 2023 Evernote's motto seems to be "Tame your work, organize your life Remember everything and tackle any project with your notes, tasks, and schedule all in one place." <https://evernote.com/>
[^fn:4]: Nixnote is a desktop client for Evernote that runs on Linux and Windows <http://www.nixnote.org/>
[^fn:5]: A community-driven Emacs distribution. The best editor is neither Emacs nor Vim, it's Emacs _and_ Vim! <https://www.spacemacs.org/>
[^fn:6]: Vim support for syntax highlighting, abbreviations, code tidying and templates made by [Neil Watson](https://watson-wilson.ca/). <https://github.com/neilhwatson/vim_cf3>
[^fn:7]: Reveal.js is an html presentation framework. It produces nice looking html slides and has features like speaker-notes and even live code execution. <https://revealjs.com/>
[^fn:8]: mu4e is an email client for Emacs built on top of the `mu` search engine. It's optimized for quickly processing large amounts of email. It operates on mail directories, so you need to sync your email locally with something like [isync](https://isync.sourceforge.io/) <https://www.djcbsoftware.nl/code/mu/mu4e/index.html>
[^fn:9]: My first emacs package, I gave it to myself for my 36th birthday. I figure that it saved me at least 36 seconds for every CFEngine example snippet that I write and it's definitely paid for itself. I don't make many changes to it, [Diego Zamboni](https://zzamboni.org/) has contributed some nice features.  <https://github.com/nickanderson/ob-cfengine3>
[^fn:10]: I really dislike the term DevOps but I found Howard's post reached in the direction I was headed. It's a great resource. <https://howardism.org/Technical/Emacs/literate-devops.html>
[^fn:11]: Org-roam is a tool for networked thought. It reproduces some of [Roam Research's](https://roamresearch.com/) key features within Org-mode. <https://www.orgroam.com/>