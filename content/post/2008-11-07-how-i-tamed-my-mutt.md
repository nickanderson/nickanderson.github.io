---
title: How I tamed my mutt
author: Nick Anderson
type: post
date: 2008-11-08T04:09:19+00:00
url: /2008/11/07/how-i-tamed-my-mutt/
aktt_tweeted:
  - 1
categories:
  - Posts
tags:
  - email
  - imap
  - mutt
  - profiles
  - screen

---
As you by now well know I try to mostly live at the console (well multiple x consoles). Mutt is my mail client of choice. I&#8217;ve tried Thunderbird, Kmail, Evolution, Sylpheed, and pine. For whatever reason I feel most comfortable with mutt. I also use IMAP for both my personal and work accounts. Mutt was originally designed to deal with local mail and while it does a very good job with IMAP I don&#8217;t like how it handles multiple accounts.
  
<!--more-->


  
In the past I have tried to make mutt &#8220;context&#8221; aware by setting up key bindings to source different account configs. While it worked for the most part, it stumbles on the folder setting. After changing folders on one account setting the folder when sourcing another account profile never seemed to work quite right.

I also tried and failed miserably to get account-hook working. I must admit I did not try very hard as I quickly realized I would get confused as to which mailbox folder was associated with which account as I have overlapping folder names.

Offlineimap is another solution that I have tried in the past. First, I don&#8217;t want to port gigs of mail around on my laptop. Second, but less of a concern was how offlineimap synchronizes mail. My mail is important, and I don&#8217;t want to accidentally wack my mailbox if something screwy happened locally.

Eventually I came to the conclusion that the best solution for me would be to use screen. I wrote a short screenrc that launched mutt with a config for my personal mail and a config for my work mail. Each of those mutt configs source a global config first. Since they are entirely seperate instances I dont have to worry about having extra settings in one or the other to clear out unused options like I did with my profile context setup. And this one actually works since there is no issue switching between folders on accounts.

After I had my screenrc ready I wrote a short bash wrapper to launch the screen session. This script (smutt) checks to see if I already have a launched screen with the name mutt and attaches to it if available. If I don&#8217;t already have a screen session named mutt then it creates a new screen.

I would love to get some feedback on what people think of this setup or how you deal with multiple imap accounts in mutt and why you like it that way. I must admit I am missing at least one thing that I use infrequently (search). Currently I just use mutt limit and / to find an email in my archives. It would be nice to have something like mairix that works over IMAP so if you know of something or have a clever solution let me know.

Here are my mutt configs so you can try out something similar.

Here is smutt my mutt wrapper.

<pre class="brush: bash; title: ; notranslate" title="">#!/bin/bash
# Nick Anderson
# http://www.cmdln.org
# mutt wrapper
# Check for previous mutt session and attach, if not found launch a new one

previousSession=$(screen -list | awk '/\.mutt/ {print $1}')
if [ "$previousSession" == "" ]; then
	screen -S mutt -c ~/.mutt/mutt_screen
else
	screen -dr $previousSession
fi
</pre>

And here is my mutt_screen config

<pre class="brush: bash; title: ; notranslate" title=""># Nick Anderson
# http://www.cmdln.org
# mutt screen setup
# Launch mutt for each account with its own profile specific config

hardstatus alwayslastline
hardstatus string '%{= kG}[email][%= %{= kw}%?%-Lw%?%{r}(%{W}%n*%f%t%?(%u)%?%{r})%{w}%?%+Lw%?%?%= %{g}][%{B}%d/%m %{G}%C%A]'
termcapinfo xterm|xterms|xs|rxvt ti@:te@

activity "activity: window ~%"  # Message when activity occurs in a window
vbell_msg "bell: window ~%"     # Message for visual bell
vbellwait 2                     # Seconds to pause the screen for visual bell

screen -t Personal mutt -F ~/.mutt/profile.d/personal/config
screen -t Work mutt -F ~/.mutt/profile.d/work/config
</pre>

Here is my ~/.mutt/common (common mutt config)

<pre class="brush: bash; title: ; notranslate" title=""># Common Mutt Config
# This file is sourced by account specific configs

set certificate_file=~/.mutt/mutt.crt		# Certificate Cache

