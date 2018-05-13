---
title: Gentoo on Software RAID1
author: Nick Anderson
type: post
date: 2006-09-04T14:10:32+00:00
url: /2006/09/04/gentoo-on-software-raid1/
categories:
  - Posts
tags:
  - gentoo
  - raid

---
I am in the process of setting up one of my new servers. Yes my old dual pIII machines are going to retire. They are going to live in a &#8220;retirement community&#8221; :P. Any way This time around I am going to use a mirror to protect my data. I never experienced a hardware failure before but I figure better safe than sorry right? So I am going to outline the steps needed to boot from a RAID0.

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">modprobe raid1 
mknod /dev/md1 b 9 1 
mknod /dev/md2 b 9 2 
mknod /dev/md3 b 9 3</pre>

Now setup your /boot swap and / partitions on your first disk (I will assume sda). After you have created your partitions we need to make the second drive partition table match. (I assume your drives are the same size)

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">sfdisk -d /dev/sda | sfdisk /dev/sdb</pre>

Now we need to create the raids using mdadm

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">mdadm --create --verbose /dev/md1 --level=1 \ 
--raid-devices=2 /dev/sda1 /dev/sdb1 
mdadm --create --verbose /dev/md2 --level=1 \ 
--raid-devices=2 /dev/sda2 /dev/sdb2 
mdadm --create --verbose /dev/md3 --level=1 \ 
--raid-devices=2 /dev/sda3 /dev/sdb3</pre>

Or if you are lazy like me

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">for i in `seq 1 3`; do mknod /dev/md$i b 9 $i;\ 
mdadm --create /dev/md$i --level=1 --raid-devices=2\ 
/dev/sda$i /dev/sdb$i; done</pre>

Backup your raid config

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">mdadm --detail --scan &gt;&gt; /etc/mdadm.conf</pre>

You can monitor the status of your raids via /proc/mdstat

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">watch -n .1 "cat /proc/mdstat"</pre>

Once the raid is done syncing you need to create your file systems on your md devices and proceed with the normal install routine. You need to do a bit of extra work when installing grub to make sure its installed on both devices, as well as allows you extra options in case of raid failure.

<p CLASS="content">
  &nbsp;
</p>

<pre CLASS="shell">grub&gt;device (hd0) /dev/sda 
grub&gt;root (hd0,0) 
grub&gt;setup (hd0) 
grub&gt;device (hd0) /dev/sdb 
grub&gt;root (hd0,0) 
grub&gt;setup (hd0)</pre>

<fieldset>
  <legend>grub.conf</legend> 
  
  <pre>default 0 
timeout 30 
splashimage=(hd0,0)/boot/grub/splash.xpm.gz  

title=Gentoo (2.6.17-gentoo-r7) 
        root (hd0,0) 
        kernel /boot/vmlinuz-2.6.17-gentoo-r7 root=/dev/md3  

title=Gentoo (2.6.17-gentoo-r7) [mirror recovery] 
        root (hd1,0) 
        kernel /boot/vmlinuz-2.6.17-gentoo-r7 root=/dev/md3</pre>
</fieldset>

<fieldset>
   
</fieldset>

<fieldset>
   
</fieldset>

<fieldset>
   [backdated from old website]<br />
</fieldset>