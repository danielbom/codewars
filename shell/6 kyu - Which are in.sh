# https://www.codewars.com/kata/which-are-in/train/shell
# My solution
inArray() {
    lst=""
    for w1 in $1; do
        for w2 in $2; do
            if [[ $w2 =~ $w1 ]]; then
                lst=" $w1"$lst
            fi
        done;
    done;
    lst=$(echo $lst | tr -c '[:graph:]' '[\n*]' | sort | uniq | tr -s "\n" ",")
    echo ${lst::-1}
}
inArray "$1" "$2"
# ...
inArray() {
    sorted1=$(echo "$1" | tr " " "\n" | sort -u)

    for j in $sorted1; do 
      if [[ $2 == *$j* ]]; then 
        if [[ -z "$str" ]]; then
          str=$j
        else
          str="$str,$j"
        fi
      fi
    done
    echo "$str"
}
inArray "$1" "$2"
# ...
inArray() {
    result=()
    for x in $1; do
        for y in $2; do
            if [[ $y == *"$x"* ]]; then
                result+=( $x )
                break
            fi
        done
    done
    echo $(echo ${result[*]} | tr ' ' "\n" | sort | uniq | tr "\n" "," | sed 's/,$//')
}
inArray "$1" "$2"
# ...
inArray() {
        while read -d" " step; do
                if [[ "$2" =~ "$step" ]]; then
                        echo $step
                fi
        done <<<"$1 "
}
inArray "$1" "$2" | sort -u | sed -z 's/\n/,/g;s/,$//'
# ...
inArray() {
    res=`for word in $1; do grep $word <<< "$2" > /dev/null && echo "$word"; done | sort -u`;
    echo $res | sed 's/\s/,/g';
}
inArray "$1" "$2"
# ...
inArray() {
    read -a instrings <<< "$1"
    for instring in ${instrings[@]}; do
        [[ "$2" =~ "$instring" ]] && echo $instring
    done | sort -u | paste -sd ','
}
inArray "$1" "$2"
# ...
inArray() {
    for s1 in $1; do
        for s2 in $2; do
            [[ $s2 = *$s1* ]] && echo $s1
        done
    done | sort -u | tr '\n', ',' | head -c -1
}
inArray "$1" "$2"
# ...
for i in $1; do grep -q "$i" <<< $2 && echo $i; done | sort -u | tr "\n" "," | sed s/,$//
# ...
inArray() {
    [[ -z "$1" || -z "$2" ]] && {
      echo ""
      exit
    }
    local s1=($1)
    for s in "${s1[@]}"; do
      [[ "$2" == *$s* ]] && echo $s
    done  | sort | uniq | xargs echo | tr ' ' ','
}
inArray "$1" "$2"