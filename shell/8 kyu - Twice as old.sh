# https://www.codewars.com/kata/twice-as-old/train/shell
# My solution
dad_years_old=$1
son_years_old=$2

son_2_pluss=$(($2 * 2))
echo $(($dad_years_old - $son_2_pluss)) | tr -d -

exit
# ...
echo $((2 * $2 - $1)) | tr -d -

