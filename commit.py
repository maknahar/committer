#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
q = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
push = False
last_commit_title = ""
last_commit_desc = ""
description = ""
somethingToCommit = False

print BColors.BOLD + "\nList Of Files Needs committing:" + BColors.ENDC
while True:
    line = q.stdout.readline()
    sys.stdout.flush()
    if 'modified:' in line or 'new file:' in line or 'renamed:' in line or 'deleted:' in line:
        print BColors.BOLD + BColors.OKBLUE + line.strip() + BColors.ENDC
        somethingToCommit = True

    if line == '':
        q.kill()
        if somethingToCommit is False:
            print "Nothing to commit. Quiting..."
            quit()
        confirm = raw_input("\nPlease Enter to continue.(q to quit):\t")
        if confirm.strip() == 'q' or confirm.strip() == 'Q':
            print "Quiting..."
            quit()
        break

while True:

    new_msg = True
    line = p.stdout.readline()

    # sys.stdout.write(line)
    sys.stdout.flush()

    if 'modified:' in line or 'new file:' in line or 'renamed:' in line or 'deleted:' in line:

        print BColors.BOLD + BColors.OKBLUE + line.strip() + BColors.ENDC
        mfile = ''

        if 'modified:' in line:
            mfile = line.split("modified:   ", 1)[1].strip("\n")
            os.system("git diff " + mfile)

        if 'new file:' in line:
            mfile = line.split("new file:   ", 1)[1].strip("\n")

        if 'renamed:' in line:
            mfile = line.split("renamed:   ", 1)[1].strip("\n")

        if 'deleted:' in line:
            mfile = line.split("deleted:   ", 1)[1].strip("\n")

        commit_msg = raw_input(
            "\nShortcuts\n a: Added new File <file name>\n " +
            BColors.WARNING + "c: Checkout this file" + BColors.ENDC +
            "\n d: Deleted file <file name>\n "
            "i: ignore this file from commit\n "
            "p: Performance Optimization\n "
            "q: Quit Committing\n "
            "r: Renamed file <file name>\n "
            "s: Same as last file\n"
            "Enter Commit Title: ")

        if commit_msg.strip() != "i" and commit_msg.strip() != '':

            if commit_msg.strip() == "a":
                commit_msg = "Added new File: " + mfile

            if commit_msg.strip() == "c":
                os.system("git checkout " + mfile)
                new_msg = False
                continue

            if commit_msg.strip() == "d":
                commit_msg = "Deleted File: " + mfile

            if commit_msg.strip() == "p":
                commit_msg = "Performance Optimization"

            if commit_msg.strip() == "s":
                commit_msg = last_commit_title
                description = last_commit_desc
                new_msg = False

            if commit_msg.strip() == "r":
                commit_msg = "Renamed file: " + mfile

            if commit_msg.strip() == "q":
                print "Quiting..."
                quit()

            if new_msg:
                push = True
                description = raw_input("\nEnter Commit Description(Optional):")
                last_commit_title = commit_msg.strip()
                last_commit_desc = description

            if description == "":
                os.system("git commit " + mfile + " -m \"" + commit_msg + "\"")
            else:
                os.system("git commit " + mfile + " -m \"" + commit_msg + "\"" + " -m \"" + description + "\"")

    if "orig" in line:
        print BColors.BOLD + BColors.OKBLUE + line.strip() + BColors.ENDC

    if line == '':
        break

if push is True:
    print BColors.OKGREEN + "\n☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺" + BColors.ENDC
    print BColors.OKBLUE + "Finished Committing all Files." + BColors.ENDC
    print BColors.OKGREEN + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ \n" + BColors.ENDC
    confirm = raw_input('\n\nEnter Y to push to remote: ')
    if confirm.strip() == 'Y' or confirm.strip() == 'y':
        os.system("git push")

print BColors.BOLD + "\nGit Status Now:" + BColors.ENDC
os.system("git status")

p.kill()
