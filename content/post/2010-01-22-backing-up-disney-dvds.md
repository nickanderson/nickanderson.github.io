---
title: Backing up Disney DVDs
author: Nick Anderson
type: post
date: 2010-01-23T02:32:58+00:00
url: /2010/01/22/backing-up-disney-dvds/
syntaxhighlighter_encoded:
  - 1
openid_comments:
  - 'a:4:{i:0;s:4:"1015";i:1;s:4:"1100";i:2;s:4:"1180";i:3;s:4:"1187";}'
categories:
  - Posts
tags:
  - arccos
  - backup dvd
  - copy dvd
  - decss
  - ripguard

---
Many of you know that I had a son about 6 months ago now. What you may not know is that my wife decided to quit her job and start a home daycare so she could be at home with our son. We all know how hard kids can be on DVDs and the like, so its important to be able to back them up. I am not a fan of the encryption or the new copy protections that have been put in place (ARccOS, RipGuard). These copy protections introduce bad sectors in the DVD, and set top players are supposed to just ignore them. The problem is not all players follow the rules. I&#8217;ve got a few cheapo players that just wont play many newer titles because of this copy protection.

Now that there is a swarm of children in the house I have several motivations to backing up my DVDs.

1) I want the kids to be able to use the cheap DVD players. If something bad happens no big deal.

2) I want the kids to use copies of the original DVDs instead of the original. Again burning a new dvd is much cheaper than buying a new one.

3) My MythTV frontends can stream ISOs and thats more convenient, I never have to get up and put a DVD in the player.

So a bit of research and some trial and error I believe I have come up with a pretty easy process.

## Packages needed:

  * Gnu ddrescue
  * dvdbackup
  * libdvdcss2
  * vlc
  * mkisofs

## The process:

  1. ddrescue -n -b 2048 /dev/dvd output.iso
  2. dvdbackup -M -i output.iso -o dvd_structure
  3. mkisofs -dvd-video -o clean\_dvd.iso dvd\_structure

Step 1 copys the DVD to disk block by block but any bad sectors found zero data is filled in. At this point you are left with a DVD iso that has the copy protection removed but the encryption is still intact. Step 2 extract the contents to a directory. This second step leaves you with the structure of a dvd without the encryption. I want to preserve everything about the original DVD (except the copy protection and encryption) so I used the mirror option. This leaves me with all the features and original menus. Step 3 take the DVD structure and pack it up into a nice ISO.

## A few things to note:

I took no steps to make the DVD fit on a single layer DVD (4.something GB). If you wanted to do that you should requantize after step 2. To verify that the final ISO did indeed have the encryption removed I un-installed libdvdcss2 and attempted to play the first ISO with VLC. VLC failed to properly play the ISO with only the copy protection removed but succeeded in playing the final ISO. After testing that I reinstalled libdvdcss2.

Process tested on Disney Pixar Cars.
  
I hope you find this helpful.