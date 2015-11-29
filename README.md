# Git Commit Helper
Git Commit Helper helps programmer commit into git with minimum typing. It automate all the work need to be done for commiting.

# Features
1. Captures modified, renamed, new and deleted file automatically for commit.
2. Let user commit file one by one with hastle of copy and pasting file path.
3. Shows git diff output for each file before commiting.
4. Let user skip some file from commiting


# Usase
1. Clone this repository.
2. Change mode of file commit.py (chmod 777 commit.py)
3. copy commit.py to PATH. (cp commit.py /usr/local/bin/)
4. run commit.py from any git repository to start commiting.


#Example:
```
$ commit.py

$FILE NAME: ../../global/groupmanager/groupManager.go

CHANGES:
diff --git a/src/vembu.com/global/groupmanager/groupManager.go b/src/vembu.com/global/groupmanager/groupManager.go
index d1a8b5b..d172e52 100644
--- a/src/vembu.com/global/groupmanager/groupManager.go
+++ b/src/vembu.com/global/groupmanager/groupManager.go

@@ -350,6 +349,7 @@
	    func (g *GroupManager) DropPersistenceData(tempchunkpath string, tempDBname stri
	        if !ok {
	                return errorutil.NewError("DB Util Type assersion failed. Actual type is " + reflect.TypeOf(con).String())
	        }
	+       defer connObj.Close()
	
	        _, err = connObj.Exec("DELETE FROM temp_chunk_file_details")
	        if err != nil {

@@ -366,13 +366,13 @@
    func (g *GroupManager) DropPersistenceData(tempchunkpath string, tempDBname stri
        if !ok {
                return errorutil.NewError("DB Util Type assersion failed. Actual type is " + reflect.TypeOf(con).String())
        }
+       defer mongoDBConnectionObj.Close()

        err = mongoDBConnectionObj.DB(tempDBname).DropDatabase()
        if err != nil {
                l.Log(logutil.WARN, "Error in deleting temp mongodb:"+err.Error())
                return errorutil.WrapError(err, "Error in deleting temp mongodb")
        }
-       defer mongoDBConnectionObj.Close()

        err = os.RemoveAll(tempchunkpath)
        if err != nil {

Commit Title

 a: Added new feature
 b: Bug Fix
 c: Build Issue
 d: Debuging
 i: ignore this file
 p: Performance Improvement
 r: Reorganized the code
 s: same as last file$
Enter Commit Title: b

Enter Commit Description(Optional):Closing db after use
[MAYANK_INTEGRATION_BRANCH db6a669] Bug Fix
 1 file changed, 6 insertions(+), 6 deletions(-)

☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺
Finished Committing all new and modified Files.
☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺

Git Status Now:

On branch MAYANK_INTEGRATION_BRANCH
Your branch is ahead of 'origin/MAYANK_INTEGRATION_BRANCH' by 3 commits.
  (use "git push" to publish your local commits)
  
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	../../../cgo/
	../../../fec/
	../../../github.com/codegangsta/
	../../../github.com/somethingnew2-0/
	../restore/restoreMain/restoreMain

nothing added to commit but untracked files present (use "git add" to track)

Do you want to Push to remote?(Y/N)y

Counting objects: 88, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (21/21), 2.05 KiB | 0 bytes/s, done.
Total 21 (delta 14), reused 0 (delta 0)
To git@gitserver:vembu/vembuhive.git
   c481841..db6a669  MAYANK_INTEGRATION_BRANCH -> MAYANK_INTEGRATION_BRANCH
$
```
