


####################USING GIT######################

### SETTING UP AND USING A LOCAL GIT REPOSITORY
#initializing git for a folder/project
#- your current pwd must be the folder you wish to initialize
$ git init  # creates a .git folder which holds the layers of the git repository

# view the current status of the git repository here
#- tells if commits have been made and shows untracked files (ie files not committed yet)
$ git status

# add a file to staging area
$ git add file.ext  # this file will no longer show in untracked files

# remove a file from the staging area
$ git rm --cached file.ext   # does not change or delete the file contents, just removes it from staging area

# commit to git
$ git commit -m "message we would like to add to our commit"

# edit your git configuration file
# (global means you are change the default git config file for all new initialized git repositories
$ git config --global --edit

# get log file of git commits (lets you see historical commits
$ git log

# get one line abbreviated summary of each commit in git log
$ git log --online

# get a graphical representation of the commits
$ git log --graph


####SETTING UP A REMOTE GIT REPOSITORY

# create a ssh key to use with remote git repository
# - (key will be used for all future git repositories)
$ ssh-keygen

# view key, use this as an easy way to copy the key
# - copy this public key and add it to your github account(or other remote repository acct)
$ cat ~/.ssh/id_rsa.pub

# open up ssh-agent
$ eval "$(ssh-agent -s)"

# add private ssh key to ssh-agent
$ ssh-add ~/.ssh/id_rsa

# adding your git repository to github
# to do this from the command line the pwd needs to have git initialized (ie contain a .git folder)
$ git remote add origin "link"  #sends all current commits to this remote repository (github etc)

# checks the origin object being (the link to the remote repository) being used
$ git remote -v # if using https:// then you will always be asked for a username and password when pushing

# sets/renames the origin for pushing and pulling to remote repository
$ git remote set-url origin git@github.com:name/repo.git
# you want to use the above method instead of https way so you can do passwordless access to github when pushing and pulling
#- for example use: git@github.com:CraftFlow/test.git rather than https://github.com/Craftflow/test.git

# pushes the local repository to the remote repository (again need to be within the pwd of the git repository
$ git push -u origin master #sets the push up to push to the specified origin and also the master branch
$ git push -u # once the first push is set up above, all other pushes can be made with just this
#-- or just use
$ git push origin master
$ git push

# create a readme file for github to use
vim readme.md   #md means this is a markdown file, so you need to write in markdown language

# for pulling others changes...see udemy website for the video

###Notes###

# when committing a message containing something like this in brackets will appear
[master (root-commit) 678f6d7]
    # it tells important information about the commit
       ["what branch committed to" ("commit type")  "commit id"]
    # for example: the above means it committed to the master branch
       #- root-commit means it was the first commit ever to this branch


### Deleting git repo
$ rm -rf .git*


