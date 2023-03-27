+++
title = "How I org in 2023"
date = 2023-03-25
tags = ["org-mode", "org-roam", "pkm"]
draft = false
author = "Nick Anderson"
+++

I've been pretty much living in `org-mode` for 6 or 7 years now[^fn:1]. It's my exocortex, second brain, and personal knowledge management system. The features and tools I use as well as how I organize my files has changed quite a bit over this period of time and I thought it would be nice give myself (and anyone else who cares) a reference of what it was like in 2023 so here it is.

{{< figure src="org-mode-this-is-the-way.jpg" >}}

As of Sunday, March 26, 2023
 I have `3551` org files in my ~/org directory. Most of these (`2534`) are _time-series_ or _daily_ files. My personal journal (under `~/org/journal`), my daily work logs, and recurring meetings (under `~/org/roam/daily`). Not all of those files actually live there, I symlink some directories in to place. I don't often do this sort of setup, and it's a bit of a mess. I hope I wrangle it into something more easily reproducible some day.

I have `14` org-roam-capture-templates and `64` org-roam-dailies-capture-templates.

As you may have been able to tell `org-roam`[^fn:2] is my primary capture interface and I _really_ like the daily capabilities. Each day I capture notes about everything I am working on into my work log while clocking time. This gives me a nice place to think and process what I am working on[^fn:3] as well as a place to get my bearings and see what I have been working on when I get side-tracked[^fn:4]. Having a new file each day gives me a fresh start and it helps me to avoid performance issues I have previously experienced with large (multi-megabyte) files. I still have a lot of org files not under my roam directory which I have yet (and may never fully) to migrate.

Beyond my time-series notes I have other collections of related notes in sub directories. For example, I have many notes about CFEngine (the best configuration management tool)[^fn:5]. I keep my CFEngine related notes in `~/org/roam/CFEngine` with sub directories for different things ( blogs, examples, notes, opportunities, releases, release-testing
).

So, how does a day in my org life flow?

Usually my day starts with meetings. I like to take notes and email them to a distribution list afterwords[^fn:6]. For example, a few minutes before my CFEngine stand-up I run `org-roam-dailies-capture` and key in `w` (work) `m` (meeting) `c` (CFEngine) `d` (daily stand-up). Immediately after activating this capture I trigger another capture for my work log keying in `w` (work) `l` (log)[^fn:7] which clocks time. The work log capture template includes a backlink to the stand-up note for the day, so I follow that link and start going through my template filling it out. The template has a headline for each person with a property that links to a node for the individual[^fn:8]. My own section contains a clock table which quickly produces a nice list of the entries with clocked time from the previous day (on Mondays or days when I have missed prior N days I tweak the clock table to pull for the right number of previous days). I review the table  to see how good I was about clocking the previous day back-filling anything that I neglected to record then delete time columns. At the end of the meeting I use `org-mime`[^fn:9] to prepare a nicely formatted multipart ASCII &amp; HTML email. After sending the mail I switch back to my work log capture and complete it. All of my regularly scheduled meetings follow the same process; I capture for the meeting template, then I capture to my work log clocking time with an automatic backlink back to the specific meeting note. It's easy to capture notes for yesterday, tomorrow or an arbitrary date in the future using `org-roam-dailies-capture-yesterday`, `org-roam-dailies-capture-tomorrow`, and `org-roam-dailies-capture-date`.

Org-roam provides useful functions for accessing time-series notes. `org-roam-dailies-goto-today` will take you to today's note for the selected template and if the file does not exist it is initialized. Similarly `org-roam-dailies-goto-yesterday`, `org-roam-dailies-goto-tomorrow`, and `org-roam-dailies-goto-date` take you to the note for yesterday, tomorrow, or the specified date, creating the file if necessary. `org-roam-dailies-goto-previous` and `org-roam-dailies-goto-next` go to the previous and next note in the series based on the file you are currently visiting making for easy navigation through the time series.