# Header settings
ignore *				# Don't display all headers
unignore From To Cc Subject Date Organization X-Mailer User-Agent
hdr_order From: Date: To: Cc: Subject:

# Set vim as the editor and use autoformat script to strip out nested replies
set editor="$HOME/.mutt/bin/autotrim %s; /usr/bin/vim -c 'set tw=70 et' %s"

# Other Settings
set markers=no					# Fix multiline url wrapping to not break in gnome terminal
set smart_wrap					# dont wrap mid word
set pager_context=5				# Retain 5 lines of previous page when scrolling.
set delete=yes					# Automatically delete messages marked for deletion on exit
set ssl_starttls=yes				# Start TLS if available on server
auto_view text/html				# autoview html
set sort=threads				# Sort messages as threads
set sort_aux=last-date-received			# Then sort by date
set strict_threads  				# Don't thread messages by subject
set fast_reply=yes				# Skip prompt for subject and recipients when replying
set beep_new=yes				# Beep when new messages arrive in mailbox
set beep=no					# Don't beep on errors

# Prefer Plain text to html, html to word etc ...
alternative_order text/plain text/html application/vnd.msword application/msword

# Simple modification to index format to display year in date column
set index_format="%4C %Z %[!%b %d %Y] %-17.17F (%3l) %s" 

# Printing
set print=yes					# Don't ask before printing
set print_command="muttprint"			# Use muttprint for pretty printing
set print_split					# Split each msg selected for printing



# GPG Common Settings
set pgp_good_sign="^gpg: Good signature from"
set pgp_decode_command="gpg %?p?--passphrase-fd 0? --no-verbose --batch --output - %f"
set pgp_verify_command="gpg --no-verbose --batch --output - --verify %s %f"
set pgp_decrypt_command="gpg --passphrase-fd 0 --no-verbose --batch --output - %f"
set pgp_sign_command="gpg --no-verbose --batch --output - --passphrase-fd 0 --armor --detach-sign --textmode %?a?-u % a? %f"
set pgp_clearsign_command="gpg --no-verbose --batch --output - --passphrase-fd 0 --armor --textmode --clearsign %?a?-u %a? %f"
set pgp_import_command="gpg --no-verbose --import -v %f"
set pgp_export_command="gpg --no-verbose --export --armor %r"
set pgp_verify_key_command="gpg --no-verbose --batch --fingerprint --check-sigs %r"
set pgp_list_pubring_command="gpg --no-verbose --batch --with-colons --list-keys %r"
set pgp_list_secring_command="gpg --no-verbose --batch --with-colons --list-secret-keys %r"
set pgp_encrypt_only_command="pgpewrap gpg --batch --quiet --no-verbose --output - --encrypt --textmode --armor --always-trust -- -r %r -- %f"
set pgp_encrypt_sign_command="pgpewrap gpg --passphrase-fd 0 --batch --quiet --no-verbose --textmode --output - --encrypt --sign %?a?-u %a? --armor --always-trust -- -r %r -- %f"
</pre>

I use an autoformat script to strip out nested quotes. (I just realized I never bothered to modify it at all as it still has greeting matches for the authors name)
  
~/.mutt/bin/autotrim

<pre class="brush: bash; title: ; notranslate" title="">#!/usr/bin/perl
#
# "Beautify" quoted message and make it "ready-to-reply".
#
# Michael Velten

use strict;

# Possible reply greetings (regexes) (note that '&gt; ' will be prefixed)
my @greetings = (
	'Hello,',
	'Hello Michael,',
);

# Possible reply "greetouts" (regexes) (note that '&gt; ' will be prefixed)
my @greetouts = (
	'Mit freundlichen Gr.*en',
	'Viele Gr.*e',
	'Regards',
);

# Possible reply leadins (regexes) (note that '&gt; ' will be prefixed)
my @leadins = (
	'.*wrote:',
	'Michael Velten schrieb.*',
);

my $saw_greeting = 0;
my $saw_leadin = 0;
my $saw_greetout = 0;
my $saw_signature = 0;
my $prev_inds = 0;

my (@mail, @purged_mail);

my $msg = shift;
die "Usage: $0 MAIL" unless $msg;
open(MAIL, "+&lt;$msg") or die "$0: Can't open $msg: $!";
push(@mail, $_) while &lt;MAIL&gt;;   # Read whole mail

