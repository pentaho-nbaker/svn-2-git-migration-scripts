#!/bin/sh

script=`basename $0`
dir=`pwd`/`dirname $0`;
function usage {
  echo "Creates a git repository from an svn repository."
  echo "usage: $script svn-repo authorsfile";
}

[ $# -lt 2 ] && usage && exit 1

svn="$1"
authorsfile="$2"

#set -- `getopt s:a: $@`
#[ $# -lt 2 ] && usage && exit 1

# while [ $# -gt 0 ]
# do
#   case "$1" in
#     -s) svn="$2";;
#     -a) authorsfile="$2";;
#     --) shift; break;;
#     *) break;;
#   esac
#   shift
# done

echo "SVN Repository: $svn"
echo "Authors File: $authorsfile"

cmd="git svn clone --authors-file=$authorsfile --no-metadata -s $svn repo 2>&1 | tee import.log"
$cmd