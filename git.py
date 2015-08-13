#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import sys

p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
while True:
    line = p.stdout.readline()

    #sys.stdout.write(line)
    sys.stdout.flush()
    if 'modified:' in line:
        mfile= line.split("modified:   ",1)[1].strip("\n")
        print "\nFILE NAME:",mfile
        print "\n\nCHANGES: \n"
        os.system("git diff "+mfile)
        commit_msg = raw_input("\nEnter Commit Title: ")
        description = raw_input("\nEnter Commit Description(Optional):")
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
        commit_msg = raw_input("\nEnter Commit Message: ")
        description = raw_input("\nEnter Commit Description(Optional):")
        if description == "":
            os.system("git commit "+mfile+ " -m \""+commit_msg+"\"")
        else:
            os.system("git commit "+mfile+ " -m \""+commit_msg+"\""+ " -m \""+description+"\"")

    if line == '':
        break


print "\n☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ \nFinished Committing all new and modified Files.\n☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ \n\nGit Status Now:\n"
os.system("git status")

p.kill()
