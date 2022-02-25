// https://www.codewars.com/kata/return-negative/train/javascript
// My solution
function makeNegative(num) {
    return num > 0 ? -num : num
}

// ...
function makeNegative(num) {
    return -Math.abs(num);
}

// ...
var makeNegative=n=>~(n>>31<<1)*n

