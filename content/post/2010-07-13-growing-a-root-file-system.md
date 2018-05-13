---
title: Growing a root file system
author: Nick Anderson
type: post
date: 2010-07-13T14:45:21+00:00
url: /2010/07/13/growing-a-root-file-system/
categories:
  - Posts
tags:
  - lvm
  - sysadmin
  - vmware
  - xen

---
IMHO one of the great benefits of virtualization is the ability to properly size your guests. Many times 512M memory and an 8G / is plenty. Increasing memory for a virtual machine is typically pretty straight forward, but there are several options when adding disk space. Mounting the space in the file system and doing something with LVM are likely the most common paths.

Depending on the situation I typically lean toward keeping my small 8G root and mounting extra storage where needed in the file system. I think its the simplest solution for most cases. I don&#8217;t like ending up with a bunch of mounts, so in the cases where storage needs are spread across the file system growing the root becomes important. You can add a new virtual disk, partition it, toss it into the Volume Group and then extend your volume and file system. There is absolutely nothing wrong with this approach but having all those virtual hard drives attached just seems a bit hap-hazard and messy. When I need more space at / I think its much cleaner to just extend the partition that is in the VG of my systemroot. Anyway here are my notes. The block devices are specific to Xen but the actions should work on other platforms and on bare metal. My default partitioning scheme is as follows, /dev/xvda 2 partitions, 100M /boot, LVM with / being comprised of the full available space. Swap is on /dev/xvdb. This allows me to keep growing xvda and extending the second partition when I need to add space.

  1. Power vm off
  2. Create snapshot incase things go horribly wrong
  3. Extend virtual drive size
  4. Power vm on
  5. Fdisk device (/dev/xvda)
  6. Delete last partition
  7. Create new partition using default values
  8. Reboot vm
  9. Resize LVM Physical Volume (pvresize /dev/xvda2)
 10. Resize Logical Volume to fill new space (lvresize -l 100%VG /dev/VolGroup00/systemroot)
 11. Resize filesystem (resize2fs /dev/VolGroup00/systemroot)
 12. Reboot for good measure
 13. Delete snapshot