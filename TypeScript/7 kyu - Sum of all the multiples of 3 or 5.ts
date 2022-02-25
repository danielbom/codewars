// https://www.codewars.com/kata/sum-of-all-the-multiples-of-3-or-5/train/javascript
// My solution
function findSum(n) {
    var sum = 0;
    for (var i = 1; i <= n; i++)
        sum += i % 3 == 0 || i % 5 == 0 ? i : 0;
    return sum;
}

// ...
const sumMultiples = (m, n) => {
    let x = n / m | 0;
    return m * x * (x + 1) / 2;
};
const findSum = n => sumMultiples(3, n) + sumMultiples(5, n) - sumMultiples(15, n);
// ...
const f = (k, n) => k * ~~(n / k) * ~~(n / k + 1) / 2;
const findSum = n => f(3, n) + f(5, n) - f(15, n);
// ...
function findSum(n) {
    return Array.from({ length: n }, (a, b) => b + 1)
        .reduce(function (curSum, val) {
            return !(val % 5 && val % 3) ? curSum + val : curSum;
        }, 0)
}
// ...
function findSum(n) {
    if (n < 3) return 0
    return (n % 3 === 0 || n % 5 === 0) ? n + findSum(n - 1) : findSum(n - 1)
}
// ...
const findSum = n => Array(n + 1).fill().map((a, i) => i).reduce((a, b) => (b % 3 == 0 || b % 5 == 0) ? a + b : a + 0);
// ...
const findSum = n => [...Array(n + 1).keys()].filter(cur => cur % 3 === 0 || cur % 5 === 0).reduce((acc, cur) => acc + cur, 0);
// ...
const fiveOr3 = (s, v) => (v % 3 == 0 || v % 5 == 0) ? s + v : s
const findSum = n => [...Array(n + 1).keys()].slice(1).reduce(fiveOr3, 0)
// ...
function findSum(n) {
    var iM3 = Math.floor(n / 3);
    var iM5 = Math.floor(n / 5);
    var iM15 = Math.floor(n / 15);
    return 3 * gauss(iM3) + 5 * gauss(iM5) - 15 * gauss(iM15);
}
function gauss(m) {
    return (m * (m + 1)) / 2;
}
// ...
function findSum(n) {
    return Array.from({ length: n }, (v, i) => i + 1).filter(x => (x % 3 == 0 || x % 5 == 0)).reduce((a, b) => a + b, 0);
}