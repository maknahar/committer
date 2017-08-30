# Git Commit Helper
Git Commit Helper helps programmer commit into git with minimum typing. It automate all the work need to be done for commiting.

# Features
1.  No need to type command repeatedly like git commit <file name> -m "msg". Just type msg and file will be commit automatically.
2. Captures modified, renamed, new and deleted file automatically for commit.
3. Let user commit files one by one without any hastle of copy and pasting file path.
4. Shows git diff output for each file before commiting.
5. Let user skip some file from commiting
6. Provide commit short cut that let you commit with typing of one character.


# Usage

```
  git clone git@github.com:maknahar/committer.git;
  cd committer; chmod 777 commit.py; 
  cp commit.py /usr/local/bin/
```

1. Clone this repository.
2. Change mode of file commit.py 
3. copy commit.py to PATH. 
4. run commit.py from any git repository to start committing.

#Example:
```
List Of Files Needs commiting:
modified:   README.md
Please Enter to countinue. Enter q to quit: 

modified:   README.md
diff --git a/README.md b/README.md
index 93ed08f..65d58bc 100644
--- a/README.md
+++ b/README.md
@@ -11,7 +11,7 @@ Git Commit Helper helps programmer commit into git with minimum typing. It autom
 
 
 # Usase
-1. Clone this repository.(__git clone git@github.com:maknahar/committer.git__)
+1. Clone this repository.(__git clone git@github.com:maknahar/committer.git__)

Commit Shortcuts
 a: Added new File <file name>
 d: Deleted file <file name>
 i: ignore this file from commit
 p: Performance Optimization
 q: same as last file
 r: Renamed file <file name>
Enter Commit Title: changed repo url  

Enter Commit Description(Optional):
[master 43f0662] changed repo url
 1 file changed, 26 insertions(+), 77 deletions(-)
 rewrite README.md (62%)

☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺
Finished Committing all Files.
☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 



Enter Y to push to remote: y
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 395 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: This repository moved. Please use the new location:
remote:   https://github.com/maknahar/committer.git
To git@github.com:maknahar/gitCommitHelper.git
   8225141..43f0662  master -> master

Git Status Now:
On branch master
Your branch is up-to-date with 'origin/master'.
```
