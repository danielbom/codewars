# https://www.codewars.com/kata/regex-password-validation/train/shell
# My solution
password=$1

if [[ 6 -le $(echo $1 | grep -o . | wc -l) ]]; then
    if [[ $(echo $1 | grep -o "[1-9]") ]]; then
    if [[ $(echo $1 | grep -o "[a-z]") ]]; then    
    if [[ $(echo $1 | grep -o "[A-Z]") ]]; then
    if [[ $(echo $1 | grep -o "[^1-9A-Za-z]") ]]; then
      echo "false";
    else echo "true"; fi;
    else echo "false"; fi;
    else echo "false"; fi;
    else echo "false"; fi;
else echo "false";
fi;
# ...
password=$1
if [[ 
     "$password" =~ ^[[:alnum:]]{6,}$ &&
     "$password" =~ [[:upper:]] &&
     "$password" =~ [[:lower:]] &&
     "$password" =~ [[:digit:]] 
   ]]; then
  echo "true";
else
  echo "false";
fi
# ...
password=$1
if [[
  ! "${password}" =~ ^[[:alnum:]]{6,}$ ||
  ! "${password}" =~ [[:digit:]] ||
  ! "${password}" =~ [[:lower:]] ||
  ! "${password}" =~ [[:upper:]]
]]; then
  echo "false"
  exit 1
fi
echo "true"
# ...
[[ $1 =~ ^[a-z0-9A-Z]{6,}$ && $1 =~ [a-z] && $1 =~ [A-Z] && $1 =~ [0-9] ]] && echo "true" || echo "false"
# ...
password=$1
a=$(echo $password | egrep "^[a-z0-9A-Z]{6,}$" | egrep "[a-z]" | egrep "[A-Z]" | egrep "[0-9]")
if [$a == ""]; then
    echo "false"
else
    echo "true"
fi
# ...
echo -n "$password" | grep -oP '^(?=.*[[:lower:]])(?=.*[[:upper:]])(?=.*[[:digit:]])[[:alnum:]]{6,}$' > /dev/null
#if [[ $password =~ '^(?=.*[[:lower:]])(?=.*[[:upper:]])(?=.*[[:digit:]])[[:alnum:]]{6,}$' ]]; then

if [ $? -ne 0 ]; then
  echo "false"
else
  echo "true"
fi
# ...
password=$1
if [[
    ${#password} -lt 6 ||
    ! ${password} =~ ^[[:alnum:]]*$ ||
    ! ${password} =~ [[:digit:]] ||
    ! ${password} =~ [[:lower:]] ||
    ! ${password} =~ [[:upper:]]
]]; then
    echo "false"
    exit 1
fi
echo "true"
# ...
if (echo "$1" | grep -Pq "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{6,}$"); then 
    echo 'true'
else
    echo 'false'
fi
# ...
if [[ $1 =~ ^[A-Za-z0-9]{6,}$ ]] && [[ $1 =~ [0-9] ]] && [[ $1 =~ [A-Z] ]]  && [[ $1 =~ [a-z] ]]; then
    echo "true"
else
    echo "false"
fi
# ...
an6='^[a-zA-Z0-9]{6,}$'; ll='[a-z]'; ul='[A-Z]'; num='[0-9]'
[[ $1 =~ $an6 && $1 =~ $ll && $1 =~ $ul && $1 =~ $num ]] && echo true || echo false
# ...
password="$1"
regex='(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])^[a-zA-Z0-9]{6,}$'

grep -qP "$regex" <<< "$password" && echo true || echo false
# ...
[[
     $1 =~ ^[A-Za-z0-9]{6,}$
  && $1 =~ [A-Z]
  && $1 =~ [a-z]
  && $1 =~ [0-9] 

]] && echo true || echo false
# ...
(( $(wc -c <<<"$1") > 6 ))  || { echo false; exit 1; }
[[ $1 =~ [[:lower:]]  ]]    || { echo false; exit 2; }
[[ $1 =~ [[:upper:]]  ]]    || { echo false; exit 3; }
[[ $1 =~ [[:digit:]]  ]]    || { echo false; exit 4; }
[[ $1 =~ [^[:alnum:]] ]]    && { echo false; exit 5; }
echo true
# ...
awk -v s=$1 '
function good(s) {
    if (length(s) < 6)        return 0
    if (  s ~ /[^a-zA-Z0-9]/) return 0
    if (!(s ~ /[a-z]/))       return 0
    if (!(s ~ /[A-Z]/))       return 0
    if (!(s ~ /[0-9]/))       return 0
    return 1
}
BEGIN {
   print good(s) ? "true" : "false"
}
'