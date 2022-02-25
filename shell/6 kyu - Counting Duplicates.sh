# https://www.codewars.com/kata/counting-duplicates/train/shell
# My solution
echo $1 | tr "[A-Z]" "[a-z]" | grep -o . \
        | sort | uniq -c | grep -o "[^1] [a-z]" \
        | cut -d " " -f 2 | wc -l
# Maybe
echo $1 | tr "[A-Z]" "[a-z]" | grep -o . | sort \
        | uniq -c | grep -o "[^1] [a-z]" | wc -l
# ...
grep -o . <<< $1 | sort -f | uniq -id | wc -l
# ...
fold -w1 <<< "${1,,}" | sort | uniq -d | wc -l
# ...
echo $1 | grep -o . | sort -f | uniq -id | wc -l
# ...
echo $1 | tr [A-Z] [a-z] | grep -o . | sort | uniq -d | wc -l
# ...
echo $1 | tr '[:upper:]' '[:lower:]' \
   | awk -F '' 'BEGIN{OFS="\n"} {$1=$1; print $0}' \
   | sort | uniq -c | awk '{if ($1>=2) print $2}' \
   | wc -l
# ...
echo ${1^^} | fold -w1 | sort | uniq -c | tr -d ' ' | grep -v "^1" | wc -l
# ...
echo $1 | awk \ 
'{l=tolower($0); \
for (i=1; i<=length(l); i++) \
    chars[substr(l,i,1)]++ }; \
END { \
dups=0; \
for (i in chars) \
    if (chars[i]>1) \
        dups++;
print dups \
}'
