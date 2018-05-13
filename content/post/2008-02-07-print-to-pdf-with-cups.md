---
title: Print to PDF with cups.
author: Nick Anderson
type: post
date: 2008-02-08T03:25:06+00:00
url: /2008/02/07/print-to-pdf-with-cups/
categories:
  - Posts
tags:
  - cups
  - pdf
  - printing

---
Printing is a pain. I hate printers, I hate paper, but I also hate a bagillion book marks to places and things that may change over time. Its handy to have PDFs around as they are easily searchable, they preserve original layout and they print correctly when you want to print something. So for most of my printing I am printing to PDF and if I need a paper copy later I can always print out that PDF. True many applications can print or export to pdf currently. However using cups-pdf allows you to print to pdf anywhere you can print. Its great when combined with RDP too. For example at one point a <a href="http://jgarrett.org" mce_href="http://jgarrett.org">freind</a> of mine had to use GreatPlains for parts and order accounting in a production enviornment. GreatPlains allows you to print to screen in only some windows. However with cups-pdf he could print any screen he wished to pdf and view it on his screen.
   
<!--more-->


   
Setting up pdf printing with cups is very easy. Im going to show you how to set this up manually. That is not using kde or gnome or the cups admin interface to do so because this is a more portable solution.

First you need to instal cups-pdf. Im using debian now so for me its apt-get install cups-pdf, but yum install or emerge or cast or whatever your distros package manager is should be able to do it. If all else fails find the source http://www.cups-pdf.de/.

`Printing is a pain. I hate printers, I hate paper, but I also hate a bagillion book marks to places and things that may change over time. Its handy to have PDFs around as they are easily searchable, they preserve original layout and they print correctly when you want to print something. So for most of my printing I am printing to PDF and if I need a paper copy later I can always print out that PDF. True many applications can print or export to pdf currently. However using cups-pdf allows you to print to pdf anywhere you can print. Its great when combined with RDP too. For example at one point a <a href="http://jgarrett.org" mce_href="http://jgarrett.org">freind</a> of mine had to use GreatPlains for parts and order accounting in a production enviornment. GreatPlains allows you to print to screen in only some windows. However with cups-pdf he could print any screen he wished to pdf and view it on his screen.
   
<!--more-->


   
Setting up pdf printing with cups is very easy. Im going to show you how to set this up manually. That is not using kde or gnome or the cups admin interface to do so because this is a more portable solution.

First you need to instal cups-pdf. Im using debian now so for me its apt-get install cups-pdf, but yum install or emerge or cast or whatever your distros package manager is should be able to do it. If all else fails find the source http://www.cups-pdf.de/.

` 
   
Is the config file for it. There you set the output directory for your PDFs by default it is $HOME/PDF so if thats fine with you do `mkdir $HOME/PDF`.

In ``Printing is a pain. I hate printers, I hate paper, but I also hate a bagillion book marks to places and things that may change over time. Its handy to have PDFs around as they are easily searchable, they preserve original layout and they print correctly when you want to print something. So for most of my printing I am printing to PDF and if I need a paper copy later I can always print out that PDF. True many applications can print or export to pdf currently. However using cups-pdf allows you to print to pdf anywhere you can print. Its great when combined with RDP too. For example at one point a <a href="http://jgarrett.org" mce_href="http://jgarrett.org">freind</a> of mine had to use GreatPlains for parts and order accounting in a production enviornment. GreatPlains allows you to print to screen in only some windows. However with cups-pdf he could print any screen he wished to pdf and view it on his screen.
   
<!--more-->


   
Setting up pdf printing with cups is very easy. Im going to show you how to set this up manually. That is not using kde or gnome or the cups admin interface to do so because this is a more portable solution.

First you need to instal cups-pdf. Im using debian now so for me its apt-get install cups-pdf, but yum install or emerge or cast or whatever your distros package manager is should be able to do it. If all else fails find the source http://www.cups-pdf.de/.

`Printing is a pain. I hate printers, I hate paper, but I also hate a bagillion book marks to places and things that may change over time. Its handy to have PDFs around as they are easily searchable, they preserve original layout and they print correctly when you want to print something. So for most of my printing I am printing to PDF and if I need a paper copy later I can always print out that PDF. True many applications can print or export to pdf currently. However using cups-pdf allows you to print to pdf anywhere you can print. Its great when combined with RDP too. For example at one point a <a href="http://jgarrett.org" mce_href="http://jgarrett.org">freind</a> of mine had to use GreatPlains for parts and order accounting in a production enviornment. GreatPlains allows you to print to screen in only some windows. However with cups-pdf he could print any screen he wished to pdf and view it on his screen.
   
<!--more-->


   
Setting up pdf printing with cups is very easy. Im going to show you how to set this up manually. That is not using kde or gnome or the cups admin interface to do so because this is a more portable solution.

First you need to instal cups-pdf. Im using debian now so for me its apt-get install cups-pdf, but yum install or emerge or cast or whatever your distros package manager is should be able to do it. If all else fails find the source http://www.cups-pdf.de/.

` 
   
Is the config file for it. There you set the output directory for your PDFs by default it is $HOME/PDF so if thats fine with you do `mkdir $HOME/PDF`.

In`` you should add the following.
   
`<Printer PDF><br />
 Info GENERIC PostScript Printer<br />
 Location local<br />
 DeviceURI cups-pdf:/<br />
 State Idle<br />
 StateTime 1185029102<br />
 Accepting Yes<br />
 Shared Yes<br />
 JobSheets none none<br />
 QuotaPeriod 0<br />
 PageLimit 0<br />
 KLimit 0<br />
 OpPolicy default<br />
 ErrorPolicy stop-printer<br />
 </Printer>`