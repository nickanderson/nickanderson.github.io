---
title: Reset mysql root password
author: Nick Anderson
type: post
date: 2008-02-09T15:13:03+00:00
url: /2008/02/09/reset-mysql-root-password/
aktt_notify_twitter:
  - no
openid_comments:
  - 'a:1:{i:0;i:1306;}'
categories:
  - Posts
tags:
  - mysql
  - password
  - reset
  - root

---
Have you ever forgotten the root password on one of your MySQL servers? No? Well maybe I&#8217;m not as perfect as you. This is a quick h00tow (how to) reset your MySQL root password. It does require root access on your server. If you have forgotten that password wait for another article.
  
<!--more-->


  
<!--adsense-->


  
First things first. Log in as root and stop the mysql daemon. Now lets start up the mysql daemon and skip the grant tables which store the passwords.
  
`Have you ever forgotten the root password on one of your MySQL servers? No? Well maybe I&#8217;m not as perfect as you. This is a quick h00tow (how to) reset your MySQL root password. It does require root access on your server. If you have forgotten that password wait for another article.
  
<!--more-->


  
<!--adsense-->


  
First things first. Log in as root and stop the mysql daemon. Now lets start up the mysql daemon and skip the grant tables which store the passwords.
  
` 
  
You should see mysqld start up successfully. If not, well you have bigger issues. Now you should be able to connect to mysql without a password.
  
``Have you ever forgotten the root password on one of your MySQL servers? No? Well maybe I&#8217;m not as perfect as you. This is a quick h00tow (how to) reset your MySQL root password. It does require root access on your server. If you have forgotten that password wait for another article.
  
<!--more-->


  
<!--adsense-->


  
First things first. Log in as root and stop the mysql daemon. Now lets start up the mysql daemon and skip the grant tables which store the passwords.
  
`Have you ever forgotten the root password on one of your MySQL servers? No? Well maybe I&#8217;m not as perfect as you. This is a quick h00tow (how to) reset your MySQL root password. It does require root access on your server. If you have forgotten that password wait for another article.
  
<!--more-->


  
<!--adsense-->


  
First things first. Log in as root and stop the mysql daemon. Now lets start up the mysql daemon and skip the grant tables which store the passwords.
  
` 
  
You should see mysqld start up successfully. If not, well you have bigger issues. Now you should be able to connect to mysql without a password.
  
`` 
  
Now kill your running mysqld, then restart it normally. You should be good to go. Try not to forget your password again.