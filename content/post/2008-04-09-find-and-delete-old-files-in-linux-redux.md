---
title: Find and delete old files in linux redux
author: Nick Anderson
type: post
date: 2008-04-09T15:21:09+00:00
url: /2008/04/09/find-and-delete-old-files-in-linux-redux/
categories:
  - Posts
tags:
  - cleanup
  - delete
  - faster
  - find
  - maintainance
  - xargs

---
After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
``After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
`` 
  
And lets see the creation loop with xargs since we are talking about squeezing a tad more performance out of things.
  
The standard for loop &#8230;
  
```After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
``After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
`` 
  
And lets see the creation loop with xargs since we are talking about squeezing a tad more performance out of things.
  
The standard for loop &#8230;
  
``` 
  
And the better faster xargs way
  
````After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
``After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
`` 
  
And lets see the creation loop with xargs since we are talking about squeezing a tad more performance out of things.
  
The standard for loop &#8230;
  
```After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
``After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
`After some lovely [feedback][1] from [Sotiris Tsimbonis][2] on my last post [Find and delete old files in linux][3] I have a better (faster) way to delete files.<!--more-->

<!--adsense-->


  
Spawning processes is expensive, its much better to not spawn a new process if its not needed. Just for proof I created 100 empty files in a temp directory and deleted them both ways.
  
The old way &#8230;
  
` 
  
The better faster way
  
`` 
  
And lets see the creation loop with xargs since we are talking about squeezing a tad more performance out of things.
  
The standard for loop &#8230;
  
``` 
  
And the better faster xargs way
  
````

 [1]: http://www.cmdln.org/2008/04/08/find-and-delete-old-files-in-linux/#comment-360
 [2]: http://stsimb.irc.gr/
 [3]: http://www.cmdln.org/2008/04/08/find-and-delete-old-files-in-linux