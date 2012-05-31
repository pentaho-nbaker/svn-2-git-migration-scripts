#!/bin/sh

function usage {
  echo "Generates an authors list to use with git-svn from the provided working directory or svn url."
  echo "usage: $0 svn-url"
}

[ $# -lt 1 ] && usage && exit 1

DOMAIN="@pentaho.com"

echo "Building svn authors list for $1..."
svn log -q $1 | awk -v DOMAIN=$DOMAIN -F '|' '/^r/ {sub("^ ", "", $2); sub(" $", "", $2); print $2" = "$2" <"$2DOMAIN">"}' | sort -u >> authors-tmp.txt
