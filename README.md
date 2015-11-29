# Git Commit Helper
Git Commit Helper helps programmer commit into git with minimum typing. It automate all the work need to be done for commiting.

# Features
1. Captures modified, renamed, new and deleted file automatically for commit.
2. Let user commit files one by one without any hastle of copy and pasting file path.
3. Shows git diff output for each file before commiting.
4. Let user skip some file from commiting
5. No need to type command repeatedly like git commit <file name> -m "msg". Just type msg and file will be commit automatically.


# Usase
1. Clone this repository.
2. Change mode of file commit.py (chmod 777 commit.py)
3. copy commit.py to PATH. (cp commit.py /usr/local/bin/)
4. run commit.py from any git repository to start commiting.


#Example:
```
$commit.py 
modified:   README.md
diff --git a/README.md b/README.md
index 1403ec0..f8ed92f 100644
--- a/README.md
+++ b/README.md
@@ -1,16 +1,23 @@
-# gitCommitHelper
-GitCommitHelper helps programmer commit into git with minimum typing.
+# Git Commit Helper
+Git Commit Helper helps programmer commit into git with minimum typing. It automate all the work need to be done for commiting.
+
+# Features
+1. Captures modified, renamed, new and deleted file automatically for commit.
+2. Let user commit file one by one with hastle of copy and pasting file path.
+3. Shows git diff output for each file before commiting.
+4. Let user skip some file from commiting
+
 
 # Usase
-1. chmod 777 git.py
-2. Copy git.py to PATH Location (ex - /usr/local/bin/)
-3. Go inside the project git directory.
-4. Run git.py from any git repository to commit.
+1. Clone this repository.
+2. Change mode of file commit.py (chmod 777 commit.py)
+3. copy commit.py to PATH. (cp commit.py /usr/local/bin/)
+4. run commit.py from any git repository to start commiting.
 
 
 #Example:
-$ git.py
+$ commit.py
 
 $FILE NAME: ../../global/groupmanager/groupManager.go
 

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
Enter Commit Title: changed readme

Enter Commit Description(Optional):
[master c45b011] changed readme
 1 file changed, 14 insertions(+), 7 deletions(-)

☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺
Finished Committing all new and modified Files.
☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 

Git Status Now:

On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean


Enter Y to push to remote: y
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 629 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To git@github.com:maknahar/gitCommitHelper.git
   9a1a391..c45b011  master -> master

$
```
