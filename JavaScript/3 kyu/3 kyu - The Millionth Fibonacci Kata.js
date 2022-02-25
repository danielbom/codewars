// https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/javascript
// My solution
const fibs = { 0: 0n, 1: 1n };
function fib(n) {
  if (n < 0) {
    const x = fib(-n);
    if (n % 2 === 0) return -x;
    else return x;
  }
  if (fibs[n]) return fibs[n];
  if (n < 0) return 0n;
  if (n === 0) return 0n;
  if (n % 2 == 0) {
    fibs[n] = (2n * fib(n / 2 - 1) + fib(n / 2)) * fib(n / 2);
  } else {
    fibs[n] = fib((n - 1) / 2) ** 2n + fib((n + 1) / 2) ** 2n;
  }
  return fibs[n];
}

// And
const fibs = { 0: 0n, 1: 1n };
function fib(n) {
  if (n < 0) {
    const x = fib(-n);
    if (n % 2 === 0) return -x;
    else return x;
  }
  if (n < 1) return 0n;
  if (n < 3) return 1n;
  const k = Math.floor(n / 2);
  const a = fib(k + 1);
  const b = fib(k);
  if (n % 2 === 1) {
    fibs[n] = a * a + b * b;
  } else {
    fibs[n] = b * (2n * a - b);
  }
  return fibs[n];
}

// ...
const fib = n =>
  (fn => (n < 0 && !(n % 2) ? -fn(Math.abs(n))[0] : fn(Math.abs(n))[0]))(
    function fn(n) {
      if (!n) return [0n, 1n];
      const [_n, _n1] = fn(n >> 1);
      const _2n = _n * (2n * _n1 - _n);
      const _2n1 = _n ** 2n + _n1 ** 2n;
      return n % 2 ? [_2n1, _2n + _2n1] : [_2n, _2n1];
    }
  );

// ...
var knownNumbers = {
  '-1': 1n,
  '-2': -1n,
  '-3': 2n,
  0: 0n,
  1: 1n,
  2: 1n,
  3: 2n,
};

function fib(n) {
  if (knownNumbers[n] != undefined) {
    return knownNumbers[n];
  }
  if (n % 2 != 0) {
    var result = fib(n + 1) - fib(n - 1);
    knownNumbers[n] = result;
    return result;
  } else {
    var result = fib(n / 2) * fib(n / 2 - 1) + fib(n / 2) * fib(n / 2 + 1);
    knownNumbers[n] = result;
    return result;
  }
}

// ...
var found = [0n,1n,1n];
found.length = 2000000;

var matrixFib = (f) => {
  if (found[f] !== undefined) return found[f];
  
  var even = !(f % 2);
  var next = even ? f/2 : (f+1)/2;
  var p = matrixFib(next);
  var q = matrixFib(next-1);

  return found[f] = even ? (2n*q + p)*p : (p*p + q*q);
}

function fib(n) {
  if (n >= 0) return matrixFib(n);
  return n %2 ? matrixFib(Math.abs(n)) : -(matrixFib(Math.abs(n)));
}
