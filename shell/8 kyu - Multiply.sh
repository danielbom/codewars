# https://www.codewars.com/kata/multiply/train/shell
# My solution
#!/bin/bash -e
a=$1
b=$2
echo $((a*b))

# ...
#!/bin/bash -e
echo $(($1*$2))

# ...
#!/bin/bash -e
a=$1
b=$2
c=`expr $a * $b`
echo $c

# ...
#!/bin/bash -e
a=$1
b=$2
expr $a \* $b

# ...
#!/bin/bash
a=$1
b=$2
c=$[a * b]
echo $c