---
title: Use bc for command line math
author: Nick Anderson
type: post
date: 2008-02-08T03:21:15+00:00
url: /2008/02/07/use-bc-for-command-line-math/
categories:
  - Posts
tags:
  - bc
  - command line
  - math

---
BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
`BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
` 
   
You enter bc, change your base to 16 for HEX type in 255 and it spits out FF the HEX value of 255.
   
Now if you want the the binary value of 255 you only need to do the following.
   
``BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
`BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
` 
   
You enter bc, change your base to 16 for HEX type in 255 and it spits out FF the HEX value of 255.
   
Now if you want the the binary value of 255 you only need to do the following.
   
`` 
   
As you can see it converted 255 into 11111111.
   
You can use it for other things with pipes as well.
   
```BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
`BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
` 
   
You enter bc, change your base to 16 for HEX type in 255 and it spits out FF the HEX value of 255.
   
Now if you want the the binary value of 255 you only need to do the following.
   
``BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
`BC is a great math library. Its extremely flexible and can be easily used in scripts.
   
<!--more-->


   
It can also be useful for command line conversions.

Say you want the HEX equivalent of 255
   
` 
   
You enter bc, change your base to 16 for HEX type in 255 and it spits out FF the HEX value of 255.
   
Now if you want the the binary value of 255 you only need to do the following.
   
`` 
   
As you can see it converted 255 into 11111111.
   
You can use it for other things with pipes as well.
   
``` 
   
And if you want to use floating point numbers try bc -l