If I am working on something that has some regular pattern but is not a recurring time series I follow a similar pattern, but instead of `org-roam-dailies-capture` I run `org-roam-capture`. Unlike `org-roam-dailies-capture` `org-roam-capture` first prompts for a node title and you select a template afterwords. For example, if I am working on support case I will run `org-roam-capture`, enter the issue number and then key in `w` (work) `s` (support). I am taken to a new node in the file for that support case where I immediately trigger `org-roam-dailies-capture` for my work log which starts clocking time and I follow the link back to the node to continue my work.

Speaking of links between notes, `org-roam-ui` provides a really fun interactive 2 or 3d graph showing the links between nodes.

{{< figure src="org-roam-ui-with-dailies-2023-03-26.png" caption="<span class=\"figure-number\">Figure 1: </span>org-roam-ui visualization with dailies as of 2023-03-26" >}}

{{< figure src="org-roam-ui-without-dailies-2023-03-26.png" caption="<span class=\"figure-number\">Figure 2: </span>org-roam-ui visualization without dailies as of 2023-03-26" >}}

I use inline code blocks while authoring this post to get current numbers on export. The above text looks like this in my org-mode file for the post which I export with `ox-hugo`.

```text
Speaking of links between notes, =org-roam-ui= provides a really fun interactive
2 or 3d graph showing the links between nodes. This is what my src_bash{echo -n
$(sqlite3 $HOME/.emacs.d/org-roam.db "select count(*) from nodes")} nodes across
src_bash{echo -n $(sqlite3 $HOME/.emacs.d/org-roam.db "select count(*) from
files")} files looks like.
```

For other activities that are typically fast or aren't of a common type spanning multiple days I simply run `org-roam-dailies-capture` and keep notes directly in my work log.

I author pretty much everything in `org-mode`. I am often able to stay in inside `org-mode` and keep a very thorough record of my exact activities. When I need to run commands I typically use `org-babel` so that commands their output and my thoughts about it form a nice log of my work as I proceed. This log is often directly transferable to communicate with others for which I leverage the copious export back ends available[^fn:10].

I currently have  `11649` nodes across `3361` in org-roam.

Let's go through a contrived example.

While checking my email in `mu4e`[^fn:11] and see a message from the CFEngine help list asking how to define a _class_ from a _variable_. The author shared what they had tried but it wasn't working. I want to respond to it so I run `org-roam-dailies-capture` and key in `e` (email) `r` (response). This creates a new node in today's work log with the headline `Responded to cfengineer@some.org Re: How do I define a class from a variable?` and a link back to the message in `mu4e` (that information was automatically pulled directly from the email I was reading when I initiated the capture).

This is the capture template I use for email responses. It populates the necessary property for proper threading (message-id).

```emacs-lisp
("er" "Response" entry
 "* Respond to %:from: %:subject :email:
:properties:
:mail_from: Nick Anderson <nick.anderson@northern.tech>
:mail_to: %:fromaddress
:MAIL_IN_REPLY_TO: <%:message-id>
:end:
%a
#+begin_quote
   %i
#+end_quote\n\n%?"
 :if-new (file+head ,(expand-file-name "work/%<%Y-%m-%d>.org" org-roam-dailies-directory)
                    "#+title: Work log for %<%Y-%m-%d>")
 :clock-in t
 :clock-resume t
 )
```

I start typing my response and use `org-roam-node-find`  to search for pre-existing examples leveraging any functions I want to use linking to them from my note. I use YAsnippet[^fn:12] to insert a cfengine src block. I re-use or write a new example running the block as I go to make sure it does what I expected until I am satisfied. Once finished I run `org-mime-org-subtree-htmlize` which exports the `org-mode` formatted text to a multipart plain text (ascii) and html message. Then I `C-c` to send it off and again to complete my capture. At this point I will probably run `org-roam-capture` type the name of the example, e.g. `class defined from variable` and key in `c` (CFEngine) `e` (Example). In the example I use `org-roam-node-insert` to create links to each function that is used in the example. This helps future me find all the examples that use a specific function from that functions note.

Next I decide that documentation should to be updated, so I run `org-jira-create-issue`, fill out the necessary minimal information and once the ticket has been created I run `org-jira-progress-issue` to set it in progress and I initiate a new work log capture. I run `projectile-switch-project` and switch to the documentation repository. I find the documentation I want to update and yank it. Then I head back to my work log run `org-rich-yank`[^fn:13] to paste the copied text with a link back to where I got it and type something about how it sucks. As I explain why it sucks I visit other repositories yanking other snippets of code for reference to backup my assertion. `ol-git-link` provides some nice capabilities for linking to git forges which is very helpful for others as well as future me doing archaeology.

