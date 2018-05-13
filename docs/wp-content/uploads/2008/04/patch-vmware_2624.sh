#!/bin/bash

build_dir=$(mktemp -p $(pwd) -d)

wget http://pastebin.com/pastebin.php?dl=f58553c1f -O $build_dir/vmmon-2.6.24.patch
wget http://pastebin.com/pastebin.php?dl=f681c5c13 -O $build_dir/vmnet-2.6.24.patch

tar --extract --file /usr/lib/vmware/modules/source/vmmon.tar --directory $build_dir
cp /usr/lib/vmware/modules/source/vmmon.tar $build_dir/vmmon.tar.bak
tar --extract --file /usr/lib/vmware/modules/source/vmnet.tar --directory $build_dir
cp /usr/lib/vmware/modules/source/vmnet.tar $build_dir/vmnet.tar.bak

cd $build_dir/vmmon-only
patch -p1 < ../vmmon-2.6.24.patch
cd $build_dir

tar --create --file vmmon.tar vmmon-only

cd vmnet-only
patch -p1 < ../vmnet-2.6.24.patch
cd $build_dir
tar --create --file vmnet.tar vmnet-only

echo " You need rootly priviliges to do the following necissary actions. 
Please use sudo or wheel up to root to finish the install."

echo ============================================

echo cp vmmon.tar /usr/lib/vmware/modules/source/
echo cp vmnet.tar /usr/lib/vmware/modules/source/
echo vmware-config.pl

echo ============================================


