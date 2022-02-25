# https://www.codewars.com/kata/jennys-secret-message/train/shell
# My solution
#!/bin/bash
if [ "$1" == "Johnny" ]; then
  echo "Hello. my Love!"
fi
echo "Hello, $1!"
# ...
[[ $1 == "Johnny" ]] && echo "Hello. my Love!" || echo "Hello, ${1}!"
