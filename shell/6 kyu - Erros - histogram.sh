# https://www.codewars.com/kata/errors-histogram/train/shell
# My solution
function stars () {
    n=$1;
    s="";
    for (( i=0; i<$n; i++ )); do
        s=$s"*";
    done;
    echo $s;
}
function hist () {
    str=$1
    local u=$(echo $str | grep -o u | wc -l);
    local w=$(echo $str | grep -o w | wc -l);
    local x=$(echo $str | grep -o x | wc -l);
    local z=$(echo $str | grep -o z | wc -l);
    [[ $u -ne 0 ]] && echo -n -e "u "$u" "$(stars "$u" )"\r"
    [[ $w -ne 0 ]] && echo -n -e "w "$w" "$(stars "$w" )"\r"
    [[ $x -ne 0 ]] && echo -n -e "x "$x" "$(stars "$x" )"\r"
    [[ $z -ne 0 ]] && echo -n -e "z "$z" "$(stars "$z" )"\r"
}
hist "$1"
# ...
hist () {
  grep -o "[uwxz]" <<< "$1" | sort | uniq -c |
  awk '{ s=""; for(i=0; i<$1; i++) s=s"*"; printf "%-2s%-d %s\r", $2, $1, s }'
}
hist "$1"
# ...
aux='
sub aux {
    my $s = shift; my @base=("w", "x", "z", "u"); my %count;
    foreach my $b (@base) {
        while($s =~ /$b/g) { $count{$b}++ }
    }
    my @keys = sort { $a cmp $b } keys %count;
    my $res = "";
    foreach my $key ( @keys ) {
        my $val = $count{$key};
        $res .= sprintf("%-2s %-6s", $key, $val).("*" x $val)."\r";
    }
    return substr($res, 0, -1);
}
$a=aux($ARGV[0]);
print $a;
'
hist () {
    echo `perl -e "$aux" "$1"`
}
hist "$1"
# ...
hist () {
    # your code
    str=$1;
    length=${#str}
    i=0;
    errors=();
    errors[0]=0;
    errors[1]=0;
    errors[2]=0;
    errors[3]=0;
    while [ $i -lt $length ];
    do
      curr=${str:$i:1}
      if [[ $curr == "u" ]];
      then
        let errors[0]++;
      elif [[ $curr == "w" ]]; then
        let errors[1]++;
      elif [[ $curr == "x" ]]; then
        let errors[2]++;
      elif [[ $curr == "z" ]]; then
        let errors[3]++;
      fi
      let i++;
    done
    
    i=0;
    error_letters=( 'u' 'w'  'x' 'z' ) 
    res=""
    while [ $i -lt 4 ];
    do
      count=${errors[$i]}
      if [ $count -gt 0 ];
      then
        starts=$(for j in `seq $count`; do echo -n "*"; done)
        letter=${error_letters[$i]}
        temp="`echo $letter $count $starts`"
        if [[ -z $res ]];
        then
          res="$temp"
        else
          res="$res\r$temp"
        fi
      fi
      let i++;
    done
    
    echo -e $res
}
hist "$1"
# ...
str=$(echo "$1" | sed 's/[a-z]/\n&/g' | sort | tr -d "\n" | tr -d [a-tvy]) 
while [ "${#str}" -gt "0" ]
do
    ch="${str:0:1}"
    len=${#str}
    str=${str##*$ch}
    len=$((len-${#str}))
    echo -n "$ch $len "
    for(( i=0;i<$len;i++ ))
    do
        echo -n '*'
    done
    echo -n $'\r'
done
# ...
star=*********************************** star+=$star
declare -A cnt=()
for (( i = 0, n = ${#1}; i < n; ++i )); do
    (( 'cnt[${1:i:1}]++' ))
done
for c in u w x z; do
    (( 'cnt[$c]' > 0 )) || continue
    printf '%s%s %d %s' "$sep" "$c" "${cnt[$c]}" "${star:0:cnt[$c]}"
    sep=$'\r'
done
# ...
hist() {
    a="*" f="  %-6d%s\r"
    for ((i=0; i<${#1}; i++))
    do case ${1:i:1} in
            u) ((cu++)); u+=$a;;
            w) ((cw++)); w+=$a;;      
            x) ((cx++)); x+=$a;;
            z) ((cz++)); z+=$a      
        esac
    done
    [ $cu ] && s+=$(printf "u$f" $cu $u)
    [ $cw ] && s+=$(printf "w$f" $cw $w)
    [ $cx ] && s+=$(printf "x$f" $cx $x)
    [ $cz ] && s+=$(printf "z$f" $cz $z)
    echo $s
}
hist "$1"
# ...
perl -e '
    $Q = $ARGV[0];
    $N = length($Q);
    $U = $W = $X = $Z = 0;
    for ($F = $N;$F--;)
    {
        $T = substr($Q,$F,1);
        if ("u" eq $T) {++$U;}
        if ("w" eq $T) {++$W;}
        if ("x" eq $T) {++$X;}
        if ("z" eq $T) {++$Z;}
    }
    # if ($U) {printf "u  %-6s%s\r",$U,"*"x$U;}
    # if ($W) {printf "w  %-6s%s\r",$W,"*"x$W;}
    # if ($X) {printf "x  %-6s%s\r",$X,"*"x$X;}
    # if ($Z) {printf "z  %-6s%s",$Z,"*"x$Z;}
    if ($U) {print "u ",$U," ","*"x$U,"\r";}
    if ($W) {print "w ",$W," ","*"x$W,"\r";}
    if ($X) {print "x ",$X," ","*"x$X,"\r";}
    if ($Z) {print "z ",$Z," ","*"x$Z;}
' "$1"
echo