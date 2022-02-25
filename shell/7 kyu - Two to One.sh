# https://www.codewars.com/kata/two-to-one/train/shell
# My solution
#!/bin/bash
longest () {
    concat=$(echo $(printf "%s%s" $1 $2) | sed -e 's/\(.\)/\1\n/g')
    alphabet=$(echo "abcdefghijklmnopqrstuvwxyz" | sed -e 's/\(.\)/\1\n/g')
    result=''
    for alpha in $alphabet
    do
        for letter in $concat
        do
            if [ $alpha == $letter ]
            then
                result=$(printf "%s%s" $result $alpha)
                break
            fi
        done
    done
    echo $result
}
longest "$1" "$2"

# ...
longest() {
    echo $1$2 | grep -o . | sort -u | paste -sd "" -
}
longest "$1" "$2"

# ...
longest () {
   string="$1$2"
   data=`echo "$string"|grep -o "[a-z]"|sort|uniq|tr -d '\n'`
   echo "$data"
}
longest "$1" "$2"
# ...
a=$1
b=$2
longest () {
    # your code
    con="$a$b"
    read -a clear_arr <<< $(echo $con | sed 's/./& /g')
    IFS=$'\n'
    sorted_arr=($(sort <<<"${clear_arr[*]}"))
    unset IFS
    printf -v sorted_str '%s' "${sorted_arr[@]}"
    result=$(echo $sorted_str | tr -s [:upper:][:lower:])
    
    echo $result
    
}
longest "$1" "$2"