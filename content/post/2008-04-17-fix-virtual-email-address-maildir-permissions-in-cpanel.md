---
title: Fix virtual email address maildir permissions in Cpanel
author: Nick Anderson
type: post
date: 2008-04-17T23:34:20+00:00
url: /2008/04/17/fix-virtual-email-address-maildir-permissions-in-cpanel/
categories:
  - Posts
tags:
  - cpanel
  - fix
  - maildir
  - permissions
  - script
  - virtual users

---
Im not a big fan of cpanel but I do manage a server that runs it. Recently some update was pushed down that caused about 50% of my users to not be able to access mail. It all boiled down to a permission issue that the cpanel scripts /scripts/mailperm did not take care of. Their scripts do not correct the permissions of the virtual user maildirs. <!--more-->

<!--adsense-->


   
From my testing the virtual users maildirs need to be UID and GID the same as the domain user account. This little shell script fixed it for me as far as I can tell. Well it mostly takes care of the issue, I had a few that the script does not handle but for the vast majority it worked.

<pre class="brush: bash; title: ; notranslate" title="">#!/bin/bash
for i in $(find /home/ -type d  -maxdepth 1 ! -name '.*' -printf &quot;%f\n&quot;);do
    local_user=$i
    echo $local_user
    domain=$(awk -F '=' '/DNS=/ {print $2}' /var/cpanel/users/$local_user)
    find /home/$local_user/mail/$domain -type d  -maxdepth 1 ! -name '.*' -printf &quot;%f\n | xargs -n 1 chown $local_user.$local_user
    
done
</pre>