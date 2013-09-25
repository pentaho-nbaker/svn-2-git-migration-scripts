# svn to git migration scripts

This is a collection of scripts and files to support the migration of Pentaho subversion repositories to git.

## Basic Usage

A fairly comprehensive authors file is included as authors.txt. Please update this if you have changes and use it for all migrations.

We're using the svn2git migration tool to perform the import. Follow the setup instructions on the svn2git project page:  
https://github.com/nirvdrum/svn2git  

One setup execute the following to import a subversion project:

    # svn2git doesn't create a folder for you, do so yourself
    mkdir NEW_REPO  
    cd NEW_REPO  

    # Assumes you've cloned this repo to the parent directory
    svn2git $SUBVERSION_FOLDER_URL  --authors ../svn-git-migration-scripts/authors.txt  
      optional: --nobranches --notags  

    # When importing from the internal SVN, you might need to provide
    # your username and password. You will need to use the following arguments:
    svn2git $SUBVERSION_FOLDER_URL -v --username [username] --authors ../svn-git-migration-scripts/authors.txt

    # Remove deleted branches and tags, we don't want them.
    git branch -a | grep @ | xargs git branch -d  
    git tag | grep @ | xargs git tag -d  
    
    # Normalize line-endings, run from the directory right above your repo
    zip -qr normal.zip NEW_REPO && unzip -aqo normal.zip && rm normal.zip
    
    
    # Add in our stadard .gitignore and .gitattributes files as found in this repo.
       "git add" then "git commit" them  
  
    git remote add origin $GITHUB_URL  
    git push origin master  
       (optionally push other branches)  

    # To push all branches
    git push origin --all

    # To push all tags  
    git push origin --tags  


## Generating an authors file

- `sh gen-svn-authors.sh $REPO_URL > my-repos-authors.txt` This generates an authors list in the format `svn_username = svn_username <svn_username@pentaho.com>`
- Edit my-repos-authors.txt to fix the actual names and email addresses as required.

## Removing history beyond a certain commit

In the event that a subversion project was created as a copy of another the migration will follow the history back to through the original project. This is not desirable and history past the creation of the project should be discarded. You can use the following command to remove history beyond a certain commit hash. This is not permanent until you invoke `git gc` on the repository.

`sh git-remove-history-past.sh $COMMIT_HASH`

## Advanced Scripts

### Reparenting branches

The `git-replace-parent.sh` script was useful to fix branchs when migrating the Mondrian project from Perforce. It will likely not be needed for any Subversion migration but it exists incase we need to manually fix branch histories. For more information see http://stackoverflow.com/questions/3810348/setting-git-parent-pointer-to-a-different-parent.

## Aftermath

- Move the subversion repository to the "archive" section. Preserving the structure as much as possible
- Update the wiki with the project you've migrated, old and new locations: http://wiki.pentaho.com/display/PEOpen/Project+Migration+List
