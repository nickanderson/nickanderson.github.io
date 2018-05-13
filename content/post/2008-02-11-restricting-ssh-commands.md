---
title: Restricting SSH commands
author: Nick Anderson
type: post
date: 2008-02-11T06:01:54+00:00
url: /2008/02/11/restricting-ssh-commands/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - authprogs
  - restrict commands
  - security
  - ssh

---
SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
```` 
  
It should be all one long line! We did turn off some additional SSH features that the key does not need access too. Go ahead and run the rsync command from your client machine.
  
`````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
```` 
  
It should be all one long line! We did turn off some additional SSH features that the key does not need access too. Go ahead and run the rsync command from your client machine.
  
````` 
  
You should get an error something like You&#8217;re not allowed to run &#8216;rsync &#8211;server &#8211;sender -logtpr . /var/backup/&#8217; Thats becasue we have yet to setup the authprogs.conf file. You can see the same information on the remote server /home/backup\_user/authprogs.log file. We just need to add our authprogs.conf so put the following on the remote server in /home/backup\_user/.ssh/authprogs.conf
  
``````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
```` 
  
It should be all one long line! We did turn off some additional SSH features that the key does not need access too. Go ahead and run the rsync command from your client machine.
  
`````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
````SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
```SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
``SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
`SSH is a powerful tool. When combined with ssh keys, it becomes easy to automate remote procedures like backups. However leaving key access wide open can be a bad idea. It is possible to use restrict ssh keys to specific commands, even coming from specific hosts. There is this nice little perl script called <a HREF="http://www.hackinglinuxexposed.com/tools/authprogs">Authprogs</a> that makes this somewhat easier. Ill show you how to use authprogs for an automated rsync over ssh.<!--more-->


  
First you need to generate your ssh key using ssh-keygen
  
` 
  
I have specified a dsa key with the comment of &#8220;Backup Key&#8221; to your .ssh directory with an empty passphrase since we are going to be using this to do something automattically.
  
Lets go ahead and copy that key to the remote server using ssh-copy-id.
  
`` 
  
Your backup_user can be whatever user will have rights to access the data you want to rsync.
  
Go ahead and ssh into the remote server using the key to test it, and while we are there lets setup authprogs. If your going to use your root user here please consider using the ssh directive &#8220;PermitRootLogin forced-commands-only&#8221; in your /etc/ssh/sshd_config
  
``` 
  
Now you should have a line in your authorized keys that ends in &#8220;Backup Key&#8221;, its the key we created and installed with ssh-copy-id. We want to add no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty,command=&#8221;/home/backup_user/bin/authprogs&#8221;. Your file should look similar to this.
  
```` 
  
It should be all one long line! We did turn off some additional SSH features that the key does not need access too. Go ahead and run the rsync command from your client machine.
  
````` 
  
You should get an error something like You&#8217;re not allowed to run &#8216;rsync &#8211;server &#8211;sender -logtpr . /var/backup/&#8217; Thats becasue we have yet to setup the authprogs.conf file. You can see the same information on the remote server /home/backup\_user/authprogs.log file. We just need to add our authprogs.conf so put the following on the remote server in /home/backup\_user/.ssh/authprogs.conf
  
`````` </code></code>