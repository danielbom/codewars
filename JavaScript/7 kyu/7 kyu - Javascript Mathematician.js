// https://www.codewars.com/kata/55c211cce1ef691d9b000061/train/javascript
// My solution
const sum = (xs) => xs.reduce((a, b) => a + b, 0);
const calculate =
  (...xs) =>
  (...ys) =>
    sum(xs) + sum(ys);
