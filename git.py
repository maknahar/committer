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


print bcolors.OKGREEN+"\n☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺"+bcolors.ENDC
print bcolors.OKBLUE+ "Finished Committing all new and modified Files."+bcolors.ENDC
print bcolors.OKGREEN+"☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ \n"+bcolors.ENDC
print bcolors.BOLD+"Git Status Now:\n"+bcolors.ENDC
os.system("git status")

p.kill()
