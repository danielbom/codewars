// https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/javascript
// My solution
function permutations(string) {
  function permutations_rec(str) {
    const array = str.split('');
    if (str.length <= 1) return array;
    return array.reduce((permutation, e, index) => {
      const substring = str.substring(0, index) + str.substring(index + 1);
      const partial = permutations_rec(substring).map(sub => e + sub);
      permutation.push(...partial);
      return permutation;
    }, []);
  }
  function unique(array) {
    return array.filter((e, i, a) => a.indexOf(e) === i);
  }

  return unique(permutations_rec(string));
}

// ...
let permutations = (s) => {
  if (s.length <= 1) return [s];
  const step = c => permutations(s.replace(c, '')).map(part => part + c);
  return [].concat(...[...new Set(s)].map(step));
};

// ...
function permutations(string) {
  var arr = string.split(''), tmp = arr.slice(), heads = [], out = [];
  if(string.length == 1) return [string];
  arr.forEach(function(v, i, arr) {
    if(heads.indexOf(v) == -1) {
      heads.push(v);
      tmp.splice(tmp.indexOf(v), 1);
      permutations(tmp.join('')).forEach(function(w) {out.push(v + w);});
      tmp.push(v);
    }
  });
  return out;
}

// ...
function permutations(str) {
  return str.length <= 1
    ? [str]
    : Array.from(new Set(
        str.split('')
          .map((char, i) => permutations(str.substr(0, i) + str.substr(i + 1)).map(p => char + p))
          .reduce((r, x) => r.concat(x), [])
      ));
}

// ...
const unique = xs => [ ...new Set(xs) ]
const concat = (a, b) => [ ...a, ...b ] 
const drop = i => xs => [ ...xs.slice(0, i), ...xs.slice(i + 1) ]

const permute = (x, i, xs) => 
  combinations(drop(i)(xs)).map(y => x + y)

const combinations = s =>
  s.length === 1 ? [ s ] : [ ...s ].map(permute).reduce(concat)

const permutations = s => unique(combinations(s));

// ...
function permutations(chs) {
    return [...new Set(
        Array.from( heapsPerms((chs+'').split('')),
        str => str.join('') )
    )];
}

function *heapsPerms(chs, n = chs.length) {
    if (n <= 1) {
      yield chs.slice();
    } else {
      for (let i = 0; i < n; i++) {
        yield *heapsPerms(chs, n-1);
        swap(chs, (n % 2 !== 0) ? 0 : i, n-1);
      }
    }
}

function swap(iterable, i, j) {
    [iterable[i], iterable[j]] = [iterable[j], iterable[i]];
}

// ...
const permutations = (str, perms = []) => {
  if (str.length === 1) return [str];
  for (let i = 0; i < str.length; i++) {
    if (str.indexOf(str[i]) === i) {
      perms = perms.concat(
        permutations(str.slice(0, i) + str.slice(i + 1))
          .map(rest => str[i] + rest)
      );
    }
  }
  return perms;
};

// ...
function permutations(s)  {
  let res = new Set();
  
  const perm = (s, z='') => {
    if ( s.length == 0) res.add(z);

    for (let i=0; i< s.length; i++) 
       perm(s.slice(0, i) + s.slice(i + 1, s.length), z + s[i]);
  }
  
  perm(s);
  return [...res];
}

// ...