When updating the Jira ticket I export the notes I took to Jira wiki syntax with `ox-jira`&nbsp;[^fn:14]. I copy that exported text, and then add it to the Jira ticket using `org-jira-add-comment`. Before I start updating the documentation I create a new branch with `magit-branch-create`[^fn:15]. I make the changes I want, commit and push. Forge[^fn:16] let's me proceed to open a pull request, request reviewers, make comments and easily grab the URL of the Pull Request which gets added to my work log which ultimately becomes a well styled comment in the associated Jira issue. Once the PR is approved I merge the pull request with `forge-merge` and close the issue with `org-jira-progress-issue`. Notice that I never left Emacs and my work log functioned as my home base where the notes I took became part of the work I produced in the form of a well styled Jira comment.

{{< figure src="angel-of-memory.png" caption="<span class=\"figure-number\">Figure 3: </span>FHTAGN &amp; TENTACLES — ZACHRIEL - ANGEL OF MEMORY by Peter Mohrbacher posted as a representation of org-mode in response to <https://pkm.social/@markmcelroy/110061567208552787>" >}}

I make presentations in org mode, for example [Org-mode all the thingz!](https://htmlpreview.github.io/?https%3A%2F%2Fgithub.com%2Fnickanderson%2FOrg-mode-all-the-thingz%2Fblob%2Fmaster%2Fpresentation.html) which [I gave at Kansas Linux Fest in 2019](https://www.youtube.com/watch?v=PE4eGkIQycc)[^fn:17].

As you can probably see I make heavy use of org-mode's exporting capabilities. In addition to the above mentioned use cases I also export to ODT, PDF, mediawiki, Slack, Hugo and various other flavors of Markdown.

I (very infrequently) make diagrams with PlantUML[^fn:18]. I might try Mermaid[^fn:19] next time.

I keep secrets in org-mode. The contents of headings that have the crypt tag are automatically GPG encrypted to my GPG key on save.

While I started my journey with org-mode using agenda for GTD and managing tasks, I have yet to master it or really even manage to get it to stick in my workflow but I keep trying. I recently got agenda feeding from a list of files based on `org-roam-db-query`&nbsp;[^fn:20]  This way I can have TODOs all over the place but I can keep agenda fast by keeping the number of files it considers relatively small.

I keep notes on people. My x-files or rolodex consists of one note per person[^fn:21].

I use `org-web-tools` to archive pull copies of web pages into notes so that I have references even when the internet breaks. I take a lot of screenshots while doing things and I pull them into my documents with org-download[^fn:22].

When working on long documents I sometimes turn on `olivetti-mode`[^fn:23]. And I am starting to like org-sticky-header[^fn:24].

I use various things for searching across my org files. When searching for text I use `ripgrep`&nbsp;[^fn:25] , in Spacemacs it's bound to `SPC /` and you are prompted to choose a top level directory to start your search from. Several years back I used Deft[^fn:26] for a while but found that it really didn't suite me well and it simply doesn't perform well[^fn:27] for my volume of files. I still have a bunch of files in my deft directory that should probably just move into my roam.

The default display when using `org-roam-node-find` shows only node names, I find a hierarchy much more useful. I adjusted it to show the node hierarchy using the example shown in the User contributed tricks[^fn:28]. E.g. File title -&gt; heading 1 -&gt; Heading 2 -&gt; ...

<a id="code-snippet--org-roam-node-display-template"></a>
```emacs-lisp
(cl-defmethod org-roam-node-hierarchy ((node org-roam-node))
  (let ((level (org-roam-node-level node)))
    (concat
     (when (> level 0) (concat (org-roam-node-file-title node) " > "))
     (when (> level 1) (concat (string-join (org-roam-node-olp node) " > ") " > "))
     (org-roam-node-title node))))

  (setq org-roam-node-display-template "${hierarchy:200} ${tags:20}")

```

Going mobile with `org-mode` I use a variety of applications to help. I use Syncthing to syncrhonize files across devices. I only synchronize a subset of my org files to mobile devices. I don't really need the ability to access my whole exocortex on the go.

Orgzly is what I use most often. I really like the home screen widget it provides that allows me to build a query showing recent notes. It makes it easy for managing trips to the store. But the editing experience is lacking, and I am in great wish of an improved capture capabilities. It can't deal with a deep directory structure of files and while that isn't much of an issue for me, it would be a great capability and I do miss it. I had some issues with sync conflicts that lead me to introduce a Tasker automation to synchronize the Orgzly db on screen wake. I also make a practice of having one capture file per mobile device. I haven't had many sync conflicts since implementing those things. I re-file my Orgzly captures to my main system way less often than I should. They usually go to my personal journal, someday I hope to have some function to refile to a specific org-roam-dailies-capture template for date at point[^fn:29].

Other applications that I use on mobile that deserve mention:

Logseq
: I really like how daily file are featured. I miss a capture capability. I dislike how the share to target is not stable. It shares to the insertion point. So if the app is open in the background that share might go to some random place I stopped writing. It's convenient at times, other times very inconvenient. I don't love the editing interface. Everything is a headline, so it's a bit ugly when I come to the file in Emacs, but It's what I tend to use if I am writing something longer on mobile, for example that is where I drafted many points for this blog post over the course of a couple months re-visiting it from time to time before I pulled it in to my system for authoring this post.

Metanote
: I don't see other people mention this one. I have found it to be a bit slow but the editing UI is not bad. Also, it has a few capture templates as well as Agenda.

Orgro
: It's read only, so it's of limited use given my current sync patterns but it's good for that.

I don't think about myself being an Emacs user, I feel like an `org-mode` user Emacs is just a delivery system. I've been playing with many things that have yet to gel into my workflow:

ob-translate
: Translate text in Emacs’ org-mode blocks. <https://github.com/krisajenkins/ob-translate>

md4rd
: Read Reddit interactively from within Emacs. <https://github.com/ahungry/md4rd>

org-transclusion
: Org-transclusion lets you insert a copy of text content via a file link or ID link within an Org file. It lets you have the same content present in different buffers at the same time without copy-and-pasting it. Edit the source of the content, and you can refresh the transcluded copies to the up-to-date state. <https://github.com/nobiot/org-transclusion>

Ement.el
: Ement.el is a Matrix client for Emacs. It aims to be simple, fast, featureful, and reliable. <https://github.com/alphapapa/ement.el>

elfeed
: Elfeed is an extensible web feed reader for Emacs, supporting both Atom and RSS. <https://github.com/skeeto/elfeed>

mastadon.el
: Emacs client for Mastodon and other compatible fediverse servers. <https://codeberg.org/martianh/mastodon.el>

org-chef
: org-chef is a package for managing recipes in org-mode. One of the main features is that it can automatically extract recipes from websites like allrecipes.com <https://github.com/Chobbes/org-chef>

org-drill
: Org-Drill is an extension for Org mode. Org-Drill uses a spaced repetition algorithm to conduct interactive "drill sessions", using org files as sources of facts to be memorised. Each topic is treated as a "flash card". <https://orgmode.org/worg/org-contrib/org-drill.html>

org-roam-search
: org-ql like search for org-roam. <https://github.com/natask/org-roam-search>

org-ql
: This package provides a query language for Org files. It offers two syntax styles: Lisp-like sexps and search engine-like keywords. <https://github.com/alphapapa/org-ql>

org-edna
: Extensible Dependencies ’N’ Actions (EDNA) for Org Mode tasks. Edna provides an extensible means of specifying conditions which must be fulfilled before a task can be completed and actions to take once it is. <https://www.nongnu.org/org-edna-el/>

org-mru-clock
: Do you often clock in to many different little tasks? Are you annoyed that you can’t just clock in to one of your most recent tasks after restarting Emacs? <https://github.com/unhammer/org-mru-clock>.

org-noter
: Org-noter’s purpose is to let you create notes that are kept in sync when you scroll through the document, but that are external to it - the notes themselves live in an Org-mode file. <https://github.com/weirdNox/org-noter>

org-cv
: This project exports an org-mode file with reasonably structured items into a latex file, which compiles into a nice CV. <https://titan-c.gitlab.io/org-cv/>

ox-leanpub
: Ox-leanpub includes Org Mode export backends to publish books and courses with Leanpub. ox-leanpub allows you to write your material entirely in Org mode, and manages the production of the files and directories needed for Leanpub to render your book. <https://github.com/zzamboni/ox-leanpub>

org-super-agenda
: This package lets you “supercharge” your Org daily/weekly agenda. The idea is to group items into sections, rather than having them all in one big list. <https://github.com/alphapapa/org-super-agenda>

org-recent-headings
: This package lets you quickly jump to recently used Org headings using Helm, Ivy, or plain-ol’ completing-read. <https://github.com/alphapapa/org-recent-headings>

org-sidebar
: This package presents helpful sidebars for Org buffers. Sidebars are customizable using org-ql queries and org-super-agenda grouping. <https://github.com/alphapapa/org-sidebar>

org-protocol-capture-html
: You can select text in the page when you capture by clicking a bookmarklet it will be copied into the template, or you can just capture the page title and URL. A selection-grabbing function is used to capture the selection. <https://github.com/alphapapa/org-protocol-capture-html>

emacs-slack
: Slack from inside Emacs. <https://github.com/yuya373/emacs-slack/>

literate-calc-mode
: Literate programming for M-x calc. Displays inline results for calculations, supports variables and updates as you type (if you want). <https://github.com/sulami/literate-calc-mode.el>

org-similarity
: org-similarity is a package to help Emacs org-mode users discover similar or related files. Under the hood, it uses Python and scikit-learn for text feature extraction, and nltk for text pre-processing. More specifically, this package provides a function to recursively scan a given directory for org files, clean their content by stripping the front matter and some undesired characters, tokenize them, replace each token with its respective linguistic stem, generate a TF-IDF sparse matrix, and calculate the cosine similarity between these documents and the buffer you are currently working on. <https://github.com/brunoarine/org-similarity>

focused
: A package that dims surrounding text. It works with any theme and can be configured to focus in on different regions like sentences, paragraphs or code-blocks. <https://github.com/larstvei/Focus>

aggressive-indent-mode
: A minor mode that keeps your code always indented. It reindents after every change, making it more reliable than electric-indent-mode. <https://github.com/Malabarba/aggressive-indent-mode>

crux
: A Collection of Ridiculously Useful eXtensions for Emacs. crux bundles many useful interactive commands to enhance your overall Emacs experience. <https://github.com/bbatsov/crux>

[^fn:1]: Checkout the post reflecting on my history with org-mode in 2023. <https://cmdln.org/2023/03/13/reflecting-on-my-history-with-org-mode-in-2023/>
[^fn:2]: According to the [introduction in the manual](https://www.orgroam.com/manual.html#Introduction) Org-roam is a tool for networked thought. It reproduces some of [Roam Research’](https://roamresearch.com/)s key features within Org-mode. Org-roam allows for effortless non-hierarchical note-taking: with Org-roam, notes flow naturally, making note-taking fun and easy.
[^fn:3]: Maggie Appleton has a nice post about [Daily notes as a frictionless default input for personal knowledge management systems](https://maggieappleton.com/daily-notes).
[^fn:4]: ADHD is a real thing. I am also not perfect in remembering to capture each thing but I don't need to be perfect to be effective.
[^fn:5]: If you like org-mode, you might also like CFEngine. It really is a knowledge management tool for infrastructure and it's very flexible and open ended much like the numerous ways of using org-mode, there are many different ways of using CFEngine. It's a tool that has few prescriptions.
[^fn:6]: I've been told multiple times by colleagues that they search out my meeting notes to help themselves complete periodic reviews. I hate doing periodic reviews, so knowing that my effort helps others in this regard is a strong motivator.
[^fn:7]: (maybe someone can suggest how that tho step process could be consolidated)
[^fn:8]: (similar to <https://daryl.wakatara.com/emacs-gtd-flow-evolved/#crm-system>)
[^fn:9]: (org-mime-htmlize-subtree in this case) as this is one of the few daily capture templates where I capture each day to a heading in a file for the month (it's easier for people that have access to a git repo containing these files to use for periodic reviews).
[^fn:10]: There are so many, org-mime is probably my most often used exporter followed by some flavor of Markdown (ox-hugo like this blog post, ox-gfm, ox-slack).
[^fn:11]: With mu4e I have offline mail reading and search and I run a local Postfix relay giving me offline sending capability.
[^fn:12]: [YASnippet](https://github.com/joaotavora/yasnippet) is a template system for Emacs. It allows you to type an abbreviation and automatically expand it into function templates. The snippet syntax is inspired from [TextMate'](https://macromates.com/manual/en/snippets)s syntax, you can even import most TextMate templates to YASnippet.
[^fn:13]: org-rich-yank pastes the last copied text and automatically surrounds the snippet in blocks, marked with the major mode of where the code came from, and adds a link to the source file after the block. I do wish that it would provide an option for the link being <https://github.com/unhammer/org-rich-yank>
[^fn:14]: ox-jira exports to Jira wiki markup. It's very nice to author fairly pretty comments with so little effort. <https://github.com/stig/ox-jira.el>
[^fn:15]: Magit is an amazing front end for git. <https://magit.vc/>
[^fn:16]: Forge provides git forge integration (pull requests, issues, etc ..) for GitLab, GitHub and probably others. <https://github.com/magit/forge>
[^fn:17]: Org source for the Org-mode all the thingz! presentation is available [here](https://github.com/nickanderson/Org-mode-all-the-thingz/blob/master/presentation.org).
[^fn:18]: The org-mode documentation has a nice article about making diagrames with PlanUML. <https://orgmode.org/worg/org-contrib/babel/languages/ob-doc-plantuml.html>
[^fn:19]: Mermaid is a JavaScript based diagramming and charting tool that renders Markdown-inspired text definitions and you can use [ob-mermaid](https://github.com/arnm/ob-mermaid) to generate them from within org-mode.
[^fn:20]: Here is my post on Matson showing the elisp for using `org-roam-db-query` to set agenda files for a custom agenda command <https://fosstodon.org/@nickanderson/109979927683467557>
[^fn:21]: Darly Wakatara has a nice post about how his workflow has evolved  <https://daryl.wakatara.com/emacs-gtd-flow-evolved/>. I noted that his contact management workflow is similar to mine. Sometime it would be nice to figure out how this could be leveraged for address completion in `mu4e`. There is [org-contacts](https://orgmode.org/worg/org-contrib/org-contacts.html) but it's not clear to me if I can use it with a file per person strategy.
[^fn:22]: `org-download` makes it easy to insert images into a document, it provides functions for taking and inserting screenshots, downloading images, renaming images as well as dragging and dropping images into your document. <https://github.com/abo-abo/org-download>
[^fn:23]: Olivetti provides nice styling for writing. <https://github.com/rnkn/olivetti>
[^fn:24]: org-sticky-heading displays in the header-line the Org heading for the node that’s at the top of the window. This way, if the heading for the text at the top of the window is beyond the top of the window, you don’t forget which heading the text belongs to. The display can be customized to show just the heading, the full outline path, or the full outline path in reverse. <https://github.com/alphapapa/org-sticky-header>
[^fn:25]: ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern. It's _very_ fast and can even has some support for searching compressed files, multiline search. <https://github.com/BurntSushi/ripgrep>
[^fn:26]: Deft takes inspiration from Notational Velocity. I still think it's a neat package and something I would recommend to new org-mode users. <https://notational.net/>
[^fn:27]: notDeft it features a Xapian database for providing fast full text search for very large volumes of notes. I haven't tried it but I haven't found myself needing something more from ripgrep for full text search much. <https://github.com/hasu/notdeft>
[^fn:28]: Lot's of good tips in the org-roam wiki user contributed tricks. My favorite so far is for showing the node hierarchy. <https://github.com/org-roam/org-roam/wiki/User-contributed-Tricks#showing-node-hierarchy>
[^fn:29]: I am super slow working towards this, so if you want to offer up some elisp for me to use I would be most grateful.