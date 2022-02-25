# https://www.codewars.com/kata/bash-basics-while-loop/train/shell
# My solution
#!/bin/bash
countToTwenty() {
    i=1
    while [ $i -le 20 ]; do
        echo Count: $i
        i=$((i+1))
    done
}
countToTwenty
# ...
echo "Count: "{1..20}
# ...
#!/bin/bash
for i in $(seq 1 20); do echo "Count: $i"; done
# ...
#!/bin/bash
countToTwenty() {
  for i in {1..20}; do echo "Count: ${i}"; done
}
countToTwenty
# ...
#!/bin/bash
countToTwenty() {
  i=1
  while [ $i -le 20 ]
  do
    echo Count: $i
    let i++
  done
}
countToTwenty
#!/bin/bash
# ...
countToTwenty() {
  for((i=0; i<=20; i++))
  do
    printf "Count: %d\n" $i
  done
}
countToTwenty