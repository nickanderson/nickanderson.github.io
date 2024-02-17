+++
title = "How I org in 2024"
date = 2024-01-05
tags = ["org-mode", "org-roam", "pkm"]
draft = false
author = "Nick Anderson"
+++

Org-mode is my exocortex, second brain, second mind, mind palace, pensive, and personal knowledge management system. It's very flexible and the features I use as well as how I organize my files continues to change so I collected things here to document how I do things in 2024, I did this in 2023 as well[^fn:1].

No, my Emacs org-mode configuration is not published. However, if you have some question, just reach out.

{{< figure src="2024-02-16_18-12-05_OIG (5).jpeg" alt="An image depectinig the essence of the statement Org-mode is my exocortex, second brain, second mind, mind palace, pensive, and personal knowledge management system. It's very flexible. Feature the org-roam unicorn. -- Dall-e 3 via Bing chat" width="50%" >}}


## Goal {#goal}

Unrealistically or not, I want total recall, to remember everything in durable plain text. I want to have control of my data. I want to do my work and interact efficiently. I want to improve my knowledge and capabilities, and I want to be able to share with others.

On the best of days I never leave Emacs and I have a record of everything I did as well as how much time I spent on each thing.

{{< figure src="/home/nickanderson/org/roam/cmdln_org/attachments/how-i-org-in-2024/2024-01-09_10-10-32_OIG (2).jpeg" alt="An image depectinig the essence of the statement Unrealistically or not, I want total recall, to remember everything in durable plain text. I want to have control of my data. I want to do my work and interact efficiently. I want to improve my knowledge and capabilities, and I want to be able to share with others. -- Dall-e 3 via Bing chat" width="50%" >}}


## Statistics {#statistics}

As of Friday, February 16, 2024
 I had `58MB` of `.org` files in `~/org`. `5067` files and `1220335` lines of text, the largest single file was `1.3MB` and the longest lined file had `26370` lines.

`4897` of these files were inside Org-roam[^fn:2], the majority of them (`3688`) were "dailies"[^fn:3].

Additionally, `~/Syncthing/Orgzly` had `9.2MB` worth of `.org` files that I synced around to a few devices and the largest `.org` file was `677K` with the most lined file having `49670` lines.

{{< figure src="/home/nickanderson/org/roam/cmdln_org/attachments/how-i-org-in-2024/2024-01-08_12-16-26_org-roam-ui-with-and-without-dailies-2024-01-05.png" caption="<span class=\"figure-number\">Figure 1: </span>org-roam-ui visualization of notes as of January 5th, 2024. Left - without dailies, Right with dailies." width="75%" >}}


## System {#system}

