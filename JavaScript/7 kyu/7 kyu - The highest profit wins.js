// https://www.codewars.com/kata/the-highest-profit-wins/train/python
// My solution
function minMax(arr){
    return [Math.min.apply(null,arr), Math.max.apply(null,arr)];
}

// ...
const R = require("ramda");

const minMax = (args) => R.juxt([Math.min, Math.max])(args[0], ...args);

// ...
const R = require("ramda");

const minMax = R.ifElse(
  R.pipe(R.length, R.equals(1)),
  R.ap(R.concat, R.identity),
  R.apply(R.juxt([Math.min, Math.max]))
);

// ...
function minMax(arr) {
    return [Math.min(...arr), Math.max(...arr)];
}
