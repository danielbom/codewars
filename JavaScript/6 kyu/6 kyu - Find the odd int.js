// https://www.codewars.com/kata/find-the-odd-int/train/javascript
// My solution
function findOdd(A) {
    counter = A.reduce(function (acc, curr) {
        if (typeof acc[curr] == 'undefined') {
            acc[curr] = 1
        } else {
            acc[curr] += 1
        }
    return acc
    }, {})
    
    return parseInt(Object.keys(counter).filter(function(key) {
        return counter[key] % 2
    })[0])
}

// ...
const findOdd = (xs) => xs.reduce((a, b) => a ^ b);

// ...
function findOdd(A) {
    var obj = {};
    A.forEach(function(el){
        obj[el] ? obj[el]++ : obj[el] = 1;
    });

    for(prop in obj) {
        if(obj[prop] % 2 !== 0) return Number(prop);
    }
}
