# https://www.codewars.com/kata/bash-basics-find-number-of-files-in-a-directory/train/shell
# My solution
if [[ -z $1 ]]; then
  echo "Nothing to find"
elif [[ -z $(find . -type d -name $1) ]]; then
  echo "Directory not found"
else
  n_files=$(find $1 -maxdepth 1 -type f | grep -e "./[^.]" | wc -l)
  abs_path=$(readlink -f $1)
  echo "There are "$n_files" files in "$abs_path
fi
# ...
if [ -z $1 ] ; then
  echo "Nothing to find"
  exit
fi

if [ ! -d $1 ] ; then
  echo "Directory not found"
  exit
fi

echo "There are $(find $1 -type f | wc -l) files in $(pwd)/$1"
# ...
if [ -z $1 ] ; then
  echo "Nothing to find!"
elif [ ! -d $1 ] ; then
  echo "Directory not found"
else
  echo "There are" `ls $1/ | wc -l` "files in" `cd $1; pwd`
fi
# ...
if [[ ! $1 ]]; then
  echo 'Nothing to find'
elif [[ ! -d $1 ]]; then
  echo 'Directory not found'
else
  result=$(find "$1" -maxdepth 1 -type f -printf "\n" | wc -l)
  echo "There are $result files in $(readlink -f $1)"
fi
# ...
[ $1 ] || echo "Nothing to find" || exit 1
cd $1 || echo "Directory not found" || exit 1
echo "There are $(find . -maxdepth 1 -type f | wc -l) files in $(pwd)"