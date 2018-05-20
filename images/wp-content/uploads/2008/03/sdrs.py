#!/usr/bin/env python
# Author: Nick Anderson <nick@anders0n.net>
# Website: http://www.cmdln.org
# Description: Simple directory revisioning script, just creates revisions of directories.
#   Its a dirty ugly script, the same thing can be accomplished with other tools like rsnapshot
#   in a more efficient manor.
#
# ~/.sdrs.conf
# backup_directories=['/path/to/source/directory', 'directory_identifier', '/path/to/some/other/directory', 'some_other_identifier']
# output_directory='/path/to/output_revision/directory
# revisions=<int>
#
#
#
#

import optparse
import os
import shutil


def restore_revision(revision, backup_directories, output_directory):
    pass
    number_backups = len(backup_directories)/2
    for backup_set in range(number_backups):
        target_directory = backup_directories[backup_set * 2]
        directory_identifier = backup_directories[backup_set * 2 + 1]
        source_directory = output_directory + '/' + directory_identifier + '.' + str(revision)
        print 'target directory: ' + target_directory
        print 'source directory: ' + source_directory
        print 'Removing Unwanted Directory State: ' + target_directory
        shutil.rmtree(target_directory)
        print 'Restoring Revision: ' + source_directory + ' to ' + target_directory
        shutil.copytree(source_directory, target_directory)
        shutil.copystat(source_directory, target_directory)
    
def create_revision(revisions, backup_directories, output_directory):
    pass
    list = range(revisions)
    list.reverse()
    number_backups = len(backup_directories)/2
    
    for backup_set in range(number_backups):
        #print backup_directories[backup_set:backup_set+1]   
        for revision in list:
    #        print backup_directories
            source_directory = backup_directories[backup_set * 2]
            directory_identifier = backup_directories[backup_set * 2 + 1]
            if revision == len(list)-1:
                if os.path.exists(output_directory + '/' + directory_identifier + '.' + str(revision)):
                    if opts.verbose:
                        print "Removing last revision: " + output_directory + '/' + directory_identifier + '.' + str(revision)
                    shutil.rmtree(output_directory + '/' + directory_identifier + '.' + str(revision))
            else:
                if os.path.exists(output_directory + '/' + directory_identifier + '.' + str(revision)):
                    if opts.verbose:
                        print "Creating Backup Revision: " + output_directory + '/' + directory_identifier + '.' + str(revision+1) + " from " + output_directory + '/' + directory_identifier + '.' + str(revision)
                    shutil.copytree(output_directory + '/' + directory_identifier + '.' + str(revision), output_directory + '/' + directory_identifier + '.' + str(revision+1))
                    shutil.copystat(output_directory + '/' + directory_identifier + '.' + str(revision), output_directory + '/' + directory_identifier + '.' + str(revision+1))
                    shutil.rmtree(output_directory + '/' + directory_identifier + '.' + str(revision))
                if revision == 0:
                   if os.path.exists(source_directory):
                        if not os.path.exists(output_directory):
                            cmd = 'mkdir -p ' + output_directory
                            os.mkdir(output_directory)
                            #os.system(cmd)
                        if opts.verbose:
                            print "Creating Backup Revision: " + output_directory + '/' + directory_identifier + '.' + str(revision) + " from " + source_directory
                        shutil.copytree(source_directory, output_directory + '/' + directory_identifier + '.' + str(revision))
                        shutil.copystat(source_directory, output_directory + '/' + directory_identifier + '.' + str(revision))




def process_args():
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.1")
    parser.add_option("-d", "--directories", dest="directories", help="Directories to backup")
    parser.add_option("-o", "--output", dest="output", help="Directory to store revisoned backups")
    parser.add_option("-r", "--revisions", dest="revisions", help="Number of revisions to keep")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False)
    parser.add_option("-c", "--config", dest="config", help="Specify config file", default=os.path.expanduser('~/')+'.sdrs.conf')
    parser.add_option("-u", "--undo", dest="undo", help="Undo changes and restore revision given, defaults to revision 0")
    return parser.parse_args()
    

(opts, args) = process_args()
# get list of directories
if os.path.exists(opts.config):
    try:
        execfile(opts.config)
        config_found = True
    except:
        print "unknown error - could not read config file"
else:
    config_found = False

if opts.directories:
    backup_directories = opts.directories.split(',')
if opts.output:
    output_directory = opts.output
if opts.revisions:
    revisons = opts.revisions

try:
    revisions
except NameError:
    print "no revison specified"
try:
    backup_directories
except NameError:
    print "no directorys specified to backup"
try:
    output_directory
except NameError:
    print "no output directory specified"

if opts.undo:
    restore_revision(opts.undo, backup_directories, output_directory)
else:
    create_revision(revisions, backup_directories, output_directory)
    