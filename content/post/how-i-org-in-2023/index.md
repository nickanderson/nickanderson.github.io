+++
title = "How I org in 2023"
date = 2023-03-25
tags = ["org-mode", "org-roam", "pkm"]
draft = false
author = "Nick Anderson"
+++

I've been pretty much living in `org-mode` for 6 or 7 years now[^fn:1]. It's my exocortex, second brain, second mind, mind palace, pensive, and personal knowledge management system[^fn:2]. The features and tools I use as well as how I organize my files has changed quite a bit over this period of time and I thought it would be nice give myself (and anyone else who cares) a reference of what it was like in 2023 so here it is.

{{< figure src="org-mode-this-is-the-way.jpg" caption="<span class=\"figure-number\">Figure 1: </span>It is the way, at least for me" width="50%" >}}


## Goal {#goal}

Unrealistically I want total recall, to remember everything in durable plain text. I want to have control of my data. I want to do my work and interact efficiently. I want to improve my knowledge and capabilities and I want to be able to share with others.


## High level statistics {#high-level-statistics}

As of `Friday, December 15, 2023` I had `56M` of `.org` files in `~/org`. That's  `4889` files and `1186734` lines of text, the largest single file was `1.3M` and the longest lined file was `26370` lines.

`4716` of these files were inside org-roam, the majority of them (`3558`) were "dailies" or time-series files.[^fn:3]

I had some `27M` other older `.org` files outside `~/org` that aren't even included in those stats. The largest of those files  was `5.6M`, and the longest lined file had `81921` lines. At couple centuries ago glacial speed (I guess they are moving pretty quickly these days) I refiled things from there into `~/org`. Not to mention `~/Syncthing/Orgzly` with `7.9M` worth of `.org` files that I synced around to a few devices and the largest `.org` file was `677K` with the most lined file having `49670` lines.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8A52ZXPhJFk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## System {#system}

I don't really use any existing workflow or organization methodology like PARA, CODE, ACCESS, Johnny Decimal, etc ... I don't know that I am organized (or disciplined?) enough to follow some thing like that. I appreciate them and pick up ideas reading about methodologies that work for others.

