// https://www.codewars.com/kata/calculate-average/train/typescript
// My solution
export function find_average(array) {
    return array ? array.reduce((a, b) =>  a + b) / array.length : 0;
    //return array ? array.reduce(function(a, b) { return a + b; }) / array.length : 0;
}

// ...
export function find_average(array) {
    return array.reduce((sum, value) => sum + value ) / array.length;
}
// ...
export function find_average(array) {
    // your code here
    return array.reduce((a,b)=>a+b,0)/array.length;
}
