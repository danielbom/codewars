// https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/javascript
// My solution
function digitize(n) {
    return ("" + n).split("").reverse().map(a => +a)
}

// ...
function digitize(n) {
    return String(n).split('').map(Number).reverse()
}