---
title: Deep thoughts
author: Nick Anderson
type: post
date: 2013-03-09T19:23:10+00:00
url: /2013/03/09/deep-thoughts/
categories:
  - Posts

---
<pre>bundle common knowledge(status)
{
  vars:
    "software" string =&gt; "$(status)", policy =&gt; "free";

    !isUsable::
      "software" string =&gt; "usable", policy =&gt; "free";

    isUsable::
      "software" string =&gt; "reusable", policy =&gt; "free";

  classes:
    "isUsable" expression =&gt; regcmp("$(software)", "usable");
    "reUsable" expression =&gt; regcmp("$(software)", "resuable");

  reports:
      Morning|Afternoon|Evening|Night::
        "Before software can be reusable it first has to be useable.",
          comment =&gt; "Ralph Johnson";
}</pre>