If credentials were pushed to a remote repository like Github, the following steps can be used to removed those credentials from the commit history after they have been removed from the current commit: 

1 - First, the pushed credentials must be discarded and replaced with new ones and any components that use them should be upgraded accordingly, anybody affected must be notified right away.

2 - Second, the following steps can be used to remove the credentials from the commit history: 

a - Checkout a new branch

git checkout --orphan latest_branch

b - Add all the files

git add -A

c - Commit the changes

git commit -am "commit message"

d - Delete the branch

git branch -D main

e - Rename the current branch to main

git branch -m main

f - Finally, force update your repository

git push -f origin main

3 - If credentials were pushed using branches other than the main branch, do the following:

a - Delete the branch remotely:  git push -d <remote_name_aka_ssh_or_https_link> <branchname>
  
b - Delete branch locally from a different branch or main branch: git branch -d <branchname>
  
c - If  the old branch is recreated using git checkout -b <branchname> and pushed using git push, it will not have any previous commit history that contained the credentials.

4 - Here are some links for more details on these steps:
https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-githubhttps://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely 
