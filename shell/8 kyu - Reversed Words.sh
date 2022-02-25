# https://www.codewars.com/kata/reversed-words/train/shell
# My solution
n=0
for arg in $@ ; do
    let n++
done

declare -a argv=( $@ )
for (( i = $n - 1 ; i >= 0; i--)) ; do
    printf "${argv[$i]} "
done
# ...
result=
for word in $1; do
  result="$word $result"
done
echo $result
# ...
for i in $(echo $1); do echo $i; done | tac | tr '\n' ' ' && echo
# ...
echo $1 | awk '{ for (i=NF; i>1; i--) printf("%s ",$i); print $1; }'
# ...
echo $1 | tac -s ' ' | tr '\n' ' '
# ...
array=(${1})
for (( i=${#array[*]}; i > -1; i-- )); do
    printf "%s " ${array[$i]}
done
