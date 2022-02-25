# https://www.codewars.com/kata/remove-first-and-last-character/train/shell
# My solution
function removeChar() {
  str=$1
  echo ${str:1:-1}
}
removeChar $1
# ...
arg=$1
echo "${arg:1:-1}"
# ...
function removeChar() {
    echo ${1:1:-1}
}
removeChar $1