There was no real formal system in use here. Pretty much the Nick Anderson S.H.I.T. (Stuff here 'n there) methodology.

{{< figure src="attachments/how-i-org-in-2023/nick-anderson-shit-method.png" caption="<span class=\"figure-number\">Figure 2: </span>Martti Bergström (@masi@fosstodon.org) uses the Nick Anderson SHIT meethod. <https://fosstodon.org/@masi/110266696809445948>" width="50%" >}}

I appreciated reading about various workflows and methodologies like PARA, CODE, ACCESS, Johnny Decimal, etc ... but I liked to do what works for me, and that has been an ever-changing target. I would say that my process was perhaps most closely aligned with CODE (Capture, Organize, Distill, Express).


## Capture {#capture}

Capturing was an important concept in my workflow. Fundamentally it's grabbing new content and putting it somewhere. It facilitated consistency and automated some tedium of organization. I needed capturing to be fast and not interrupt my flow.

Org-roam was my primary capture interface and I _really_ liked the daily capabilities. Each day I captured notes about everything I was working on into my work log while clocking time. This gave me a nice place to think and process what I was working on[^fn:4] as well as a place to get my bearings and see what I had been working on when I got side-tracked[^fn:5]. Having a new file each day gave me a fresh start and it helped me to avoid performance issues I had previously experienced with large (multi-megabyte) files.

I had `24` org-capture-templates,  `16` org-roam-capture-templates and `75` org-roam-dailies-capture-templates.

<div class="org-youtube"><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8A52ZXPhJFk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="YouTube Video"></iframe></div>


### Capture templates helped me {#capture-templates-helped-me}

-   **Remember relationships between notes.** Many included `%a`&nbsp;[^fn:6] to create a link to the node where I was when the capture was initiated with my configuration automatically creating an ID in the source node if necessary. I preferred ID links as they don't break as I move files around.

-   **Automatically organize captured content.** I capture to my work log the most, but as I identify recurring similar content I create templates to ensure like content is stored together.

-   **Track time spent.** Only my work log capture template clocks time. Work log entries might contain the details of the work I was doing, or if it's related to work being done over multiple days might link to another node where those details are stored. If I am working on a specific project where time tracking is needed I will manually clock time in the project related files. At times I feel a desire for concurrent clocking but I hadn't made any efforts to see how to implement such capability. Org-mode already provided capabilities to help avoid clocking multiple things concurrently and I hadn't convinced myself that concurrent clocking was really needed.

-   **Initialize new files.** Org-mode can create new files and the outline path to the captured node, but alone it has no capability to initialize content outside the capture target. Org-roam's capture templates have the ability to initialize the reset of the file if target file does not already exist.

-   **Setup nodes for export.** For many of my recurring meetings I like to send out my notes to my team. My capture templates initialize the mail related properties so that I can easily export and sent my note via email.


### Other tools used for capture {#other-tools-used-for-capture}

Some of the features that I used to get content into Org-mode were not part of org-capture.

I used `org-rich-yank`[^fn:7] often, which let me copy text and paste it with context allowing it to be syntax highlighted as well as providing a link back to the source.

{{< figure src="org-rich-yank.gif" width="100%" >}}

I occasionally used `org-web-tools`[^fn:8] to pull web pages into org. Either as a buffer to read, or as a subtree to store. When I wanted to clip a bit of text from a web page I used `org-protocol`[^fn:9] bookmarklets to get the content into Emacs.

I used `org-jira`[^fn:10] to pull issues from Atlassian Cloud Jira into org-mode.

I used `gif-screencast`&nbsp;[^fn:11] to record many of the animations found on this page.

{{< figure src="./attachments/how-i-org-in-2024/org-web-tools-read-as-org.gif" width="100%" >}}

I used `org-download`&nbsp;[^fn:12]to facilitate dragging things onto my buffer to attach them and downloading files (usually images) as attachments. It provided a screenshot tool but I didn't tend to use it.

I occasionally used some [elisp from sachachua's](https://sachachua.com/blog/2021/04/org-mode-insert-youtube-video-with-separate-captions/)&nbsp;[^fn:13]blog to download youtube videos with their transcripts.


## Retrieval {#retrieval}

I retrieved content from my org in a myriad of ways.

Frequently I would find notes by name using `org-roam-node-find`. This worked well for finding notes with a regular naming pattern, e.g. I took notes on the work I did while releasing new software versions. The capture template for that type of note created files titled `Release work for X`, so it was quick and easy to `org-roam-node-find`, type `Release work for 3.18.7`, and jump to that note. Similarly, I kept notes on individual people, those notes were titled with the persons name, so it was quick to `org-roam-node-find` and start typing the persons name to find their note.

I frequently found notes via link. `org-roam-node-insert` made it easy to simply insert a link to another note (found by name as noted above). Many of my capture templates also contain links, some to well known related notes and some using `%a`&nbsp;[^fn:6] to provide a link to the location I was when I decided to initiate the capture. That annotation link (`%a`) can result in links to unrelated things, but I had found the ability to track back and be aware of unrelated things that were happening around that time to be useful during some archaeology sessions.

Sometimes I would use `org-roam-buffer` to get a view on which notes link to my current note.

{{< figure src="./attachments/how-i-org-in-2023/2024-01-12_12-52-45_Screenshot_2024-01-12_125217.png" caption="<span class=\"figure-number\">Figure 3: </span>Screenshot showing the org-mode source for this section on the left and org-roam-buffer listing links to this section on the right" width="100%" >}}

Searching by name is not always effective, sometimes I needed to search widely and dive deep searching for specific strings. For that, most often I used `org-ripgrep-consult`.

For serendipitous stumbles, I occasionally used `org-roam-random-note` to surface some random note.

I long desired to make effective use of `org-agenda` and I had played around with using `org-roam-db-query` to identify which files contained TODO keywords to keep the files loaded by `org-agenda` to a minimum, but I had yet to really make agenda part of my routine.

`org-roam-dynamic-blocks`&nbsp;[^fn:14] stayed on my radar, but I had yet to really make it an active part of my workflow.

[^fn:1]: How I org in 2023 <https://cmdln.org/2023/03/25/how-i-org-in-2023/>
[^fn:2]: Org-roam is a plain-text personal knowledge management system. According to the [introduction in the manual](https://www.orgroam.com/manual.html#Introduction) Org-roam is a tool for networked thought. It reproduces some of [Roam Research’](https://roamresearch.com/)s key features within Org-mode. Org-roam allows for effortless non-hierarchical note-taking: with Org-roam, notes flow naturally, making note-taking fun and easy. Really, it facilitates capturing information by extending Org-mode's existing capture system, maintains a sqlite database of nodes (headings) with IDs and other metadata and provides the ability to surface and navigate back links (which nodes link to the current node). <https://www.orgroam.com/>
[^fn:3]: Org-roam dailies are files organized by date. I use them for my journal, work log, and recurring meetings.
[^fn:4]: Maggie Appleton has a nice post about [Daily notes as a frictionless default input for personal knowledge management systems](https://maggieappleton.com/daily-notes).
[^fn:5]: I am not perfect in remembering to capture each thing but I don't need to be perfect to be effective.
[^fn:6]: `%a` - Annotation, normally the link created with `org-store-link`.
[^fn:7]: `org-rich-yank` doesn't get enough publicity, I used it many times a day. It pastes the last copied text and automatically surrounds the snippet in blocks, marked with the major mode of where the code came from, and adds a link to the source file after the block. I recommend customizing `org-rich-yank-format-paste` and making the link to the source a comment as described in the README. <https://github.com/unhammer/org-rich-yank>
[^fn:8]: `org-web-tools` contains library functions and commands useful for retrieving web page content and processing it into Org-mode content. <https://github.com/alphapapa/org-web-tools>
[^fn:9]: `org-protocol` intercepts calls from emacsclient to trigger custom actions without external dependencies. Only one protocol has to be configured with your external applications or the operating system, to trigger an arbitrary number of custom actions. <https://orgmode.org/worg/org-contrib/org-protocol.html>
[^fn:10]: `org-jira` facilitates getting content from Jira into org-mode and managing Jira issues from org-mode. <https://github.com/ahungry/org-jira>
[^fn:11]: `gif-screencast` captures one frame per user action and let's me stay inside Emacs while doing so. The project can be found here: <https://gitlab.com/ambrevar/emacs-gif-screencast>
[^fn:12]: Find org-download here: <https://github.com/abo-abo/org-download>
[^fn:13]: I edited the elisp to switch from `youtube-dl` to `yt-dlp`.
[^fn:14]: `org-roam-dynamic-blocks` is not yet packaged, but you can find it here <https://github.com/chrisbarrett/nursery/blob/main/lisp/org-roam-dblocks.el>. Perhaps someday it will become part of Org-roam <https://github.com/org-roam/org-roam/issues/2251>