I use the Nick Anderson S.H.I.T. (Stuff here 'n there) methodology.

{{< figure src="nick-anderson-shit-method.png" caption="<span class=\"figure-number\">Figure 2: </span>Martti Bergström (@masi@fosstodon.org) uses the Nick Anderson SHIT meethod. <https://fosstodon.org/@masi/110266696809445948>" width="50%" >}}

I capture as much as I reasonably can. When I see enough of the same type of things I try to pile them near each other and build some kind of pneumatic tube to automatically funnel similar things into the right pile automatically.

{{< figure src="robot-pnumatic-tubes-piles-of-notes-1.png" caption="<span class=\"figure-number\">Figure 3: </span>A system of pneumatic tuebes coming out from a male robotic individual sucking up documents and blowing them out into piles. Use a realistic future sci-fi style." width="50%" >}}

I started tracking much of my various collections of piles in version control and  you can watch a [gource generated visualization here](https://www.youtube.com/watch?v=b7y0y6sWb2I).

{{< figure src="gource-screenshot.png" caption="<span class=\"figure-number\">Figure 4: </span>Frame from gource visualization" width="50%" >}}


## Capture {#capture}

Capturing is an important concept. Fundamentally it's grabbing new content and putting it somewhere. It facilitates consistency and automates some tedium. It's something that should be fast and not interrupt my flow.

`org-roam`[^fn:4] is my primary capture interface and I _really_ like the daily capabilities. Each day I capture notes about everything I am working on into my work log while clocking time. This gives me a nice place to think and process what I am working on[^fn:5] as well as a place to get my bearings and see what I had been working on when I got side-tracked[^fn:6]. Having a new file each day gave me a fresh start and it helped me to avoid performance issues I had previously experienced with large (multi-megabyte) files. I still had a lot of org files not under my roam directory which I had yet to (and may never fully) migrate.

I had `24` org-capture-templates,  `16` org-roam-capture-templates and `75` org-roam-dailies-capture-templates.

{{< figure src="angel-of-memory.png" caption="<span class=\"figure-number\">Figure 5: </span>FHTAGN &amp; TENTACLES — ZACHRIEL - ANGEL OF MEMORY by Peter Mohrbacher posted as a representation of org-mode in response to <https://pkm.social/@markmcelroy/110061567208552787>" width="50%" >}}

Beyond my time-series notes I had other collections of related notes in sub directories. For example, I had many notes about CFEngine (the best configuration management tool)[^fn:7]. I kept my CFEngine related notes in `~/org/roam/CFEngine` with sub directories for different things ( blogs, examples, index.org, northern.tech-customers, notes, opportunities,
).

I used `org-web-tools` to pull web pages into org. Either as a buffer to read, or as a subtree to store.

`org-rich-yank`[^fn:8] let me copy text and paste it with context allowing it to be syntax highlighted as well as providing a link back to the source.


## Retrieval {#retrieval}

When I am retrieving information from my system I am usually searching for a note by name or searching for what notes I have about something.

When searching for a note by name, I'll use `org-roam-node-find`.

When I am searching wide I use `ripgrep` via `consult-ripgrep` which is bound to `SPC /` and searches `~/org` by default.

If I have found a note I can see what other notes link to it with `org-roam-buffer`. There is even support for finding _unlinked_ back references, which I am not using for performance reasons.

{{< figure src="org-roam-buffer.png" >}}

`org-roam-ui` provides a really fun interactive 2 or 3d graph showing the links between nodes allowing you to explore your notes visually.

{{< figure src="org-roam-ui-browse-notes.png" caption="<span class=\"figure-number\">Figure 6: </span>Browsing this node in org-roam-ui" width="50%" >}}

{{< figure src="org-roam-ui-with-dailies-2023-03-26.png" caption="<span class=\"figure-number\">Figure 7: </span>org-roam-ui visualization with dailies as of 2023-03-26" width="50%" >}}

{{< figure src="org-roam-ui-without-dailies-2023-03-26.png" caption="<span class=\"figure-number\">Figure 8: </span>org-roam-ui visualization without dailies as of 2023-03-26" width="50%" >}}

`org-roam-random-note` can be fun to stumble around completely random nodes. There exists a video on YouTube but I'm currently unable to find the reference where someone customizes their startup to display a random note.

`org-agenda` can be fed by `org-roam-db-query`, helping to solve the issue of figuring out which files should be included by agenda. I have done this, but I still don't really make use of `org-agenda`, I want to, but it hasn't clicked for me yet so I just keep poking at it a few times a year.

org-roam-dynamic-blocks is neat for maintaining a list of notes matching some criteria from org-roam though I don't make use of this near as much as I would like yet.


## Output {#output}

Output is an important aspect of my system. It's important to me that I can easily share my knowledge with others.

I use org-babel frequently. It's very convenient and efficient to be able to execute code directly in my documents.
Copying and pasting between a console and what I am writing introduces much chance for error. Having code blocks and in-line execution improve the accuracy of my notes and anything else that I am producing.

For example, the Statistics section of this post uses inline code blocks and the data is freshly generated each time I export an updated version. Named blocks let me inject dynamic content in a sentence and provides easy access for on-demand execution, not to mention the ability to leverage as input to other blocks.

I have begun to make more consistent use of `org-transclusion`[^fn:9] while authoring content. Instead of duplicating content copying to the new place I want to use it I will distill what I want to use into an atomic chunk and then reference it. I find this is helpful in several ways. It reduces unnecessary growth to the volume of text that I have, reduces the number of duplicate hits for things when I am searching for something, increases the interlinking of my org-mode files providing a more rich experience with `org-roam-buffer` showing things that used the content as well as interconnected in the `org-roam-ui` graph visualization.

With so many export backends available I don't usually have to spend time mucking around with some bespoke syntax. I can author in org-mode and quickly export it to another format. It's nice to have relatively good formatting in many formats with relatively little effort.

I export using `ox-jira` and use `org-jira` to manage issues in Jira Cloud. Again, everyone benefits from well styled comments and ticket descriptions and no real extra effort is required from me.

I make presentations using `org-reveal` and `org-re-reveal` with nice features like speaker notes. These presentations can also be printed to PDF.

I write reports that I export to ODT for copying and pasting into google drive[^fn:10] and PDF for emailing to clients.

I write blog posts exporting with `ox-hugo` to multiple websites using different hugo configurations.

I author emails in org-mode exported with `org-mime`[^fn:11] as a multi-part ASCII &amp; HTML message.

`abbrev-mode` is amazing at auto correcting my most common typos. `writegood-mode` and `olivette` are both nice for writing.


## Workflow {#workflow}

So, how does a day in my org life flow?

Usually my day starts with meetings. I like to take notes and email them to a distribution list afterwords[^fn:12]. For example, a few minutes before my CFEngine stand-up I run `org-roam-dailies-capture-today` and key in `w` (work) `m` (meeting) `c` (CFEngine) `d` (daily stand-up). Immediately after activating this capture I trigger another capture for my work log keying in `w` (work) `l` (log)[^fn:13] which clocks time.

{{< figure src="standup-worklog.gif" caption="<span class=\"figure-number\">Figure 9: </span>Animation showing standup and worklog capture" width="100%" >}}

The work log capture template includes a backlink to the stand-up note for the day, so I follow that link and start going through my template filling it out. The template has a headline for each person with a property that links to a node for the individual. My own section contains a clock table which quickly produces a nice list of the entries with clocked time from the previous day (on Mondays or days when I have missed prior N days I tweak the clock table to pull for the right number of previous days). I review the table to see how good I was about clocking the previous day back-filling anything that I neglected to record then delete time columns.

At the end of the meeting I use `org-mime`[^fn:11] to prepare a nicely formatted multipart ASCII &amp; HTML email. After sending the mail I switch back to my work log capture and complete it. All of my regularly scheduled meetings follow the same process; I capture for the meeting template, then I capture to my work log clocking time with an automatic backlink back to the specific meeting note. It's easy to capture notes for yesterday, tomorrow or an arbitrary date in the future using `org-roam-dailies-capture-yesterday`, `org-roam-dailies-capture-tomorrow`, and `org-roam-dailies-capture-date`.

Org-roam provides useful functions for accessing time-series notes. `org-roam-dailies-goto-today` will take you to today's note for the selected template and if the file does not exist it is initialized. Similarly `org-roam-dailies-goto-yesterday`, `org-roam-dailies-goto-tomorrow`, and `org-roam-dailies-goto-date` take you to the note for yesterday, tomorrow, or the specified date, creating the file if necessary. `org-roam-dailies-goto-previous` and `org-roam-dailies-goto-next` go to the previous and next note in the series based on the file you are currently visiting making for easy navigation through the time series.

`org-roam-node-random` is fun, as it says, it takes you to a random node. It's nice for serendipitous stumbles.

If I am working on something that has some regular pattern but is not a recurring time series I follow a similar pattern, but instead of `org-roam-dailies-capture` I run `org-roam-capture`. Unlike `org-roam-dailies-capture` `org-roam-capture` first prompts for a node title and you select a template afterwords. For example, if I am working on support case I will run `org-roam-capture`, enter the issue number and then key in `w` (work) `s` (support). I am taken to a new node in the file for that support case where I immediately trigger `org-roam-dailies-capture` for my work log which starts clocking time and I follow the link back to the node to continue my work.

For other activities that are typically fast or aren't of a common type spanning multiple days I simply run `org-roam-dailies-capture` and keep notes directly in my work log.

I author pretty much everything in `org-mode`. I am often able to stay in inside `org-mode` and keep a very thorough record of my exact activities. When I need to run commands I typically use `org-babel` so that commands their output and my thoughts about it form a nice log of my work as I proceed. This log is often directly transferable to communicate with others for which I leverage the copious export back ends available[^fn:14].

As of Friday, December 15, 2023
 I currently have  `15189` nodes across `4716` files in org-roam.


### Contrived example {#contrived-example}

Let's go through a contrived example.

While checking my email in `mu4e`[^fn:15] and see a message from the CFEngine help list asking how to define a _class_ from a _variable_. The author shared what they had tried but it wasn't working. I want to respond to it so I run `org-roam-dailies-capture` and key in `e` (email) `r` (response). This creates a new node in today's work log with the headline `Responded to cfengineer@some.org Re: How do I define a class from a variable?` and a link back to the message in `mu4e` (that information was automatically pulled directly from the email I was reading when I initiated the capture).

This is the capture template I use for email responses. It populates the necessary property for proper threading (message-id).

```emacs-lisp
("e" "Email")
("er" "Response" entry
 "* Respond to %:from: %:subject :email:
:properties:
:mail_from: Nick Anderson <nick.anderson@northern.tech>
:mail_to: %:fromaddress
:MAIL_IN_REPLY_TO: <%:message-id>
:MAIL_SUBJECT: %:subject
:REF: %a
:end:
#+begin_quote
   %i
#+end_quote

%?"
 :if-new (file+head ,(expand-file-name
                      "work/%<%Y-%m-%d>.org"
                      org-roam-dailies-directory)
                    "#+title: Work log for %<%Y-%m-%d>")
 :clock-in t
 :clock-resume t
 )
```

I start typing my response and use `org-roam-node-find`  to search for pre-existing examples leveraging any functions I want to use linking to them from my note. I use YAsnippet[^fn:16] to insert a cfengine src block. I re-use or write a new example running the block as I go to make sure it does what I expected until I am satisfied. Once finished I run `org-mime-org-subtree-htmlize` which exports the `org-mode` formatted text to a multipart plain text (ascii) and html message. Then I `C-c` to send it off and again to complete my capture. At this point I will probably run `org-roam-capture` type the name of the example, e.g. `class defined from variable` and key in `c` (CFEngine) `e` (Example). In the example I use `org-roam-node-insert` to create links to each function that is used in the example. This helps future me find all the examples that use a specific function from that functions note.

Next I decide that documentation should to be updated, so I run `org-jira-create-issue`, fill out the necessary minimal information and once the ticket has been created I run `org-jira-progress-issue` to set it in progress and I initiate a new work log capture. I run `projectile-switch-project` and switch to the documentation repository. I find the documentation I want to update and yank it. Then I head back to my work log run `org-rich-yank` to paste the copied text with a link back to where I got it and type something about how it sucks. As I explain why it sucks I visit other repositories yanking other snippets of code for reference to backup my assertion. `ol-git-link` provides some nice capabilities for linking to git forges which is very helpful for others as well as future me doing archaeology.

When updating the Jira ticket I export the notes I took to Jira wiki syntax with `ox-jira`&nbsp;[^fn:17]. I copy that exported text, and then add it to the Jira ticket using `org-jira-add-comment`. Before I start updating the documentation I create a new branch with `magit-branch-create`[^fn:18]. I make the changes I want, commit and push. Forge[^fn:19] let's me proceed to open a pull request, request reviewers, make comments and easily grab the URL of the Pull Request which gets added to my work log which ultimately becomes a well styled comment in the associated Jira issue. Once the PR is approved I merge the pull request with `forge-merge` and close the issue with `org-jira-progress-issue`. Notice that I never left Emacs and my work log functioned as my home base where the notes I took became part of the work I produced in the form of a well styled Jira comment.
I make presentations in org mode, for example [Org-mode all the thingz!](https://htmlpreview.github.io/?https%3A%2F%2Fgithub.com%2Fnickanderson%2FOrg-mode-all-the-thingz%2Fblob%2Fmaster%2Fpresentation.html) which [I gave at Kansas Linux Fest in 2019](https://www.youtube.com/watch?v=PE4eGkIQycc)[^fn:20].

As you can probably see I make heavy use of org-mode's exporting capabilities. In addition to the above mentioned use cases I also export to ODT, PDF, mediawiki, Slack, Hugo and various other flavors of Markdown.

I (very infrequently) make diagrams with PlantUML[^fn:21]. I might try Mermaid[^fn:22] next time.

I keep secrets in org-mode. The contents of headings that have the crypt tag are automatically GPG encrypted to my GPG key on save.

While I started my journey with org-mode using agenda for GTD and managing tasks, I have yet to master it or really even manage to get it to stick in my workflow but I keep trying. I recently got agenda feeding from a list of files based on `org-roam-db-query`&nbsp;[^fn:23]  This way I can have TODOs all over the place but I can keep agenda fast by keeping the number of files it considers relatively small.

I keep notes on people. My x-files or rolodex consists of one note per person[^fn:24]<sup>, </sup>[^fn:25].

I use `org-web-tools` to archive pull copies of web pages into notes so that I have references even when the internet breaks. I take a lot of screenshots while doing things and I pull them into my documents with org-download[^fn:26].

When working on long documents I sometimes turn on `olivetti-mode`[^fn:27]. And I am starting to like org-sticky-header[^fn:28].

I use various things for searching across my org files. When searching for text I use `ripgrep`&nbsp;[^fn:29] , in Spacemacs it's bound to `SPC /` and you are prompted to choose a top level directory to start your search from. Several years back I used Deft[^fn:30] for a while but found that it really didn't suite me well and it simply doesn't perform well[^fn:31] for my volume of files. I still have a bunch of files in my deft directory that should probably just move into my roam.

The default display when using `org-roam-node-find` shows only node names, I find a hierarchy much more useful. I adjusted it to show the node hierarchy using the example shown in the User contributed tricks[^fn:32]. E.g. File title -&gt; heading 1 -&gt; Heading 2 -&gt; ...

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


### Mobile {#mobile}

Going mobile with `org-mode` I use several different applications to help.

I use Syncthing to syncrhonize files across devices. I only synchronize a subset of my org files to mobile devices. I don't really need the ability to access my whole exocortex on the go.

Orgzly is my primary capture tool on mobile. My `Orgzly` directory is synchronized across all of my mobile devices. Each device that I use Orgzly on has a device specific file that is configured as the `Default notebook`.  I really like the home screen widget, I typically have it showing a query showing notes from the device specific file created in the last 3 days. If I want to take a note I use the `+` button on the home screen widget, there is also an option for a new note in the notifications drop-down drawer but I tend not to use that. It's pretty serviceable for short notes about something, e.g. "Saw Brian at the store, he broke his foot. We should get together and grill." or lists for the store e.g. "TODO Milk :@store:", "TODO Black Beans :@store:".

It makes it easy for managing trips to the store. But the editing experience is lacking, and I am in great wish of an improved capture capabilities. It can't deal with a deep directory structure of files and while that isn't much of an issue for me, it would be a great capability and I do miss it. I had some issues with sync conflicts that lead me to introduce a Tasker automation to synchronize the Orgzly db on screen wake[^fn:33]. I also make a practice of having one capture file per mobile device. I haven't had many sync conflicts since implementing those things. I re-file my Orgzly captures to my main system way less often than I should. They usually go to my personal journal, someday I hope to have some function to refile to a specific org-roam-dailies-capture template for date at point[^fn:34].

Other applications that I use on mobile that deserve mention:

Logseq
: I really like how daily file are featured. I miss a capture capability. I dislike how the share to target is not stable. It shares to the insertion point. So if the app is open in the background that share might go to some random place I stopped writing. It's convenient at times, other times very inconvenient. I don't love the editing interface. Everything is a headline, so it's a bit ugly when I come to the file in Emacs, but It's what I tend to use if I am writing something longer on mobile, for example that is where I drafted many points for this blog post over the course of a couple months re-visiting it from time to time before I pulled it in to my system for authoring this post.

Metanote
: I don't see other people mention this one. I have found it to be a bit slow but the editing UI is not bad. Also, it has a few capture templates as well as Agenda.

Orgro
: It's read only, so it's of limited use given my current sync patterns but it's good for that.


### LLMs {#llms}

2023 was a banner year for generative AI and like many others I dabbled to see how my workflow could benefit from the use of large language models. While OpenAI was all the rage, I was mostly interested in local LLMs.


#### org-ai {#org-ai}

In June I started to use `org-ai`[^fn:35] for a bit but it required emacs 28.2 which I don't run regularly and additionally the way it used blocks felt a bit un-natural.


#### chatgpt-shell {#chatgpt-shell}

In July 5th 2023 I began using `chatpt-shell`[^fn:36] for dall-e and chatgpt. But given my aversion to using hosted services I didn't use it often.

You can use the shell conversationally with chatgpt or dall-e.

{{< figure src="asking-dall-e-to-make-image-in-dall-e-shell.png" caption="<span class=\"figure-number\">Figure 10: </span>Asking Dall-e to make an image using the interactive dall-e-shell" width="50%" >}}

Most often I use babel src blocks but I seem to lose context history with that so I tend to re-feed my entire query. I've used it to help me re-word text, brainstorm creative ideas, and generate shell one-liners, all from the comfort of my Emacs org-mode buffer.

```text
#+name: chatgpt-prompt
#+begin_src chatgpt-shell
  You are a devotee to the church of emacs and the way of org-mode. Write a short creed in the style of the Mandalorian.
#+end_src
```

```text
This is the Way of the Church of Emacs, sworn to the reverence of org-mode.

I am a devout disciple, bound to the path of sublime productivity, guided by the spirit of the Mandalorian.

In the sacred realm of Emacs, I embrace the true Force, with org-mode as my ally and ally of my thoughts.

I reclaim the scattered chaos and forge a majestic union between my mind and the machine, as the Mandalorian molds armor from Beskar.

With fervent keystrokes, I document my purpose, my tasks, and my dreams, for org-mode is my sacred codex, unyielding in its power.

I wield the formidable swords of agenda and timeline, slicing through the veils of confusion, illuminating the path towards mastery.

My inbox is an abyss, but I, the chosen one, embrace it fearlessly. I tame it with Org Capture, capturing ideas like a bounty hunter snatches fugitives.

My rituals are sacred: I nest headings, cultivate hierarchies, and summon clarity amidst the chaos. I create tables, agendas, and outlines, as the Mandalorian carefully constructs his battlesuit.

I heed the whispers of tags and properties, for they are the sigils that unlock the arcane powers of organization and navigation within my realm.

In the Church of Emacs, I am conscious of the present, for the Clock ticks onwards, tracking the flow of time, ensuring that I honor its value.

I traverse the vast landscapes of my org-files, maneuvering swiftly between them, indexing my solemn pursuits, as the Mandalorian voyages across galaxies.

Not bound by mere text, the Church of Emacs embraces diversity; I integrate spreadsheets, embed images, and attach files, uniting all knowledge beneath org-mode's banner.

Though others may falter amidst the allure of flashy tools, I, like the Mandalorian, hold steadfast loyalty to simplicity, cherishing org-mode's humility.

My brethren, fellow pilgrims of pure productivity, unite with me. Together, we cultivate the principles of steadfastness, focus, and intelligent automation.

I pledge allegiance to the Church of Emacs, the Way of org-mode, for in its embrace lies boundless power and the secrets of imperial efficiency.

This is our Creed. This is the Way.

```

Looking forward to some package that will support bard or claude 2[^fn:37] but really I am mostly waiting to have easy access to a local LLM that I can train on my `~/org`.


#### llm {#llm}

With `llm`[^fn:38] I have access to local llms, but I haven't figured out how I could train on my notes yet.

{{< figure src="ask-local-llm-write-ode-and-dall-e-picture-it.png" caption="<span class=\"figure-number\">Figure 11: </span>Asking a local llm to write an ode to org-mode and dall-e to make a picture of a futuristic robot singing said ode using src blocks." width="50%" >}}


#### Khoj {#khoj}

By August 13th I had started to play with Khoj[^fn:39]. It's neat, but was terribly slow with the local model. By October 17th Khoj had added support for GPU offload and the speed of the local LLM responses improved greatly. Around this time the developers got quite busy with larger re-architectures and running Khoj locally was not working well and sadly my use decreased. It's really nice that the developers actually use org-mode themselves and there is support from within Emacs.

```org
** 🤔 *You*: Summarize how I org in 2023.
   :PROPERTIES:
   :RECEIVED: [2023-08-13 23:54:33]
   :END:

*** 🏮 *Khoj*:   Based on the provided text, here is a summary of how you organize your work in 2023:
   :PROPERTIES:
   :RECEIVED: [2023-08-14 00:01:41]
   :END:
You have been using org-mode for 6 or 7 years now and it has become your "exocortex," "second brain," and "personal knowledge management system." You use various tools and features within org-mode to manage your files, including capturing information through templates, organizing them into different categories, and using tags to label important items.
You have over 48 million .org files in your main org directory, with the majority of them being "dailies" or time-series files. You also use a combination of capture templates (24 for org-mode, 16 for org-roam-capture-templates, and 68 for org-roam-dailies-capture-templates) to help you quickly capture information and organize it within your system.
Your goal is to have total recall of all the information in your system, as well as control over your data, improved knowledge and capabilities, and the ability to share with others. You also keep track of high-level statistics for your org files, including the size of each file and the number of lines in the longest file.
Overall, you have a complex and detailed system for managing your work and personal information using org-mode, which allows you to stay organized, efficient, and productive.^{ [fn:14]}^{ [fn:15]}^{ [fn:16]}
**** References
:PROPERTIES:
:VISIBILITY: folded
:END:
[fn:14] ** [[https://cmdln.org/2023/03/25/how-i-org-in-2023/][How I org in 2023 ·]].
 CREATED: [2023-06-12 Mon 12:01]
[ME]: In the following I will show you a question and then a text. I want you to answer that question based on the text. Use the text as primary source but also add any external information you think is relevant.
Here is the question:
 Summarize this text.
Here is the text:
 I’ve been pretty much living in org-mode for 6 or 7 years now1. It’s my
 exocortex, second brain, and personal knowledge management
 system. The features and tools I use as well as how I organize my files
 has changed quite a bit over this period of time and I thought it would
 be nice give myself (and anyone else who cares) a reference of what it
 was like in 2023 so here it is.
 Figure 1: It is the way, at least for me
 Figure 1: It is the way, at least for me
 Goal
 Unrealistically I want total recall, to remember everything in durable
 plain text. I want to have control of my data. I want to improve my
 knowledge and capabilities and I want to be able to share with others.
 High level statistics
 As of Sunday, June 11, 2023 I have 48M of .org files in ~/org. That’s 4178
 files, the largest single file is 1.3M and the longest lined file has 21639
 lines.
 4001 of these files are inside org-roam, the majority of them (3028) are
 “dailies” or time-series files.2
 I have 24 org-capture-templates, 16 org-roam-capture-templates and 68
 org-roam-dailies-capture-templates.
 Capture
 Capturing
[fn:15] ** /home/nickanderson/org/roam/cmdln.org/20230317222611-how_i_org_in_2023.org.
 I've been pretty much living in =org-mode= for 6 or 7 years now[fn:1]. It's my exocortex, second brain, second mind, mind palace, pensive, and personal knowledge management system[fn:2]. The features and tools I use as well as how I organize my files has changed quite a bit over this period of time and I thought it would be nice give myself (and anyone else who cares) a reference of what it was like in 2023 so here it is.
[[./attachments/how-i-org-in-2023/org-mode-this-is-the-way.jpg]]

[fn:16] ** Expanding on [[id:2f60c4c8-2c4b-488c-b1f0-17f2b4821519][How I org in 2023]].

Adding in notes about [[id:4d53e175-3ec7-4bb5-ae4a-37add1f0aee7][org-transclusion]].
more adjectives to describe what my org-mode is (second mind, mind palace, pensive

```

Looking forward to 2024 where I hope to see the self hosting and general usability improve.

Specifically I hope to see:

-   Improvements to the Emacs client so that it does not block Emacs waiting on llm inference (search has been lightning fast).
-   Easy self hosting out of the box with GPU offload support.
-   Improved RAG, leveraging my notes is amazing, but my notes mish-mash of structuring don't seem to work well.
-   Easier swapping of local models. Maybe even via Ollma


#### gptel {#gptel}

By the end of October I started using `gptel`&nbsp;[^fn:40]. Initially I used it with GPT4All Desktop but quickly found ollma which made it very easy to try different models as well as running queries from the CLI. gptel has such a light weight interface, it became my primary llm interface. Wherever I am, I can easily select some text and ship it off to the llm of my choice with a prompt.

It would be really neat if support for Khoj was added so that I could easily ask questions about my notes. `gptel` doesn't block waiting for LLMs to respond like the Khoj package did.

The author is quite responsive, great package, 10/10 recommend.

<https://github.com/karthink/gptel>


### Other things I use, play with or intend to play with {#other-things-i-use-play-with-or-intend-to-play-with}

I don't think about myself being an Emacs user, I feel like an `org-mode` user Emacs is just a delivery system. I've been playing with many things that have yet to gel into my workflow:

ob-translate
: Translate text in Emacs’ org-mode blocks. <https://github.com/krisajenkins/ob-translate>

md4rd
: Read Reddit interactively from within Emacs. <https://github.com/ahungry/md4rd>

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

osm
: Osm.el is a tile-based map viewer, with a responsive movable and zoomable display. You can bookmark your favorite locations using regular Emacs bookmarks or create links from Org files to locations.  <https://github.com/minad/osm>

org-ref
: org-ref makes it easy to insert citations, cross-references, indexes and glossaries as hyper-functional links into org files. <https://github.com/jkitchin/org-ref>

org-cite
: <https://orgmode.org/manual/Citations.html>

org-bibtex
: Org-bibtex is responsible for handling bibtex citation in orgmode. <http://gewhere.github.io/org-bibtex>

orgmdb
: Tools for managing your watchlist in org-mode and some functions for interacting with OMDb API. <https://github.com/isamert/orgmdb.el>

org-roam-review
: Provides commands to categorise and review org-roam nodes for Evergreen note-taking. Notes are surfaced using the spaced-repetition algorithm from org-drill. <https://github.com/chrisbarrett/nursery/blob/main/lisp/org-roam-review.el>

org-pretty-table
: Draw pretty unicode tables in org-mode and orgtbl-mode. <https://github.com/Fuco1/org-pretty-table>

org-roam-timestamps
: Small package to keep track of the modification and creation time of individual nodes. <https://github.com/tefkah/org-roam-timestamps>

camcorder.el
: Record screencasts directly from emacs. <https://github.com/Malabarba/camcorder.el>

org-msg
: Use org-mode for authoring email. Seems to be centered around mail client use vs org-mime which seems more around emailing from org-mode. <https://github.com/jeremy-compostella/org-msg>

gptai
: One of the many ai related things I want to look into some day. <https://github.com/antonhibl/gptai>

chatgpt
: One of the many ai related things I want to look into some day. <https://github.com/emacs-openai/chatgpt>

codegpt
: One of the many ai related things I want to look into some day. <https://github.com/emacs-openai/codegpt>

ChatGPT.el
: One of the many ai related things I want to look into some day. <https://github.com/joshcho/ChatGPT.el>

gpt.el
: One of the many ai related things I want to look into some day. <https://github.com/stuhlmueller/gpt.el>

chatgpt-arcana.el
: One of the many ai related things I want to look into some day. <https://github.com/CarlQLange/chatgpt-arcana.el>

openai-api.el
: One of the many ai related things I want to look into some day. <https://github.com/benjamin-asdf/openai-api.el>

chatgpt emacs shell
: One of the many ai related things I want to look into some day. <https://xenodium.com/a-chatgpt-emacs-shell/>

pocket-reader.el
: Client for Pocket ([getpocket.com](https://getpocket.com)) that allows you to manage your reading list (add, remove, delete, tag, view, favorite, etc ..) within Emacs.

orgrr
: A replica of org-roam v1 implemented using ripgrep. <https://github.com/rtrppl/orgrr>

gkroam
: Another replica of roam research implemented using ripgrep. <https://github.com/Kinneyzhang/gkroam>

denote
: Simple note taking tool using predictable and descriptive file-naming scheme. <https://github.com/protesilaos/denote>

zk
: Another simple Zettlekasten implementation for Emacs. <https://github.com/localauthor/zk>

zettledeft
: Extends Deft into a basic zettelkasten. As of 2023 the author has ceased maintenance and is moving to denote. <https://github.com/localauthor/zk>


## Look and Feel {#look-and-feel}

Typically I am a function over form kind of person, but I do use a few thing that improve the look of my Emacs for `org-mode`.

I think `org-modern` makes things look a bit nicer. With `org-modern` and `org-indent` enabled the fringe around src blocks is disabled. I used `org-modern-indent` to fix that up.

{{< figure src="org-modern-without-org-modern-indent.png" caption="<span class=\"figure-number\">Figure 12: </span>org-modern without org-modern-indent" width="100%" >}}

{{< figure src="org-modern-with-org-modern-indent.png" caption="<span class=\"figure-number\">Figure 13: </span>org-modern with org-modern-indent" width="100%" >}}

[^fn:1]: Checkout the post reflecting on my history with org-mode in 2023. <https://cmdln.org/2023/03/13/reflecting-on-my-history-with-org-mode-in-2023/>
[^fn:2]: It's so many things for me as you will hopefully understand if you read through this whole thing.
[^fn:3]: My personal journal, daily work logs, and recurring meetings.
[^fn:4]: According to the [introduction in the manual](https://www.orgroam.com/manual.html#Introduction) Org-roam is a tool for networked thought. It reproduces some of [Roam Research’](https://roamresearch.com/)s key features within Org-mode. Org-roam allows for effortless non-hierarchical note-taking: with Org-roam, notes flow naturally, making note-taking fun and easy.
[^fn:5]: Maggie Appleton has a nice post about [Daily notes as a frictionless default input for personal knowledge management systems](https://maggieappleton.com/daily-notes).
[^fn:6]: ADHD is a real thing. I am also not perfect in remembering to capture each thing but I don't need to be perfect to be effective.
[^fn:7]: If you like org-mode, you might also like CFEngine. It really is a knowledge management tool for infrastructure and it's very flexible and open ended much like the numerous ways of using org-mode, there are many different ways of using CFEngine. It's a tool that has few prescriptions.
[^fn:8]: `org-rich-yank` doesn't get enough publicity, I used it many times a day. It pastes the last copied text and automatically surrounds the snippet in blocks, marked with the major mode of where the code came from, and adds a link to the source file after the block. I recommend customizing `org-rich-yank-format-paste` and making the link to the source a comment as described in the README. <https://github.com/unhammer/org-rich-yank>
[^fn:9]: Org-transclusion lets you insert a copy of text content via a file link or ID link within an Org file. It lets you have the same content present in different buffers at the same time without copy-and-pasting it. Edit the source of the content, and you can refresh the transcluded copies to the up-to-date state. <https://github.com/nobiot/org-transclusion>
[^fn:10]: I wonder if html would work for a copy source pasting into a google doc as well or better.
[^fn:11]: (org-mime-htmlize-subtree in this case) as this is one of the few daily capture templates where I capture each day to a heading in a file for the month (it's easier for people that have access to a git repo containing these files to use for periodic reviews).
[^fn:12]: I've been told multiple times by colleagues that they search out my meeting notes to help themselves complete periodic reviews. I hate doing periodic reviews, so knowing that my effort helps others in this regard is a strong motivator.
[^fn:13]: (maybe someone can suggest how that tho step process could be consolidated)
[^fn:14]: There are so many, org-mime is probably my most often used exporter followed by some flavor of Markdown (ox-hugo like this blog post, ox-gfm, ox-slack).
[^fn:15]: With mu4e I have offline mail reading and search and I run a local Postfix relay giving me offline sending capability.
[^fn:16]: [YASnippet](https://github.com/joaotavora/yasnippet) is a template system for Emacs. It allows you to type an abbreviation and automatically expand it into function templates. The snippet syntax is inspired from [TextMate'](https://macromates.com/manual/en/snippets)s syntax, you can even import most TextMate templates to YASnippet.
[^fn:17]: ox-jira exports to Jira wiki markup. It's very nice to author fairly pretty comments with so little effort. <https://github.com/stig/ox-jira.el>
[^fn:18]: Magit is an amazing front end for git. <https://magit.vc/>
[^fn:19]: Forge provides git forge integration (pull requests, issues, etc ..) for GitLab, GitHub and probably others. <https://github.com/magit/forge>
[^fn:20]: Org source for the Org-mode all the thingz! presentation is available [here](https://github.com/nickanderson/Org-mode-all-the-thingz/blob/master/presentation.org).
[^fn:21]: The org-mode documentation has a nice article about making diagrames with PlanUML. <https://orgmode.org/worg/org-contrib/babel/languages/ob-doc-plantuml.html>
[^fn:22]: Mermaid is a JavaScript based diagramming and charting tool that renders Markdown-inspired text definitions and you can use [ob-mermaid](https://github.com/arnm/ob-mermaid) to generate them from within org-mode.
[^fn:23]: Here is my post on Matson showing the elisp for using `org-roam-db-query` to set agenda files for a custom agenda command <https://fosstodon.org/@nickanderson/109979927683467557>
[^fn:24]: Darly Wakatara has a nice post about how his workflow has evolved  <https://daryl.wakatara.com/emacs-gtd-flow-evolved/>. I noted that his contact management workflow is similar to mine. Sometime it would be nice to figure out how this could be leveraged for address completion in `mu4e`. There is [org-contacts](https://orgmode.org/worg/org-contrib/org-contacts.html) but it's not clear to me if I can use it with a file per person strategy.
[^fn:25]: Will Vaughn makes a claim that "At any time, I can go to the Org-roam page for my CEO (or anyone else) to see the details of any conversation or meeting I have had with him, ever.", a claim I aspire to. <https://willvaughn.org/articles/vp-of-emacs-a-personal-wiki-in-plain-text/>
[^fn:26]: `org-download` makes it easy to insert images into a document, it provides functions for taking and inserting screenshots, downloading images, renaming images as well as dragging and dropping images into your document. <https://github.com/abo-abo/org-download>
[^fn:27]: Olivetti provides nice styling for writing. <https://github.com/rnkn/olivetti>
[^fn:28]: org-sticky-heading displays in the header-line the Org heading for the node that’s at the top of the window. This way, if the heading for the text at the top of the window is beyond the top of the window, you don’t forget which heading the text belongs to. The display can be customized to show just the heading, the full outline path, or the full outline path in reverse. <https://github.com/alphapapa/org-sticky-header>
[^fn:29]: ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern. It's _very_ fast and can even has some support for searching compressed files, multiline search. <https://github.com/BurntSushi/ripgrep>
[^fn:30]: Deft takes inspiration from Notational Velocity. I still think it's a neat package and something I would recommend to new org-mode users. <https://notational.net/>
[^fn:31]: notDeft it features a Xapian database for providing fast full text search for very large volumes of notes. I haven't tried it but I haven't found myself needing something more from ripgrep for full text search much. <https://github.com/hasu/notdeft>
[^fn:32]: Lot's of good tips in the org-roam wiki user contributed tricks. My favorite so far is for showing the node hierarchy. <https://github.com/org-roam/org-roam/wiki/User-contributed-Tricks#showing-node-hierarchy>
[^fn:33]: I have an `Orgzly` profile with an _event_ for `Display On` that triggers a `Sync Orgzly` _task_ which is an _Action_ `com.orgzly.intent.action.SYNC_START`  for _Package_ `com.orgzly` _Class_ `com.orgzly.android.sync.SyncService` _Target_ `Service`.
[^fn:34]: I am super slow working towards this, so if you want to offer up some elisp for me to use I would be most grateful.
[^fn:35]: org-ai is one of the LLM packages that I experimented with for a short time prior to July 2023 <https://github.com/rksm/org-ai>
[^fn:36]: chatgpt-shell has been my package of choice for interacting with large language models from July 5th 2023 <https://github.com/xenodium/chatgpt-shell>
[^fn:37]: Claude 2 is yet another large language model. <https://www.anthropic.com/index/claude-2> It beat ChatGPT 4 in some tests as of July 2023. <https://decrypt.co/148147/anthropic-claude-2-ai-chatbot-comparison-openai-chatgpt-google-bard>
[^fn:38]: `llm` is a CLI utility and Python library for integrating with Large Language Models, including OpenAI, PaLM and even local models on your own machine. <https://llm.datasette.io/en/stable/>
[^fn:39]: Khoj is a desktop application to search and chat with your notes, documents and images. It is an offline-first, open source AI personal assistant accessible from your Emacs, Obsidian or Web browser. It works with jpeg, markdown, notion org-mode, pdf files and github repositories. <https://khoj.dev/>
[^fn:40]: `gptel` :: A light llm client. Provides an unobtrusive way to send text to various LLMs from anywhere in Emacs. <https://github.com/karthink/gptel>