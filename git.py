#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
push = False
last_commit_title = ""
last_commit_desc = ""
description=""

while True:
    new_msg=True
    line = p.stdout.readline()

    #sys.stdout.write(line)
    sys.stdout.flush()
    if 'modified:' in line:
        mfile= line.split("modified:   ",1)[1].strip("\n")
        print "\nFILE NAME:",mfile
        print "\n\nCHANGES: \n"
        os.system("git diff "+mfile)

        commit_msg = raw_input("\nCommit Title\n a: Added new feature\n b: Bug Fix\n c: Build Issue\n d: Debuging\n i: ignore this file\n p: Performance Improvement\n q: same as last file\n r: Reorganized the code\n t: Added test case\nEnter Commit Title: ")

        if commit_msg!="i":
            push = True
            if commit_msg=="a":
                commit_msg="Added new feature"
            if commit_msg=="b":
                commit_msg="Bug Fix"
            if commit_msg=="c":
                commit_msg="Build Issue"
            if commit_msg=="d":
                commit_msg="Debuging"
            if commit_msg=="p":
                commit_msg="Performance Improvement"
            if commit_msg=="q":
                commit_msg=last_commit_title
                description=last_commit_desc
                new_msg=False
            if commit_msg=="r":
                commit_msg="Refactoring the code"
            if commit_msg=="t":
                commit_msg="Added test case"

            if new_msg:
                description = raw_input("\nEnter Commit Description(Optional):")
                last_commit_title=commit_msg
                last_commit_desc=description

            if description == "":
                os.system("git commit "+mfile+ " -m \""+commit_msg+"\"")
            else:
                os.system("git commit "+mfile+ " -m \""+commit_msg+"\""+ " -m \""+description+"\"")


    if 'new file:' in line:
        mfile= line.split("new file:   ",1)[1].strip("\n")
        os.system("git diff "+mfile)
        print "\nFILE NAME:",mfile
        print "\nCHANGES: New File\n"
        os.system("git diff "+mfile)
        commit_msg = raw_input("\nCommit Title\n a: Added new feature\n b: Bug Fix\n c: Build Issue\n d: Debuging\n i: ignore this file\n p: Performance Improvement\n q: same as last file\n r: Reorganized the code\n t: Added test case\nEnter Commit Title: ")

        if commit_msg!="i":
            push = True
            if commit_msg=="a":
                commit_msg="Added new feature"
            if commit_msg=="b":
                commit_msg="Bug Fix"
            if commit_msg=="c":
                commit_msg="Build Issue"
            if commit_msg=="d":
                commit_msg="Debuging"
            if commit_msg=="p":
                commit_msg="Performance Improvement"
            if commit_msg=="q":
                commit_msg=last_commit_title
                description=last_commit_desc
                new_msg=False
            if commit_msg=="r":
                commit_msg="Rorganized the code"
            if commit_msg=="t":
                commit_msg="Added test case"


            if new_msg:
                description = raw_input("\nEnter Commit Description(Optional):")
                last_commit_title=commit_msg
                last_commit_desc=description

            if description == "":
                os.system("git commit "+mfile+ " -m \""+commit_msg+"\"")
            else:
                os.system("git commit "+mfile+ " -m \""+commit_msg+"\""+ " -m \""+description+"\"")


    if line == '':
        break


print bcolors.OKGREEN+"\n☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺"+bcolors.ENDC
print bcolors.OKBLUE+ "Finished Committing all new and modified Files."+bcolors.ENDC
print bcolors.OKGREEN+"☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ \n"+bcolors.ENDC
print bcolors.BOLD+"Git Status Now:\n"+bcolors.ENDC
os.system("git status")

if push==True:
    confirm = raw_input('\n\nDo you want to Push to remote?(Y/N)')
    if confirm=='Y' or confirm=='y':
        os.system("git push")

p.kill()
