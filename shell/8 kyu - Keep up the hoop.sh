# https://www.codewars.com/kata/keep-up-the-hoop/train/shell
# My solution
#!/bin/bash
if [ $1 -lt 10 ]; then
    echo "Keep at it until you get it"
else
    echo "Great, now move on to tricks"
fi

# ...
#!/bin/bash
n=$1
if [ "$n" -ge 10 ];then
    echo 'Great, now move on to tricks'
else
    echo 'Keep at it until you get it'
fi
# ...
#!/bin/bash
(( $1 >= 10 )) && echo 'Great, now move on to tricks' || echo 'Keep at it until you get it'
# ...
#!/bin/bash
win="Great, now move on to tricks";
fail="Keep at it until you get it";
[[ $1 -ge 10 ]] && echo $fail || echo $win;
# ...
#!/bin/bash
[[ $1 -lt 10 ]] && echo 'Keep at it until you get it' || echo 'Great, now move on to tricks'
# ...
#!/bin/bash
if (( $1 < 10 ))
  then echo "Keep at it until you get it"
  else echo "Great, now move on to tricks"
fi