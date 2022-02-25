# https://www.codewars.com/kata/pi-approximation/train/shell
# My solution
#!/bin/bash
iterPi() {
    local pi="3.141592653589"
    local i=1
    local signal=1
    local calc=0
    local calc_ps=$(echo "$calc - $pi" | bc -l)
    local diff=$(echo $calc_ps | tr -d -) # abs

    while (( $(echo "scale=10; $diff > $1" | bc -l) ))
    do
        local calc=$(echo "scale=12; $calc + (4.0 / $i) * $signal" | bc -l)
        local i=$(($i+2))
        local signal=$(($signal*-1))
        local calc_ps=$(echo "$calc - $pi" | bc -l)
        local diff=$(echo $calc_ps | tr -d -) # abs
    done
    local iter=$(echo "scale=0; ($i - 1) / 2" | bc -l)
    printf "%.0f %.10f" $iter $calc
}
iterPi $1
# Not complete