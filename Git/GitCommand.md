# Git Commands

[Reference]
https://try.github.io/levels/1/challenges/1![TryGit]
https://git-scm.com/docs![Git Docs]
https://git-scm.com/book/en/v2![Git Pro Books]

* *git init*
    - Initializes a Git repository.
    - .git file is created and hidden in usual.

* *git status*
    - it's healty to run git status often. Sometimes things change and you don't notice it.
    - <Status Type>
        - *'staged'* : Files are ready to be committed.
        - *'unstaged'* : Files with changes that have not been prepared to be committed.
        - *'untracked'* : Files aren't tracked by Git yet. This usually indicates a newly created file.
        - *'deleted'* : File has been deleted and is waiting to be removed from Git.

* *git add \<fileName\>*
    - makes the assigned files added to Git Version Control system.
    - *git add -A \.* : the dot stands for the current directory, so everything in and beneath it is added.  The -A ensures even files deletions are included.
    - *git reset \<filename\>* : removes a file or files from the staging area. 
    - *'Staging Area'* : A place where we can group files together before we "commit" them to Git.

* *git commit -m "Messages"* 
    - stores changes of the staged files to Git
    - *git add '\*.txt'* : With wildcards, you can add many files of the same type. Single quotations are required. When using wildcards you want to be extra careful when doing commits. Make sure to check what files and folders are staged by using 'git status' before you do the actual commit.

* *git log*
    - brows the commits that you've done so far to see what you changed.
    - *git log --summary* : brows more information for each commit. You can see where new files were added for the first time or where files were deleted. It's a good overview of what's going on in the project.

* *git remote add origin https://github.com/gdh1829/Todays_Studying.git*
    - pushes your local repo to the GitHub server. This command takes a remote name and a repository URL.
    - *git remote* : Git doesn't care what you name your remotes, but it's typical to name your main one origin.

* *git push -u origin master*
    - The push command tells Git where to put our commits when you're ready.
    - In general, the name of the remote is *origin* and the default local branch name is *master*.
    - The *-u* tells Git to remember the parameters, so that next time we can simplty run *git push* and Git will know what to do.
    - *hooks* : When you start to get the hang of git you can do some really cool things with *hooks* when you push. For example) you can upload directly to a webserver whenever you push to your master remote instead of having to upload your site with an ftp client. Refer to here, https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

* *git pull origin master*
    - checks for changes on your GitHub repository and pull down any new changes.
    - *git stash* : Sometimes when you go to pull you may have changes you don't want to commit just yet. One option you have, other than commiting is to stash the changes. Use the command *'git stash'* to stash your changes, and *'git stash apply'* to re-apply your changes after your pull.

* *git diff HEAD*
    - takes a look at what is different from your last commit.
    - *HEAD* : The HEAD is a pointer that holds your position within all your different commits. By default HEAD points to your most recent commit, so it can be used as a quick way to reference that commit without having to look up the SHA.


※Commit Etiquette: You want to try to keep related changes together in seperate commits. Using *'git diff'* gives you a good overview of changes you have made and lets you add files or directories one at a time and commit them seperately.

* *git diff --staged*
    - Another great use fr *diff* is looking at changes within files that have already been staged.

* *git reset \<fileName\>*
    - unstage a file.
    - doesn't mean the file has removed but still there and has just not staged anymore.
* *git checkout -- \<target\>*
    - Files can be changed back to how they were at the last commit.

※ What is the '--'? : why do you have to use this *'--'* thing? *git checkout* seems to work fine without it. It's simply promising the command line that there are no more options after the *'--'*. This way if you happen to have a branch named *octocat.txt*, it will still revert the file, instead of switching to the branch of the same name.

* *git branch \<new branch name\>*
    - creates a new branch.
    - Branches are what naturally happens when you want to work on multiple features at the same time. You wouldn't want to end up with a master branch which has Feature A half done and Feature B half done. Rather you'd seperate the code base into two "snapshots"(branches) and work on and commit to them seperately. As soon as one was ready, you might merge this branch back into the master branch and push it to the remote server.
    - *git branch* : browse a list of local branches.

* *git checkout \<branch\>*
    - switches your branch.
    - *git checkout -b new_branch* : checkouts and creates a branch at the same time, which is the same thing as doing *git branch new_branch* and *git checkout new_branch*.

* *git rm '\*.txt'*
    - does not only remove the actual files from disk but does also stage the removal of the files.
    - *git rm -r <folder name>* : recursively removes all folders and files from the given directory.

* *git commit -am "Delete stuff"*
    - If you happen to delete a file without using *'git rm'*, you'll find that you still have to *'git rm'* the deleted files from the working tree. You can save this step by using the *'-a'* option on *'git commit'*, which auto removes deleted files with the commit.

※ *Pull Requests* : If you're hosting your repo on GitHub, you can do something called a pull request. A pull request allows the boss of the project to look through your changes and make comments before deciding to merge in the change. It's a really great feature that is used all the time for remote workers and open-source projects. Please refer to https://help.github.com/articles/about-pull-requests/ here.

* *git merge \<branch name\>*
    - (current branch is master) merges your changes from the another branch into the master branch.
    - since you're already on the master branch, so you just need to tell Git to merge the another branch into it.

※ *Merge Conflict* : Merge Conflicts can occur when changes are made to a file at the same time. For more information, take a look at the section of the https://git-scm.com/book/en/v2![Pro Git Book] on https://git-scm.com/docs/git-merge#_how_conflicts_are_presented![how conflicts are presented].

* *git branch -d \<branch name\>*
    - deletes a branch.
    - *Force Delete* : What if you have been working on a feature branch and you decide you really don't want this feature anymore? You might decide to delete the branch since you're scrapping the idea. You'll notice that *git branch -d bad_feature* doesn't work. This is because *-d* won't let you delete something that hasn't been merged. You can either add the *--force (-f)* option or use *-D* which combines *-d -f* together into one command. 
