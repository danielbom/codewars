// https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/javascript
// My solution
function josephus(items, k) {
  const result = [];
  let next = (k - 1) % items.length;
  while (items.length > 0) {
    result.push(items[next]);
    items = items.filter((_, i) => i !== next);
    next = (next + k - 1) % items.length;
  }
  return result;
}

// And
const nextSafePosition = (length, current, k) => (current + k - 1) % length;

const josephus = (items, k) =>
  items.reduce(
    ([result, next, rest]) => [
      [...result, rest[next]],
      nextSafePosition(rest.length - 1, next, k),
      rest.filter((_, i) => i !== next),
    ],
    [[], (k - 1) % items.length, items]
  )[0];

// And
const nextSafePosition = (length, current, k) => (current + k - 1) % length;

const josephus = (items, k) => {
  const rec = (rest, next) =>
    rest.length > 0
      ? [
          rest[next],
          ...rec(
            rest.filter((_, i) => i !== next),
            nextSafePosition(rest.length - 1, next, k)
          ),
        ]
      : [];

  return rec(items, (k - 1) % items.length);
};

// And
const R = require("ramda");

const josephus = R.pipe(
  (items, k) => [items, (len, curr) => (curr + k - 1) % len],
  (items, f) =>
    items.reduce(
      ([arr, next, rest]) => [
        arr.concat(rest[next]),
        f(rest.length - 1, next),
        R.remove(next, rest),
      ],
      [[], (k - 1) % items.length, items]
    ),
  F.head
);

// ...
function josephus(items, k){
  var result = [], index = 0;
  while (items.length > 0){
    index = (index + k - 1) % items.length;
    result = result.concat(items.splice(index, 1));
  }
  return result;
}

// ...
function josephus(items,k){
  var dest = [],
      i = 0;
  
  while (items.length > 0) {
    dest.push(items.splice(i = (i + k - 1) % items.length, 1)[0]);
  }
  
  return dest;
}

// ...
const josephus = (items, k) =>
  [...items]
    .reverse()
    .map((_, i, a) => (a.splice(i, 0, ...a.splice(-k % (a.length - i))), a[i]));
