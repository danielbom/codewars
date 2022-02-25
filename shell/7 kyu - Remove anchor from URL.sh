# https://www.codewars.com/kata/remove-anchor-from-url/train/shell
# My solution
#!/bin/bash
echo $1

# ...
#!/bin/bash
${1%#*}

# ...
#!/bin/bash
echo $1 | cut -f1 -d "#"

# ...
#!/bin/bash
sed -e 's/#.*//' <<< $1