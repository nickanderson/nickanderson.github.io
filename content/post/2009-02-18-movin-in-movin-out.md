---
title: Movin in movin out
author: Nick Anderson
type: post
date: 2009-02-18T20:35:10+00:00
url: /2009/02/18/movin-in-movin-out/
aktt_notify_twitter:
  - no
aktt_tweeted:
  - 1
categories:
  - Posts

---
Every time I have a new shell account I end up customizing it. Making alterations to my vimrc, screenrc or whatever. It can be a huge pain when you have lots of slightly varying configs on different machines. I wrote this little script to grab my files and create a self extracting shell script so I can easily setup my environment on multiple machines.<!--more-->The usage is pretty straightforward. Define your remote path, and the filename along with your user that has scp access. Then define the files you want to include. To create the archive just run the moveout script. Once the self extracting script is uploaded you can just download it and execute it.

Example Restore:

<pre class="brush: bash; title: ; notranslate" title="">wget example.com/movein && bash movein
</pre>

moveout script

#!/bin/bash
  
\# Nick Anderson
  
\# http://www.cmdln.org

\# This script eases &#8220;moving&#8221; into a new account.
  
\# You define files that are staple configs like your vimrc,
  
\# .bashrc, .screenrc etc &#8230; The files are added to a self
  
\# extracting shell script and uploaded via scp to a remote
  
\# server. Once the self extracting shell script is available
  
\# you can wget it and execute it. 

TMPDIR=$(mktemp -d -t moveout.XXXX)
  
PAYLOADDIR=$TMPDIR/payload
  
BUILDER=$TMPDIR/build
  
DECOMPRESSOR=$TMPDIR/decompress

\# Create directories
  
mkdir $TMPDIR/payload

function addFile() {
      
cp -R $1 $PAYLOADDIR
  
}

#################################################
  
\# Remote path (uses scp)
  
#################################################
  
export REMOTEPATHSPEC=&#8221;example.com:public_html/&#8221;
  
export REMOTEFILE=&#8221;movein&#8221;
  
export REMOTESSHUSER=&#8221;remoteuser&#8221;

#################################################
  
\# Include these files in movin #
  
#################################################
  
addFile ~/.vim
  
addFile ~/.bashrc
  
addFile ~/.bash_logout
  
addFile ~/.screenrc
  
addFile ~/.profile
  
#################################################

cd $TMPDIR

\# Generate selfextraction builder
  
cat >> $TMPDIR/build <<EOF #!/bin/bash cd payload tar cf ../payload.tar . cd .. if [ -e "payload.tar" ]; then gzip payload.tar if [ -e "payload.tar.gz" ]; then cat decompress payload.tar.gz > movein
  
else
  
echo &#8220;payload.tar.gz does not exist&#8221;
  
exit 1
  
fi
  
else
  
echo &#8220;payload.tar does not exist&#8221;
  
exit 1
  
fi

echo &#8220;movein created&#8221;
  
exit 0
  
EOF
  
chmod +x $TMPDIR/build

\# Generate decompression script
  
cat >> $TMPDIR/decompress <<EOF #!/bin/bash cd ~ ARCHIVE=\$(awk '/^\_\_ARCHIVE\_\_/ { print NR + 1; exit 0; }' \$0) # Pipe tarfile into tar tail -n+\$ARCHIVE \$0 | tar xzv -C ~ exit 0 \_\_ARCHIVE\_\_ EOF chmod +x $TMPDIR/decompress cd $TMPDIR ./build scp $TMPDIR/movein $REMOTESSHUSER@$REMOTEPATHSPEC/$REMOTEFILE rm -rf $TMPDIR [/bash] Note: Be careful to not expose any sensitive information if your put your self extracting script on a publicly available address.