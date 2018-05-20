---
title: 'CFEngine 3 Tip: Find out what classes are being defined'
author: Nick Anderson
type: post
date: 2012-10-18T21:00:49+00:00
url: /2012/10/18/cfengine-3-tip-find-out-what-classes-are-being-defined/
categories:
  - Posts
tags:
  - allclassesreport
  - CFEngine
  - classes
  - tip

---
CFEngine defines a classes for dec[<img class="alignright size-medium wp-image-1085" title="A+ report" src="http://www.cmdln.org/images/wp-content/uploads/2012/10/produc4-300x199.jpg" alt="" width="300" height="199" srcset="http://www.cmdln.org/images/wp-content/uploads/2012/10/produc4-300x199.jpg 300w, http://www.cmdln.org/images/wp-content/uploads/2012/10/produc4.jpg 529w" sizes="(max-width: 300px) 100vw, 300px" />][1]ision making during runs. Many of these hard classes you can see by running cf-promises -v. That wont show you all the other classes that are raised during a policy run.

You could run something like this to see what classes are raised during execution.

<pre class="brush: bash; title: ; notranslate" title="">cf-agent -KIv | grep "cf3&gt;\s*+" | grep -v :</pre>

But that isn&#8217;t really a clear picture under normal operation. You can use the <a href="http://cfengine.com/manuals/cf3-reference#allclassesreport-in-agent" target="_blank">allclassesreport in body agent control </a>to write out a list of classes defined during execution in /var/cfengine/state/allclasses.txt. It can be handy to have. I was recently wanting to do something when policy was executed by cf-execd but not when executed manually. Based on all the other automatic classes defined I had a suspicion there was an automatic class for that, and I had no need to manually add a class to exec\_command in body executor control. I turned on the allclassesreport and sure enough, I found from\_cfexecd was being raised.

Of course all of this information is readily available for remote agents in the dashboard of the enterprise version. And with the <a href="http://cfengine.com/25free" target="_blank">25free program</a> to get started, you should definitely take a look.

 [1]: http://www.cmdln.org/images/wp-content/uploads/2012/10/produc4.jpg
