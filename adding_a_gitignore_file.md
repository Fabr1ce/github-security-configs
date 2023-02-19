 A gitignore file tells git which files to ignore so they won't get pushed to a remote git repository.
 
 ## Adding a gitignore file:
 To add  gitignore file, create a file called .gitignore at the root of the repository. Add the names of the files and directories git should ignore (i.e. node_modules).
 If those files were previously committed, the cache can be cleared using the following command:

    $ git rm -r --cached <FILE OR DIRECTORY NAME>

    
