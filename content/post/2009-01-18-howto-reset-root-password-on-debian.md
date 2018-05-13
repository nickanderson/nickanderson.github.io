---
title: Howto reset root password on Debian
author: Nick Anderson
type: post
date: 2009-01-18T21:16:05+00:00
url: /2009/01/18/howto-reset-root-password-on-debian/
aktt_notify_twitter:
  - no
aktt_tweeted:
  - 1
categories:
  - Posts

---
Ever run into a situation where passing the option single to the kernel wasn&#8217;t enough to get your root password reset? This is not Debian specific but some distros (including Debian) require that you still enter the root password when booting to single user mode. This is just a quick run through of how to reset your root password without a live cd. <!--more-->Reboot your system and at the grub prompt hit e to enter edit mode, then select the kernel line and hit e again. Now append single init=/bin/bash to the line. Hit enter to temporarily save it and hit b to boot. Shortly you will be dropped at a root prompt, now you just need to remount your root file system rw so you can update the passwd.

<pre class="brush: bash; title: ; notranslate" title="">mount -o remount,rw /

</pre>

Now you should be able to successfully run passwd and update your password.