# Process whole mail
LINE:
foreach my $line (@mail) {

	# If _my_ signature appears don't mess with it but just include
	# the rest of the message (i.e. the signature) unmodified
	# (hack)
	if ($line =~ /^-- $/ || $saw_signature) {
		$saw_signature = 1;
		push(@purged_mail, $line);
		next LINE;
	}

	# Treat non-quoted lines as is
	if ($line !~ /^&gt;/) {
		push(@purged_mail, $line);
		next LINE;
	}

	# Remove empty quoted lines
	next LINE if $line =~ /^&gt;\s*$/;

	# Remove quoted greeting
	unless ($saw_greeting) {
		foreach my $greeting (@greetings) {
			if ($line =~ /^&gt; $greeting$/) {
				$saw_greeting = 1;
				next LINE;
			}
		}
	}

	# Remove quoted "greetout"
	unless ($saw_greetout) {
		foreach my $greetout (@greetouts) {
			if ($line =~ /^&gt; $greetout$/) {
				$saw_greetout = 1;
				next LINE;
			}
		}
	}

	# Remove quoted reply leadin
	# (check more than once because there might
	# be some double or more quoted lines)
	#unless ($saw_leadin) {
	foreach my $leadin (@leadins) {
		if ($line =~ /^&gt;+ $leadin$/) {
			$saw_leadin = 1;
			next LINE;
		}
	}

	# Remove line if &gt;= 3rd indentation level,
	# otherwise tighten "&gt; &gt; " to "&gt;&gt; "
	my ($pref, $suff) = $line =~ /^([&gt; ]+)(.*)$/;
	my $inds = $pref =~ tr/&gt;//;
	next LINE if $inds &gt;= 2;
	$pref =~ s/(&gt; (?!$))/&gt;/g;
	$line = $pref . $suff . "\n";

	# Insert 3 lines between 1st and &gt;1st level quoting
	$line = "\n" x 3 . $line if $prev_inds == 1 &amp;&amp; $inds &gt; 1;

	# Save purged line
	push(@purged_mail, $line);

	# Store indendation level for next iteration
	$prev_inds = $inds;
}

# Overwrite original mail with purged mail
truncate(MAIL, 0);
seek(MAIL, 0, 0);
print MAIL @purged_mail;
close(MAIL);
</pre>

And here is an example of one of my profiles.

<pre class="brush: bash; title: ; notranslate" title=""># Mutt Configuration
source ~/.mutt/common

set realname="Nick Anderson" 			# Name
set from=redacted@domain.com			# Email Address
set envelope_from=yes				# Use from value with sendmail -f

# Signature
set signature=~/.mutt/profile.d/personal/sig

set reverse_name				# when replying use To: as From: address if matches alternates
alternates "alternate1@domain.com|alternate2@domain.com"


# Imap Configuration
set imap_user="redacted"		# Imap username
set imap_pass="redacted"			# Imap password

set imap_idle=no				# Attempt to use IMAP IDLE extension to check for new mail on current mailbox
						# Does not always work, disable with some imap servers

# Imap Folders
# +FolderName is relative to base folder
set folder=imaps://mail.cmdln.org/		# Set base folder
set spoolfile=+Inbox				# Set inbox
set mbox=+Archive				# Set archive folder (mail goes here by default after being read)
set record=+Sent				# Set sent folder
set trash=+Trash				# Set trash folder (deleted mail goes here)
set postponed=+Drafts				# Set drafts folder

# Keybindings
macro index A "s+Archive&lt;enter&gt;"

# Cache things to speed up access
set header_cache=~/.mutt/profile.d/personal/cache/header_cache
set message_cachedir=~/.mutt/profile.d/personal/cache/body_cache

# Sendmail settings (msmtp)
set sendmail="/usr/bin/msmtp --tls-certcheck=off --file=/home/cmdln/.mutt/profile.d/msmtp.config"

# GPG Key &amp; Common Settings
set pgp_sign_as=8BE09DE6
# my_hdr X-PGP-Key: url				# URL to public gpg key
set pgp_autosign=yes				# Automatically sign all outgoing messages
set pgp_timeout=1800				# Time in seconds to cache key passphrase
set pgp_replyencrypt=yes			# Automatically encrypt replies to encrypted messages
</pre>