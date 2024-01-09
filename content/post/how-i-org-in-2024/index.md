+++
title = "How I org in 2024"
date = 2024-01-05
tags = ["org-mode", "org-roam", "pkm"]
draft = false
author = "Nick Anderson"
+++

Org-mode is my exocortex, second brain, second mind, mind palace, pensive, and personal knowledge management system. It's very flexible and the features I use as well as how I organize my files continues to change so I collected things here to document how I do things in 2024, I did this in 2023 as well[^fn:1].

{{< figure src="OIG (5).jpeg" alt="An image depectinig the essence of the statement Org-mode is my exocortex, second brain, second mind, mind palace, pensive, and personal knowledge management system. It's very flexible. Feature the org-roam unicorn. -- Dall-e 3 via Bing chat" width="75%" >}}


## Goal {#goal}

Unrealistically or not, I want total recall, to remember everything in durable plain text. I want to have control of my data. I want to do my work and interact efficiently. I want to improve my knowledge and capabilities, and I want to be able to share with others.

On the best of days I never leave Emacs and I have a record of everything I did as well as how much time I spent on each thing.

{{< figure src="2024-01-09_10-10-32_OIG (2).jpeg" alt="An image depectinig the essence of the statement Unrealistically or not, I want total recall, to remember everything in durable plain text. I want to have control of my data. I want to do my work and interact efficiently. I want to improve my knowledge and capabilities, and I want to be able to share with others. -- Dall-e 3 via Bing chat" width="75%" >}}


## Statistics {#statistics}

As of Tuesday, January  9, 2024
 I had `57MB` of `.org` files in `~/org`. `4945` files and `1195464` lines of text, the largest single file was `1.3MB` and the longest lined file had `26370` lines.

`4775` of these files were inside Org-roam[^fn:2], the majority of them (`3608`) were "dailies"[^fn:3].

Additionally, `~/Syncthing/Orgzly` had `7.9MB` worth of `.org` files that I synced around to a few devices and the largest `.org` file was `677K` with the most lined file having `49670` lines.

{{< figure src="2024-01-08_12-16-26_org-roam-ui-with-and-without-dailies-2024-01-05.png" caption="<span class=\"figure-number\">Figure 1: </span>org-roam-ui visualization of notes as of January 5th, 2024. Left - without dailies, Right with dailies." width="75%" >}}


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

-   **Remember relationships between notes.** Many included `%a` to create a link to the node where I was when the capture was initiated with my configuration automatically creating an ID in the source node if necessary. I preferred ID links as they don't break as I move files around.

-   **Automatically organize captured content.** I capture to my work log the most, but as I identify recurring similar content I create templates to ensure like content is stored together.

-   **Track time spent.** Only my work log capture template clocks time. Work log entries might contain the details of the work I was doing, or if it's related to work being done over multiple days might link to another node where those details are stored. If I am working on a specific project where time tracking is needed I will manually clock time in the project related files. At times I feel a desire for concurrent clocking but I hadn't made any efforts to see how to implement such capability. Org-mode already provided capabilities to help avoid clocking multiple things concurrently and I hadn't convinced myself that concurrent clocking was really needed.

-   **Initialize new files.** Org-mode can create new files and the outline path to the captured node, but alone it has no capability to initialize content outside the capture target. Org-roam's capture templates have the ability to initialize the reset of the file if target file does not already exist.

-   **Setup nodes for export.** For many of my recurring meetings I like to send out my notes to my team. My capture templates initialize the mail related properties so that I can easily export and sent my note via email.


### Other tools used for capture {#other-tools-used-for-capture}

Some of the features that I used to get content into Org-mode were not part of org-capture.

I used `org-web-tools`[^fn:6] to pull web pages into org. Either as a buffer to read, or as a subtree to store. When I wanted to clip a bit of text from a web page I used `org-protocol`[^fn:7] bookmarklets to get the content into Emacs.

`org-rich-yank`[^fn:8] let me copy text and paste it with context allowing it to be syntax highlighted as well as providing a link back to the source.

I used `org-jira`[^fn:9] to pull issues from Atlassian Cloud Jira into org-mode.

[^fn:1]: How I org in 2023 <https://cmdln.org/2023/03/25/how-i-org-in-2023/>
[^fn:2]: Org-roam is a plain-text personal knowledge management system. According to the [introduction in the manual](https://www.orgroam.com/manual.html#Introduction) Org-roam is a tool for networked thought. It reproduces some of [Roam Research’](https://roamresearch.com/)s key features within Org-mode. Org-roam allows for effortless non-hierarchical note-taking: with Org-roam, notes flow naturally, making note-taking fun and easy. Really, it facilitates capturing information by extending Org-mode's existing capture system, maintains a sqlite database of nodes (headings) with IDs and other metadata and provides the ability to surface and navigate back links (which nodes link to the current node). <https://www.orgroam.com/>
[^fn:3]: Org-roam dailies are files organized by date. I use them for my journal, work log, and recurring meetings.
[^fn:4]: Maggie Appleton has a nice post about [Daily notes as a frictionless default input for personal knowledge management systems](https://maggieappleton.com/daily-notes).
[^fn:5]: I am not perfect in remembering to capture each thing but I don't need to be perfect to be effective.
[^fn:6]: `org-web-tools` contains library functions and commands useful for retrieving web page content and processing it into Org-mode content. <https://github.com/alphapapa/org-web-tools>
[^fn:7]: `org-protocol` intercepts calls from emacsclient to trigger custom actions without external dependencies. Only one protocol has to be configured with your external applications or the operating system, to trigger an arbitrary number of custom actions. <https://orgmode.org/worg/org-contrib/org-protocol.html>
[^fn:8]: `org-rich-yank` doesn't get enough publicity, I used it many times a day. It pastes the last copied text and automatically surrounds the snippet in blocks, marked with the major mode of where the code came from, and adds a link to the source file after the block. I recommend customizing `org-rich-yank-format-paste` and making the link to the source a comment as described in the README. <https://github.com/unhammer/org-rich-yank>
[^fn:9]: `org-jira` facilitates getting content from Jira into org-mode and managing Jira issues from org-mode. <https://github.com/ahungry/org-jira>