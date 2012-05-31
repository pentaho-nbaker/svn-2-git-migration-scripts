#!/bin/sh

function usage {
  echo "Removes all history beyond the commit hash provided"
  echo "usage: $script commit-hash comment-to-use-for-initial-commit";
}

[ $# -lt 2 ] && usage && exit 1

git checkout -b oldroot $1
TREE=`git write-tree`
COMMIT=`echo "$2" | git commit-tree "$TREE"`
git checkout -b newroot "$COMMIT"
git rebase --onto newroot oldroot master
# repeat for other branches than master that should use the new initial commit
#git rebase --onto newroot oldroot 1.1
#git checkout master
#git branch -D oldroot
#git branch -D newroot

echo "Please review repository history. Run git gc to make changes permanent!"
#git gc # WARNING: if everything's done right, this will actually delete your history from the repo!
