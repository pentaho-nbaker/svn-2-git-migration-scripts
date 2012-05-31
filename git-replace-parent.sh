#!/bin/sh

replace_first_parent() {
    old_parent=$(git rev-parse --verify "${1}^1") || return 1
    new_parent=$(git rev-parse --verify "${2}^0") || return 2
    new_commit=$(
      git cat-file commit "$1" |
      sed -e '1,/^$/s/^parent '"$old_parent"'$/parent '"$new_parent"'/' |
      git hash-object -t commit -w --stdin
    ) || return 3
    git replace "$1" "$new_commit"
}

replace_first_parent $@