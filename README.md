# Git Commit Helper
Git Commit Helper helps programmer commit into git with minimum typing. It automate all the work need to be done for commiting.

# Features
1.  No need to type command repeatedly like git commit <file name> -m "msg". Just type msg and file will be commit automatically.
2. Captures modified, renamed, new and deleted file automatically for commit.
3. Let user commit files one by one without any hastle of copy and pasting file path.
4. Shows git diff output for each file before commiting.
5. Let user skip some file from commiting
6. Provide commit short cut that let you commit with typing of one character.


# Usase
1. Clone this repository.(__git clone git@github.com:maknahar/gitCommitHelper.git__)
2. Change mode of file commit.py (__chmod 777 commit.py__)
3. copy commit.py to PATH. (__cp commit.py /usr/local/bin/__)
4. run commit.py from any git repository to start commiting.


#Example:
```
$commit.py 

modified:   README.md

diff --git a/README.md b/README.md
index 5e612de..54247dd 100644
--- a/README.md
+++ b/README.md
@@ -49,7 +49,6 @@ index 1403ec0..f8ed92f 100644
  
  
  #Example:
- Sample change
 -$ git.py
 +$ commit.py
  

Commit Shortcuts
 a: Added new File <file name>
 b: Bug Fix
 c: Build Issue
 d: Deleted file <file name>
 i: ignore this file from commit
 p: Performance Improvement
 q: same as last file
 r: Renamed file <file name>
 t: Added test case
Enter Commit Title: changed Readme 

Enter Commit Description(Optional):
[master 59afe9b] changed Readme
 1 file changed, 1 deletion(-)

☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺
Finished Committing all new and modified Files.
☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 

Git Status Now:

On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean


Enter Y to push to remote: y

Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 615 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To git@github.com:maknahar/gitCommitHelper.git
   59afe9b..1ac3501  master -> master

```
