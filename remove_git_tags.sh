#!/bin/bash
tags=$(git tag | grep @)

for tag in ${tags[@]}
do
echo "Removing tag: " $tag
$(git tag -d $tag)
$(git push origin :refs/tags/$tag)
done