---
title: Get around that pesky firewall filtering with tsocks
author: Nick Anderson
type: post
date: 2008-02-12T18:12:18+00:00
url: /2008/02/12/get-around-that-pesky-firewall-filtering-with-tsocks/
categories:
  - Posts
tags:
  - bypass
  - firewall
  - howto
  - proxy
  - screencast
  - security
  - ssh
  - tsocks
  - video

---
I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
`I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
` 
  
Now you need to edit your tsocks.conf to point it to localhost (since we are using ssh dynamic ports). Ensure the following lines in /etc/tsocks.conf
  
``I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
`I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
` 
  
Now you need to edit your tsocks.conf to point it to localhost (since we are using ssh dynamic ports). Ensure the following lines in /etc/tsocks.conf
  
`` 
  
So thats it! Easy eh? Now to surf or check email in privacy.
  
```I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
`I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
` 
  
Now you need to edit your tsocks.conf to point it to localhost (since we are using ssh dynamic ports). Ensure the following lines in /etc/tsocks.conf
  
``I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
`I generally don&#8217;t have any issues knowing someone might be snooping on a bit of my traffic. However there are times you may want your traffic to be a bit more private. For example if your boss is a raging tyrant and your looking for a new job, and you know the sky would fall if he found out you emailed or happened to be on Career Builder or for that matter had even the slightest idea of abandoning him. Yes I am recounting something from my past, hey at least its distant past :). So if you find yourself in that situation read on for how to use tsocks and ssh as a simple proxy.
  
<!--more-->


  
<!--adsense-->


  
First things first, for this to work you need to have ssh access to a machine outside your network. I like to use an account in shanghi, but really if you just ssh back to your home machine that will most likely suffice. Ok now that you can ssh out you can use ssh dynamic port forwarding via SOCKS, but you need to install tsocks before that will be useful.
  
For debian:
  
` 
  
Now you need to edit your tsocks.conf to point it to localhost (since we are using ssh dynamic ports). Ensure the following lines in /etc/tsocks.conf
  
`` 
  
So thats it! Easy eh? Now to surf or check email in privacy.
  
``` 
  
*Note: Another great use for this is when you are on the road. Many hotels block outbound port 25, which causes you to not be able to send email with your prefered mail client unless you start doing ssh port forwarding or some other trickery. And its a pita to setup multiple outbound smtp connections that you have to switch to. Anyway hope you find this useful. Here is a video of the process for your viewing pleasure.

[flash http://www.cmdln.org/videos/tsocks\_in\_5\_minutes\_or\_less.flv w=640 h=480 preview={http://www.cmdln.org/videos/tsocks\_in\_5\_minutes\_or\_less.jpg|320|240} linktext={screencast: tsocks} mode=3 caption={screencast: tsocks}]