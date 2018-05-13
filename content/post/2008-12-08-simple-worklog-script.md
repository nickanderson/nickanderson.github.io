---
title: Simple worklog script
author: Nick Anderson
type: post
date: 2008-12-08T18:20:09+00:00
url: /2008/12/08/simple-worklog-script/
aktt_notify_twitter:
  - no
categories:
  - Posts
tags:
  - utility
  - worklog

---
I have a pretty good memory when it comes to juggling multiple tasks but I am (and have been for some time) trying to break my self of using my brain to store everything. One area a worklog benefits is when you want to look back over time and see what your were working on several months ago (this can be helpful for reviews). At any rate there are many tools to do similar things. At any rate I wrote a simple tool to try and help with this. Feel free to take it modify it or comment on the horrible code.<!--more-->

<pre class="brush: bash; title: ; notranslate" title="">#!/usr/bin/env python
# Author Nick Anderson &lt;nick#anders0n.net&gt;
# Simple worklog to log entries and show entries for a 
# matched string.
# Examples:
# worklog this is an entry
# worklog
# Prompted to type an entry
# worklog --show 2008 Dec
# worklog --show 2008 December 08
# Show todays entries with just --show
# worklog --show 

import sys, re, os
from optparse import OptionParser
from time import localtime, strftime

worklogfile = 'worklog.log'
homedir = os.path.expanduser("~") + '/'
worklog = homedir + worklogfile

def displayLog(inputstring):
    """
    Display all log entries for dates matching string.
    If no date string given, default to today.
    """
    if len(args) == 0:
        date = today
    else:
        date = " ".join(args)

    file = open(worklog, 'r')
    for line in file.readlines():
        if re.match('\t', line):
            if print_entry:
                print line.rstrip()
        elif re.match(date, line):
            print_entry = True
            print line.rstrip()
        else:
            print_entry = False
    file.close

def writeLog(inputstring):
    """
    Write a log entry for the current date

    inputstring - arguments passed to script
    """
    entries_today = False
    file = open(worklog, "ra")
    for line in file.readlines():
        if line.rstrip('\n') == today:
            entries_today = True
            file.close()

    file = open(worklog, "a")
    if not entries_today:
        file.write(today + '\n')

    if len(args) == 0:
        print "Log Entry:"
        entry = '\t' + sys.stdin.readline()
    else:
        entry = '\t' + " ".join(inputstring) + '\n'
    file.write(entry)
    file.close()       

if __name__ == '__main__':
    today = strftime("%Y %B %d %A", localtime())
    parser = OptionParser()
    parser.add_option("-s", "--show", dest="show", action="store_true", 
                      help="Show entries for date")
    (options, args) = parser.parse_args()

    if options.show:
        displayLog(args)
    else:
        try:
            writeLog(args)
        except KeyboardInterrupt:
            sys.exit()

</pre>

Example Usage:

<pre class="brush: bash; title: ; notranslate" title="">worklog I did something

worklog --show
2008 December 08 Monday
	I did something
</pre>