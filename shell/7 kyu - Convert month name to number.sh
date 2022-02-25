# https://www.codewars.com/kata/convert-month-name-to-number/train/shell
# My solution
month=$(echo "${1,,}")

if [[ $month = "jan"* ]];   then echo "01";
elif [[ $month = "feb"* ]]; then echo "02";
elif [[ $month = "mar"* ]]; then echo "03";
elif [[ $month = "apr"* ]]; then echo "04";
elif [[ $month = "may"* ]]; then echo "05";
elif [[ $month = "jun"* ]]; then echo "06";
elif [[ $month = "jul"* ]]; then echo "07";
elif [[ $month = "aug"* ]]; then echo "08";
elif [[ $month = "sep"* ]]; then echo "09";
elif [[ $month = "oct"* ]]; then echo "10";
elif [[ $month = "nov"* ]]; then echo "11";
elif [[ $month = "dec"* ]]; then echo "12";
fi;
# ...
date -d "${1,,} 1" +%m
# ...
date --date="$(printf "01 %s" $1)" +"%m"
# ...
month="$1"
case "${month,,}" in
  jan|january) echo 01;;
  feb|february) echo 02;;
  mar|march) echo 03;;
  apr|april) echo 04;;
  may) echo 05;;
  jun|june) echo 06;;
  jul|july) echo 07;;
  aug|august) echo 08;;
  sep|september) echo 09;;
  oct|october) echo 10;;
  nov|november) echo 11;;
  dec|december) echo 12;;
  *) return 1;;
esac
# ...
month="${1,,}"
declare -A months=(
    ["january"]="01"
    ["february"]="02"
    ["march"]="03"
    ["april"]="04"
    ["may"]="05"
    ["june"]="06"
    ["july"]="07"
    ["august"]="08"
    ["september"]="09"
    ["october"]="10"
    ["november"]="11"
    ["december"]="12"
)

if [ ${months[$month]} ]; then
    echo ${months[$month]}
else
    for key in ${!months[@]}; do
        if [ ${key:0:3} == $month ]; then echo ${months[$key]}; fi
    done
fi
# ...
month="$1"
month=${month:0:3}
month=${month,,}

case "$month" in
  "dec") echo "12";;
  "nov") echo "11";;
  "oct") echo "10";;
  "jan") echo "01";;
  "feb") echo "02";;
  "mar") echo "03";;
  "apr") echo "04";;
  "may") echo "05";;
  "jun") echo "06";;
  "jul") echo "07";;
  "aug") echo "08";;
  "sep") echo "09";;
esac