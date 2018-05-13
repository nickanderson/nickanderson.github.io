---
title: Notes on Zenoss ZenPacks
author: Nick Anderson
type: post
date: 2010-05-24T20:00:20+00:00
url: /2010/05/24/notes-on-zenoss-zenpacks/
categories:
  - Posts
tags:
  - sysadmin
  - zenoss
  - zenpack

---
Recently I was building a ZenPack for [Zenoss][1]. The ZenPack included an Event Command which executed a custom script. I wanted to store the custom script in the ZenPack and I didn&#8217;t want to do anything other than have proper script dependencies in place for it to work.

<pre class="brush: bash; title: ; notranslate" title="">${here/ZenPackManager/packs/ZenPacks.community.YOURZENPACK/path}/libexec/yourscript.sh  ${dev/manageIp}

</pre>

Custom scripts can be placed in $ZENHOME/ZenPacks/ZenPacks.CompanyName.Package/Zenpacks/CompanyName/Package/lib but if you want them to be executable place them in libexec.

Thanks to [Matt Ray][2] for telling me how to properly path the Event Command and the note about scripts in libexec getting the executable bit set, the docs I found only specified the lib directory.

 [1]: http://community.zenoss.org/index.jspa
 [2]: http://community.zenoss.org/people/mray