// https://www.codewars.com/kata/59f7a040a5b820c684000046/train/javascript
// My solution
class List {
  static fromList(xs, index = 0) {
    if (index >= xs.length) return List.empty;
    return new List(xs[index], () => List.fromList(xs, index + 1));
  }

  static cycle(xs) {
    if (xs.nil()) return xs;
    const same = new List(xs.head());
    same.lazyRest = () => xs.tail().append(same);
    same.inf = true;
    return same;
  }

  static replicate(n, x) {
    return List.repeat(x).take(n);
  }

  static iterate(fn, x) {
    return new List(x, () => List.iterate(fn, fn(x)), true);
  }

  static repeat(x) {
    const xs = new List(x);
    xs.lazyRest = () => xs;
    xs.inf = true;
    return xs;
  }

  static get FIB() {
    const fib = new List(0);
    fib.lazyRest = () =>
      new List(1, () => fib.zipWith((x, y) => x + y, fib.tail()));
    return fib;
  }

  static get PRIME() {
    const filterPrime = xs => {
      const p = xs.head();
      return new List(p, () => filterPrime(xs.tail().filter(x => x % p !== 0)));
    };
    return filterPrime(List.iterate(x => x + 1, 2));
  }

  static get PI() {
    const mult = (x, y) => x * y;
    const plus = (x, y) => x + y;
    const odd = List.iterate(x => x + 2, 1);
    const arctan = x => odd.map(y => Math.pow(x, y) / y);
    const a2 = arctan(1 / 2);
    const a3 = arctan(1 / 3);
    const s = a2.zipWith(plus, a3);
    const signs = List.cycle(List.fromList([1, -1]));
    return s
      .zipWith(mult, signs)
      .scanl(plus, 0)
      .map(x => x * 4);
  }

  constructor(value, lazyRest, inf = false) {
    this.value = value;
    this.lazyRest = lazyRest;
    this.rest = null;
    this.inf = inf;
  }

  nil() {
    return this === List.empty;
  }

  head() {
    return this.value;
  }

  tail() {
    if (this.nil()) return this;
    if (this.rest === null) this.rest = this.lazyRest();
    return this.rest;
  }

  last() {
    if (this.tail().nil()) return this.head();
    return this.tail().last();
  }

  init() {
    if (this.nil() || this.inf) return this;
    if (this.tail().nil()) return this.tail();
    return new List(this.head(), () => this.tail().init());
  }

  length(count = 0) {
    if (this.nil()) return count;
    return this.tail().length(count + 1);
  }

  get(index) {
    if (index === 0) return this.value;
    return this.tail().get(index - 1);
  }

  drop(n) {
    if (n <= 0 || this.nil()) return this;
    return this.tail().drop(n - 1);
  }

  take(n) {
    if (this.nil()) return this;
    if (n <= 0) return List.empty;
    return new List(this.head(), () => this.tail().take(n - 1));
  }

  cons(x) {
    return new List(x, () => this, this.inf);
  }

  append(xs) {
    if (this.inf) return this;
    if (this.nil()) return xs;
    return new List(this.head(), () => this.tail().append(xs), xs.inf);
  }

  slice(start = 0, end = Infinity) {
    return start > end
      ? List.empty
      : this.inf && !isFinite(end)
      ? this.drop(start)
      : this.drop(start).take(end - start);
  }

  map(fn) {
    if (this.nil()) return this;
    return new List(fn(this.head()), () => this.tail().map(fn), this.inf);
  }

  filter(pred) {
    if (this.nil()) return this;
    if (!pred(this.head())) return this.tail().filter(pred);
    return new List(this.head(), () => this.tail().filter(pred), this.inf);
  }

  reverse() {
    return this.foldl((xs, x) => xs.cons(x), List.empty);
  }

  any(pred) {
    if (this.nil()) return false;
    return pred(this.head()) || this.tail().any(pred);
  }

  all(pred) {
    if (this.nil()) return true;
    return pred(this.head()) && this.tail().all(pred);
  }

  the() {
    const v = this.head();
    const equals = x => x === v;
    if (!this.nil() && this.all(equals)) return v;
    return undefined;
  }

  findIndex(pred, index = 0) {
    if (this.nil()) return -1;
    if (pred(this.head())) return index;
    return this.tail().findIndex(pred, index + 1);
  }

  elemIndex(x) {
    return this.findIndex(y => y === x);
  }

  elem(x) {
    return this.elemIndex(x) !== -1;
  }

  find(pred) {
    if (this.nil()) return;
    if (pred(this.head())) return this.head();
    return this.tail().find(pred);
  }

  foldl(fn, x) {
    if (this.nil()) return x;
    return this.tail().foldl(fn, fn(x, this.head()));
  }

  foldr(fn, x) {
    if (this.nil()) return x;
    if (this.inf) return fn(x || this.head());
    return fn(this.head(), this.tail().foldr(fn, x));
  }

  scanl(fn, x) {
    if (this.nil()) return this.cons(x);
    return new List(
      x,
      () => this.tail().scanl(fn, fn(x, this.head())),
      this.inf
    );
  }

  scanr(fn, x) {
    if (this.nil()) return this.cons(x);
    const list = this.tail().scanr(fn, x);
    const y = fn(this.head(), list.head());
    return list.cons(y);
  }

  zipWith(fn, xs) {
    if (this.nil()) return this;
    if (xs.nil()) return xs;
    return new List(
      fn(this.head(), xs.head()),
      () => this.tail().zipWith(fn, xs.tail()),
      this.inf && xs.inf
    );
  }

  concatMap(fn) {
    if (this.nil()) return this;
    const head = fn(this.head());
    if (head.inf) return head;
    if (head.nil()) return this.tail().concatMap(fn);
    return new List(head.head(), () =>
      head.tail().append(this.tail().concatMap(fn))
    );
  }

  concat() {
    const id = x => x;
    return this.concatMap(id);
  }

  toList() {
    if (this.inf) return [];
    const xs = [];
    let it = this;
    while (!it.nil()) {
      xs.push(it.value);
      it = it.tail();
    }
    return xs;
  }
}

List.empty = new List(undefined, null);

// ...
class EmptyList {
  all(f) { return true; }
  any(f) { return false; }
  append(xs) { return xs; }
  concat() { return this; }
  concatMap(f) { return this; }
  cons(x) { return Cons(x, () => this); }
  drop(n) { return this; }
  elem(x) { return false; }
  elemIndex(x) { return -1; }
  filter(f) { return this; }
  find(f) { return undefined; }
  findIndex(f) { return -1; }
  foldl(f, x) { return x; }
  foldr(f, x) { return x; }
  get(i) { return undefined; }
  head() { return undefined; }
  init() { return this; }
  last() { return undefined; }
  length() { return 0; }
  map(f) { return this; }
  nil() { return true; }
  reverse() { return this; }
  scanl(f, x) { return Cons(x, () => this); }
  scanr(f, x) { return Cons(x, () => this); }
  slice(i, j) { return this; }
  tail() { return this; }
  take(n) { return this; }
  the() { return undefined; }
  toList() { return []; }
  zipWith(f, xs) { return this; }
}

class LazyList {
  constructor(first, rest) {
    this.first = first;
    this.rest = rest;
  }

  singleton() { return this.tail() == Nil; }
  head() { return this.first; }
  tail() { return this.rest(); }
  init() { return this.singleton() ? Nil : Cons(this.head(), () => this.tail().init()); }
  last() { return this.singleton() ? this.head() : this.tail().last(); }
  length() { return 1 + this.tail().length(); }
  toList() { return [this.head()].concat(this.tail().toList()); }
  get(i) { return (i == 0) ? this.head() : this.tail().get(i-1); }
  nil() { return false; }
  take(n) { return (n <= 0) ? Nil : Cons(this.head(), () => this.tail().take(n-1)); }
  drop(n) { return (n <= 0) ? this : this.tail().drop(n-1); }
  cons(x) { return Cons(x, () => this); }
  append(xs) { return Cons(this.head(), () => this.tail().append(xs)); }
  slice(i=0, j=-1) {
    if (j > i) return this.drop(i).take(j-i);
    else if (j >= 0) return Nil;
    else return this.drop(i);
  }
  map(f) { return Cons(f(this.head()), () => this.tail().map(f)); }
  filter(f) { return f(this.head()) ? Cons(this.head(), () => this.tail().filter(f)) : this.tail().filter(f); }
  reverse() { return List.fromList(this.toList().reverse()); }
  concat() { return this.head().nil() ? this.tail().concat() : Cons(this.head().head(), () => this.tail().cons(this.head().tail()).concat()); }
  concatMap(f) { return this.map(f).concat(); }
  zipWith(f, xs) { return (xs == Nil) ? Nil : Cons(f(this.head(), xs.head()), () => this.tail().zipWith(f, xs.tail())); }
  foldr(f, x) { return (f.length <= 1) ? f(this.head()) : f(this.head(), this.tail().foldr(f, x)); }
  foldl(f, x) { return this.tail().foldl(f, f(x, this.head())); }
  scanr(f, x) { return this.reverse().scanl((a, b) => f(b, a), x).reverse(); }
  scanl(f, x) { return Cons(x, () => this.tail().scanl(f, f(x, this.head()))); }
  elem(x) { return this.head() == x || this.tail().elem(x); }
  elemIndex(x) {
    if (this.head() == x) return 0;
    var t = this.tail().elemIndex(x);
    if (t == -1) return -1;
    else return 1 + t;
  }
  find(f) { return f(this.head()) ? this.head() : this.tail().find(f); }
  findIndex(f) {
    if (f(this.head())) return 0;
    var t = this.tail().findIndex(f);
    if (t == -1) return -1;
    else return 1 + t;
  }
  any(f) { return f(this.head()) || this.tail().any(f); }
  all(f) { return f(this.head()) && this.tail().all(f); }
  the() {
    if (this.singleton()) return this.head();
    if (this.tail().head() != this.head()) return undefined;
    return this.head() == this.tail().the() ? this.head() : undefined;
  }
}

var Cons = (first, rest) => new LazyList(first, rest);
var Nil = new EmptyList();
var List = {};  

List.empty = new EmptyList();
List.fromList = function(l) {
  if (l.length == 0) return Nil;
  return Cons(l[0], () => List.fromList(l.slice(1)));
};
List.repeat = function(x) {
  var ordinary = Cons(x, () => Nil);
  ordinary.tail = function() { return ordinary; };
  return ordinary;
};
List.iterate = function(f, x) {
  var ordinary = Cons(x, () => Nil);
  ordinary.tail = function() { return List.iterate(f, f(x)); };
  return ordinary;
};
List.copy = function(xs) {
  if (xs == Nil) return Nil;
  var ordinary = Cons(xs.head(), () => undefined);
  ordinary.tail = function() { return List.copy(xs.tail()); };
  return ordinary;
};

function wrap(node, xs) {
  var oldtail = node.tail;
  node.tail = (function(xs) { return function() {
    if (oldtail() == Nil) return List.cycle(xs);
    else return wrap(oldtail(), xs);
  };})(xs);
  return node;
}

List.cycle = function(xs) {
  return wrap(List.copy(xs), xs);
};

List.replicate = function(n, x) {
  if (n == 0) return Nil;
  return Cons(x, () => List.replicate(n-1, x));
};

var nextFib = ([a, b]) => [b, a+b];
List.FIB = List.iterate(nextFib, [0, 1]).map(pair => pair[0]);

/*
arctan(x) can be written as an infinite sum 0 + x^1/1 - x^3/3 + x^5/5 - x^7/7 ..
π is equal to 4 * ( arctan(1/2) + arctan(1/3) )
*/

var mul = (a, b) => a * b;
var plus = (a, b) => a + b;
var plusMinus = List.cycle(List.fromList([1, -1]));
var odds = List.iterate(a => a + 2, 1);
var oddDenom = odds.map(x => 1/x);
var alternatingSignOddDenom = oddDenom.zipWith(mul, plusMinus);
var oddPowers = (x) => List.iterate(a => a * x * x, x);
var arctan = (x) => oddPowers(x).zipWith(mul, alternatingSignOddDenom).scanl(plus, 0);
List.PI = arctan(1/2).zipWith(plus, arctan(1/3)).map(x => x * 4);

/*
filterPrime [2..] where
filterPrime (p:xs) = p : filterPrime [x | x <- xs, x `mod` p /= 0]
*/

function primes(list) {
  var p = list.head();
  return Cons(p, () => primes(list.filter(x => x % p != 0)));
}

List.PRIME = primes(List.iterate(x => x+1, 2));

// ...
class List {
  constructor(fn) {
    this.fn = fn;
  }

  static get empty() {
    //return an empty list
    return new List(function* () {});
  }

  static get PRIME() {
    // start with List of each positive number greater than one
    // for each element in list, filter:
    // all( x % (List.iterate(y=>y+1, 2).take(x-2))  !==  0)
    return List.iterate(x => x + 1, 3)
      .filter(x => {
        return List.iterate(y => y + 1, 2)
          .take(x - 2)
          .all(y => x % y !== 0);
      })
      .cons(2);
  }

  static get FIB() {
    return new List(function* () {
      let a = 0;
      let b = 1;
      while (true) {
        yield a;
        yield b;
        a += b; // -> 1 -> 3 -> ...
        b += a; // -> 2 -> 5 -> ...
      }
    });
  }

  static get PI() {
    return new List(function* () {
      let pi = 0;
      yield pi;
      let i = 1;
      let sign = 4;
      while (true) {
        pi += (sign * (Math.pow(1 / 2, i) + Math.pow(1 / 3, i))) / i;
        yield pi;
        i += 2;
        sign *= -1;
      }
    });
  }

  static arctan(value) {
    //yields the expansion of arctan(value)
    return List.iterate(x => x + 1, 0) //get the values 0 to inf
      .filter(x => x % 2 == 1) // take only the odd values
      .map(x => Math.pow(value, x) / x) //nth term: x^n/n
      .zipWith((x, y) => x * y, List.cycle(List.fromList([1, -1]))); //alternate positive and negative
  }

  // Class methods ////////////////////////////
  static repeat(value) {
    //infinitely repeat the supplied value
    return List.replicate(Infinity, value);
  }

  static iterate(fn, value) {
    //infinitely apply the supplied function to the supplied value, returning the value
    return new List(function* () {
      let next = value; //init to the starting value
      while (true) {
        yield next;
        next = fn(next);
      }
    });
  }

  static fromList(list) {
    //copies a List, or converts an Array to a List
    if (list instanceof List) {
      return new List(list.fn);
    } else if (list instanceof Array) {
      return new List(function* () {
        let i = 0;
        while (i < list.length) {
          yield list[i];
          i += 1;
        }
      });
    }
  }

  static cycle(list) {
    return new List(function* () {
      let fn;
      while (true) {
        fn = list.fn();
        let next = fn.next();
        while (!next.done) {
          yield next.value;
          next = fn.next();
        }
      }
    });
  }

  static replicate(count, value) {
    return new List(function* () {
      let i = 0;
      while (i < count) {
        i += 1;
        yield value;
      }
    });
  }

  // Instance methods /////////////////////////
  take(count) {
    let fn = function* () {
      let i = 0;
      let fn = this.fn();
      let next = fn.next();
      while (i < count && !next.done) {
        yield next.value;
        next = fn.next();
        i += 1;
      }
    };
    return new List(fn.bind(this));
  }

  head() {
    // return new List(this.fn, this.start, this.start + 1).toList()[0];
    return this.take(1).toList()[0];
  }

  tail() {
    return this.drop(1);
  }

  init() {
    let fn = function* () {
      let fn = this.fn();
      let prev = fn.next(); // if done, no yield;
      let next = fn.next();
      while (!prev.done) {
        if (!next.done) {
          yield prev.value;
        }
        prev = next;
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  last() {
    return this.get(this.length() - 1);
  }

  get(i) {
    return this.drop(i).head();
  }

  drop(count) {
    let fn = function* () {
      let i = 0;
      let fn = this.fn();
      let next = fn.next();
      while (!next.done) {
        if (i < count) {
          i += 1;
        } else {
          yield next.value;
        }
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  length() {
    return this.toList().length;
  }

  nil() {
    return this.all(x => x === undefined);
  }

  cons(value) {
    let fn = function* () {
      yield value; //prepend the value

      let fn = this.fn();
      let next = fn.next();
      while (!next.done) {
        yield next.value;
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  append(list) {
    let fn = function* () {
      let fn = this.fn();
      let next = fn.next();
      while (!next.done) {
        yield next.value;
        next = fn.next();
      }
      fn = list.fn();
      next = fn.next();
      while (!next.done) {
        yield next.value;
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  slice(i = 0, j = Infinity) {
    if (i >= j) {
      return List.empty;
    } else {
      return this.drop(i).take(j - i);
    }
  }

  map(mapFn) {
    let fn = function* () {
      let fn = this.fn();
      let next = fn.next();
      while (!next.done) {
        yield mapFn(next.value);
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  filter(filt) {
    let fn = function* () {
      let fn = this.fn();
      let next = fn.next();
      while (!next.done) {
        if (filt(next.value)) {
          yield next.value;
        }
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  reverse() {
    return List.fromList(this.toList().reverse());
  }

  concat() {
    let fn = function* () {
      let fnOuter = this.fn();
      let nextOuter = fnOuter.next();
      let fnInner;
      let nextInner;
      while (!nextOuter.done) {
        fnInner = nextOuter.value.fn();
        nextInner = fnInner.next();
        while (!nextInner.done) {
          yield nextInner.value;
          nextInner = fnInner.next();
        }
        nextOuter = fnOuter.next();
      }
    };
    return new List(fn.bind(this));
  }

  concatMap(mapFn) {
    return this.map(mapFn).concat();
  }

  zipWith(mapFn, list) {
    let fn = function* () {
      let fn1 = this.fn();
      let fn2 = list.fn();
      let next1 = fn1.next(); //evaluate the parent list
      let next2 = fn2.next(); //evaluate the daughter list simultaneously
      while (!next1.done && !next2.done) {
        yield mapFn(next1.value, next2.value); //apply the function to the list results
        next1 = fn1.next();
        next2 = fn2.next();
      }
    };
    return new List(fn.bind(this));
  }

  foldr(foldFn, value) {
    let fn = this.fn();
    let next = fn.next();
    if (next.done) {
      return value;
    }
    //assess how many arguments are expected
    if (foldFn.length === undefined) {
      return foldFn;
    } else if (foldFn.length === 0) {
      return foldFn();
    } else if (foldFn.length === 1) {
      return foldFn(this.get(0));
    }

    let inner = () => {
      next = fn.next();
      if (next.done) {
        return value;
      } else {
        return foldFn(next.value, inner());
      }
    };
    return foldFn(next.value, inner());
  }

  foldl(foldFn, value) {
    let fn = this.fn();
    let next = fn.next();

    let inner = lastVal => {
      next = fn.next();
      if (next.done) {
        return lastVal;
      } else {
        return inner(foldFn(lastVal, next.value));
      }
    };
    // if next.done
    return inner(foldFn(value, next.value));
  }

  scanr(scanFn, value) {
    let fn = function* () {
      let fn1 = this.fn();
      let next1 = fn1.next();
      let i = 0;

      while (!next1.done) {
        let fn2 = this.fn();
        let next2 = fn2.next();
        let j = 0;
        while (j < i) {
          //throw away the values at the beginning
          next2 = fn2.next();
          j += 1;
        }
        let inner = () => {
          next2 = fn2.next();
          if (next2.done) {
            return value;
          } else {
            return scanFn(next2.value, inner());
          }
        };
        yield scanFn(next2.value, inner());
        i += 1;
        next1 = fn1.next();
      }

      yield value;
    };
    return new List(fn.bind(this));
  }

  scanl(scanFn, value) {
    let fn = function* () {
      let result = value;
      yield result;

      let fn = this.fn();
      let next = fn.next();

      while (!next.done) {
        result = scanFn(result, next.value);
        yield result;
        next = fn.next();
      }
    };
    return new List(fn.bind(this));
  }

  elem(value) {
    return this.elemIndex(value) !== -1;
  }

  elemIndex(value) {
    return this.findIndex(x => x === value);
  }

  find(findFn) {
    let ind = this.findIndex(findFn);
    if (ind === -1) {
      return undefined;
    } else {
      return this.get(ind);
    }
  }

  findIndex(findFn) {
    let i = 0;
    let fn = this.fn();
    let next = fn.next();
    while (!next.done) {
      if (findFn(next.value)) {
        return i;
      } else {
        next = fn.next();
        i += 1;
      }
    }
    return -1;
  }

  any(findFn) {
    return this.findIndex(findFn) !== -1;
  }

  all(findFn) {
    let fn = this.fn();
    let next = fn.next();
    while (!next.done) {
      if (!findFn(next.value)) {
        return false;
      }
      next = fn.next();
    }
    return true;
  }

  the() {
    let head = this.head();
    let fn = this.fn();
    let next = fn.next();
    while (!next.done) {
      if (head !== next.value) {
        return undefined;
      }
      next = fn.next();
    }
    return head;
  }

  toList() {
    // let result = [];
    let result = new Array(0);
    const fn = this.fn();
    let next = fn.next();
    while (!next.done) {
      result.push(next.value);
      next = fn.next();
    }
    return result;
  }
}

module.exports = List;

// ...
// ***************
//   Expressions
// ***************

// Expression

class Expression {
  constructor() {
    this.up = null;
    this.left = this;
    this.right = this;
  }
  enumerator() {
    throw Errors.ErrorAssertImplemented('enumerator');
  }
  cloneTree() {
    return new ExpressionCloner(this).cloneTree();
  }
  clone() {
    const other = new Expression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    this.up = exp.up;
    this.left = exp.left;
    this.right = exp.right;
  }
  evaluate() {
    return this.enumerator().collect();
  }
  addBefore(exp) {
    exp.right = this;
    exp.left = this.left;
    this.left.right = exp;
    this.left = exp;
    exp.up = this.up;
    if (this.up != null && this.up.down == this) this.up.down = exp;
  }
  addAfter(exp) {
    exp.left = this;
    exp.right = this.right;
    this.right.left = exp;
    this.right = exp;
    exp.up = this.up;
  }
  addUp(exp) {
    this.replace(exp);
    exp.addLast(this);
  }
  replace(exp) {
    this.left.right = exp;
    this.right.left = exp;
    exp.left = this.left;
    exp.right = this.right;
    this.right = this;
    this.left = this;
    if (this.up != null) {
      if (this.up.down == this) this.up.down = exp;
      exp.up = this.up;
      this.up = null;
    }
  }
  remove() {
    const right = this.right;
    this.left.right = this.right;
    this.right.left = this.left;
    this.right = this;
    this.left = this;
    if (this.up != null) {
      if (this.up.down == this) this.up.down = right;
      this.up = null;
    }
  }
  toString() {
    return 'Expression';
  }
}

class Enumerator {
  constructor(exp) {
    this.exp = exp;
  }
  moveNext() {
    throw Errors.ErrorAssertImplemented('moveNext');
  }
  reset() {
    throw Errors.ErrorAssertImplemented('reset');
  }
  current() {
    throw Errors.ErrorAssertImplemented('current');
  }
  collect() {
    return [...this.enumerate()];
  }
  *enumerate() {
    while (this.moveNext()) {
      yield this.current();
    }
  }
}

// Content Expression

class ContentExpression extends Expression {
  constructor(content) {
    super();
    this.content = content;
  }
  clone() {
    const other = new ContentExpression(this.content);
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.content = exp.content;
  }
  enumerator() {
    return new ContentEnumerator(this);
  }
  evaluate() {
    return this.content;
  }
  toString() {
    return `ContentExpression: ${this.content}`;
  }
}

class ContentEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.index == 0) return false;
    this.index++;
    return true;
  }
  reset() {
    this.index = -1;
  }
  current() {
    if (this.index == -1) throw Errors.ErrorEnumeratorReset;
    return this.exp.content;
  }
}

// Container Expression

class ContainerExpression extends Expression {
  constructor() {
    super();
    this.down = null;
  }
  clone() {
    const other = new ContainerExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.down = exp.down;
  }
  enumerator() {
    return new ContainerEnumerator(this);
  }
  addFirst(exp) {
    if (this.down == null) {
      this.down = exp;
      exp.up = this;
    } else {
      this.down.addBefore(exp);
    }
  }
  addLast(exp) {
    if (this.down == null) {
      this.down = exp;
      exp.up = this;
    } else {
      this.down.left.addAfter(exp);
    }
  }
  addDown(exp) {
    const first = this.down;
    exp.up = this;
    this.down = exp;
    if (first == null) return;
    let child = first;
    do {
      child.up = exp;
      child = child.right;
    } while (child != first);
    if (exp.down == null) exp.down = first;
  }
  implode() {
    if (this.up == null) return;
    const left = this.left;
    const right = this.right;
    const up = this.up;
    const upDown = up.down;
    const first = this.down;
    const last = first == null ? null : first.left;
    this.remove();
    if (first == null) return;
    let child = first;
    do {
      child.up = up;
    } while (child != first);
    if (upDown == this) up.down = first;
    if (left != this) {
      left.right = first;
      first.left = left;
    }
    if (right != this) {
      right.left = last;
      last.right = right;
    }
  }
  toString() {
    return 'ContainerExpression';
  }
}

class ContainerEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.child == null) {
      this.child = this.exp.down;
      if (this.child == null) return false;
      this.childE = this.child.enumerator();
    }
    while (true) {
      if (this.childE.moveNext()) return true;
      this.childE.reset();
      this.child = this.child.right;
      if (this.child == this.exp.down) return false;
      this.childE = this.child.enumerator();
    }
  }
  reset() {
    if (this.childE != null) this.childE.reset();
    this.child = null;
    this.childE = null;
  }
  current() {
    if (this.childE == null) throw Errors.ErrorEnumeratorReset;
    return this.childE.current();
  }
}

// Slice Expression

class SliceExpression extends ContainerExpression {
  constructor(from = 0, to = null) {
    super();
    this.from = from;
    this.to = to;
  }
  clone() {
    const other = new SliceExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.from = exp.from;
    this.to = exp.to;
  }
  enumerator() {
    return new SliceEnumerator(this);
  }
  toString() {
    return 'SliceExpression';
  }
}

class SliceEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null)
      this.containerE = new ContainerEnumerator(this.exp);
    if (this.exp.to != null) {
      if (this.exp.from >= this.exp.to) return false;
    }
    while (this.index < this.exp.from) {
      if (!this.containerE.moveNext()) return false;
      this.index++;
      if (this.index == this.exp.from) return true;
    }
    if (this.exp.to != null) {
      if (this.index + 1 >= this.exp.to) return false;
    }
    if (!this.containerE.moveNext()) return false;
    this.index++;
    return true;
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
    this.index = -1;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.containerE.current();
  }
}

// Map Expression

class MapExpression extends ContainerExpression {
  constructor(selector) {
    super();
    this.selector = selector;
  }
  clone() {
    const other = new MapExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.selector = exp.selector;
  }
  enumerator() {
    return new MapEnumerator(this);
  }
  toString() {
    return 'MapExpression';
  }
}

class MapEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null)
      this.containerE = new ContainerEnumerator(this.exp);
    return this.containerE.moveNext();
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.exp.selector(this.containerE.current());
  }
}

// Filter Expression

class FilterExpression extends ContainerExpression {
  constructor(predicate) {
    super();
    this.predicate = predicate;
  }
  clone() {
    const other = new FilterExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.predicate = exp.predicate;
  }
  enumerator() {
    return new FilterEnumerator(this);
  }
  toString() {
    return 'FilterExpression';
  }
}

class FilterEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null)
      this.containerE = new ContainerEnumerator(this.exp);
    if (!this.containerE.moveNext()) return false;
    while (!this.exp.predicate(this.current())) {
      if (!this.containerE.moveNext()) return false;
    }
    return true;
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.containerE.current();
  }
}

// Reverse Expression

class ReverseExpression extends ContainerExpression {
  constructor() {
    super();
  }
  clone() {
    const other = new ReverseExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
  }
  enumerator() {
    return new ReverseEnumerator(this);
  }
  toString() {
    return 'ReverseExpression';
  }
}

class ReverseEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
    this.items = null;
    this.index = -1;
  }
  moveNext() {
    if (this.child == null) {
      this.child = this.exp.down;
      if (this.child == null) return false;
      this.child = this.child.left;
      this.childE = this.child.enumerator();
    }
    while (true) {
      if (this.items == null) {
        this.items = [];
        this.index = -1;
        while (this.childE.moveNext())
          this.items.unshift(this.childE.current());
      }
      if (this.index + 1 < this.items.length) {
        this.index++;
        return true;
      }
      this.childE.reset();
      this.child = this.child.left;
      if (this.child == this.exp.down.left) return false;
      this.childE = this.child.enumerator();
      this.items = null;
      this.index = -1;
    }
  }
  reset() {
    if (this.childE != null) this.childE.reset();
    this.child = null;
    this.childE = null;
    this.items = null;
    this.index = -1;
  }
  current() {
    if (this.items == null) throw Errors.ErrorEnumeratorReset;
    return this.items[this.index];
  }
}

// Concat Expression

class ConcatExpression extends ContainerExpression {
  constructor() {
    super();
  }
  clone() {
    const other = new ConcatExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
  }
  enumerator() {
    return new ConcatEnumerator(this);
  }
  toString() {
    return 'ConcatExpression';
  }
}

class ConcatEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  getEnumerator(exp) {
    let descendant = exp;
    if (descendant instanceof MutableListExpression) descendant = exp.down;
    else descendant = exp;
    return descendant.enumerator();
  }
  getItems(exp, e) {
    this.items = [];
    let item = e.current();
    if (Array.isArray(item)) {
      this.items = item;
    } else if (item instanceof List) {
      this.defferedE = item.exp.down.enumerator();
    } else {
      this.items.push(item);
    }
  }
  moveNext() {
    if (this.child == null) {
      this.child = this.exp.down;
      if (this.child == null) return false;
      this.childE = this.getEnumerator(this.child);
    }
    while (true) {
      if (this.items == null) {
        this.index = -1;
        if (this.childE.moveNext()) {
          this.getItems(this.child, this.childE);
        } else {
          while (true) {
            this.childE.reset();
            this.child = this.child.right;
            if (this.child == this.exp.down) return false;
            this.childE = this.getEnumerator(this.child);
            if (this.childE.moveNext()) {
              this.getItems(this.child, this.childE);
              break;
            }
          }
        }
      }
      if (this.index + 1 < this.items.length) {
        this.index++;
        return true;
      } else {
        if (this.defferedE != null) {
          if (this.defferedE.moveNext()) {
            this.items = [];
            this.items.push(this.defferedE.current());
            this.index = 0;
            return true;
          } else {
            this.defferedE.reset();
            this.items = null;
            this.index = -1;
          }
        } else {
          this.items = null;
          this.index = -1;
        }
      }
    }
  }
  reset() {
    if (this.childE != null) this.childE.reset();
    if (this.defferedE != null) this.defferedE.reset();
    this.child = null;
    this.childE = null;
    this.defferedE = null;
    this.items = null;
    this.index = -1;
  }
  current() {
    if (this.items == null) throw Errors.ErrorEnumeratorReset;
    return this.items[this.index];
  }
}

// Zip Expression

class ZipExpression extends ContainerExpression {
  constructor(selector, otherExp) {
    super();
    this.selector = selector;
    this.otherExp = otherExp;
  }
  clone() {
    const other = new ZipExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.selector = exp.selector;
    this.otherExp = exp.otherExp.cloneTree();
  }
  enumerator() {
    return new ZipEnumerator(this);
  }
  toString() {
    return 'ZipExpression';
  }
}

class ZipEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null) {
      this.containerE = new ContainerEnumerator(this.exp);
      this.otherContainerE = new ContainerEnumerator(this.exp.otherExp);
    }
    return this.containerE.moveNext() && this.otherContainerE.moveNext();
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    if (this.otherContainerE != null) this.otherContainerE.reset();
    this.containerE = null;
    this.otherContainerE = null;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.exp.selector(
      this.containerE.current(),
      this.otherContainerE.current()
    );
  }
}

// Scan Right Expression

class ScanRightExpression extends ContainerExpression {
  constructor(reducer, seed) {
    super();
    this.reducer = reducer;
    this.seed = seed;
  }
  clone() {
    const other = new ScanRightExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.reducer = exp.reducer;
    this.seed = exp.seed;
  }
  enumerator() {
    return new ScanRightEnumerator(this);
  }
  toString() {
    return 'ScanRightExpression';
  }
}

class ScanRightEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null) {
      this.index = 0;
      this.items = [];
      let x = this.exp.seed;
      let fn = this.exp.reducer;
      if (false) {
        // BONUS: #2
        /*if (fn.length == 0) {
        if (x === undefined)
          this.items.unshift(fn());
        else
          this.items.unshift(x);
      } else if (fn.length == 1) {
        this.containerE = new ReverseEnumerator(this.exp);
        if (x === undefined && e.moveNext())
          this.items.unshift(e.current());
        else
          this.items.unshift(x);*/
      } else {
        this.items.unshift(x);
        this.containerE = new ReverseEnumerator(this.exp);
        while (this.containerE.moveNext()) {
          x = fn(this.containerE.current(), x);
          this.items.unshift(x);
        }
      }
      return true;
    }
    if (this.index + 1 >= this.items.length) return false;
    this.index++;
    return true;
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
    this.item = null;
    this.index = -1;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.items[this.index];
  }
}

// Scan Left Expression

class ScanLeftExpression extends ContainerExpression {
  constructor(reducer, seed) {
    super();
    this.reducer = reducer;
    this.seed = seed;
  }
  clone() {
    const other = new ScanLeftExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.reducer = exp.reducer;
    this.seed = exp.seed;
  }
  enumerator() {
    return new ScanLeftEnumerator(this);
  }
  toString() {
    return 'ScanLeftExpression';
  }
}

class ScanLeftEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null) {
      this.item = this.exp.seed;
      this.containerE = new ContainerEnumerator(this.exp);
      return true;
    }
    if (!this.containerE.moveNext()) return false;
    this.item = this.exp.reducer(this.item, this.containerE.current());
    return true;
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
    this.item = null;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.item;
  }
}

// Init Expression

class InitExpression extends ContainerExpression {
  constructor() {
    super();
  }
  clone() {
    const other = new InitExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
  }
  enumerator() {
    return new InitEnumerator(this);
  }
  toString() {
    return 'InitExpression';
  }
}

class InitEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null) {
      this.containerE = new ContainerEnumerator(this.exp);
      if (!this.containerE.moveNext()) return false;
      this.next = this.containerE.current();
      if (!this.containerE.moveNext()) return false;
      this.item = this.next;
      this.next = this.containerE.current();
    } else {
      if (!this.containerE.moveNext()) return false;
      this.item = this.next;
      this.next = this.containerE.current();
    }
    return true;
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
    this.item = null;
    this.next = null;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.item;
  }
}

// Repeat Expression

class RepeatExpression extends Expression {
  constructor(seed) {
    super();
    this.seed = seed;
  }
  clone() {
    const other = new RepeatExpression(this.seed);
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.seed = exp.seed;
  }
  enumerator() {
    return new RepeatEnumerator(this);
  }
  toString() {
    return 'RepeatExpression';
  }
}

class RepeatEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  getItem(exp) {
    this.item = exp.seed;
  }
  moveNext() {
    if (this.item == null) {
      this.getItem(this.exp);
    }
    return true;
  }
  reset() {
    this.item = null;
  }
  current() {
    if (this.item == null) throw Errors.ErrorEnumeratorReset;
    return this.item;
  }
}

// Iterate Expression

class IterateExpression extends Expression {
  constructor(selector, seed) {
    super();
    this.selector = selector;
    this.seed = seed;
  }
  clone() {
    const other = new IterateExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.selector = exp.selector;
    this.seed = exp.seed;
  }
  enumerator() {
    return new IterateEnumerator(this);
  }
  toString() {
    return 'IterateExpression';
  }
}

class IterateEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.item == null) {
      this.item = this.exp.seed;
    } else {
      this.item = this.exp.selector(this.item);
    }
    return true;
  }
  reset() {
    this.item = null;
  }
  current() {
    if (this.item == null) throw Errors.ErrorEnumeratorReset;
    return this.item;
  }
}

// Cyclic Expression

class CyclicExpression extends Expression {
  constructor(list) {
    super();
    this.list = list;
  }
  clone() {
    const other = new CyclicExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.list = exp.list.clone();
  }
  enumerator() {
    return new CyclicEnumerator(this);
  }
  toString() {
    return 'CyclicExpression';
  }
}

class CyclicEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.containerE == null)
      this.containerE = this.exp.list.exp.down.enumerator();
    if (!this.containerE.moveNext()) {
      if (this.has) {
        this.containerE.reset();
        this.has = false;
        this.containerE.moveNext();
      } else {
        return false;
      }
    } else {
      this.has = true;
    }
    return true;
  }
  reset() {
    if (this.containerE != null) this.containerE.reset();
    this.containerE = null;
    this.has = false;
  }
  current() {
    if (this.containerE == null) throw Errors.ErrorEnumeratorReset;
    return this.containerE.current();
  }
}

// Replicate Expression

class ReplicateExpression extends Expression {
  constructor(count, seed) {
    super();
    this.count = count;
    this.seed = seed;
  }
  clone() {
    const other = new ReplicateExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
    this.count = exp.count;
    this.seed = exp.seed;
  }
  enumerator() {
    return new ReplicateEnumerator(this);
  }
  toString() {
    return 'ReplicateExpression';
  }
}

class ReplicateEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.index + 1 >= this.exp.count) return false;
    this.index++;
    return true;
  }
  reset() {
    this.index = -1;
  }
  current() {
    if (this.index == -1) throw Errors.ErrorEnumeratorReset;
    return this.exp.seed;
  }
}

// Mutable List Expression

class MutableListExpression extends ContainerExpression {
  constructor(items) {
    super();
    this.addFirst(new ContainerExpression());
    if (items != null) {
      for (let item of items) {
        if (item instanceof Expression) {
          this.down.addLast(item);
        } else {
          this.down.addLast(new ContentExpression(item));
        }
      }
    }
  }
  static get empty() {
    return new MutableListExpression([]);
  }
  static fromList(list) {
    return new MutableListExpression(list);
  }
  static repeat(n) {
    return MutableListExpression.fromExp(new RepeatExpression(n));
  }
  static iterate(fn, x) {
    return MutableListExpression.fromExp(new IterateExpression(fn, x));
  }
  static cycle(xs) {
    return MutableListExpression.fromExp(new CyclicExpression(xs));
  }
  static replicate(n, x) {
    return MutableListExpression.fromExp(new ReplicateExpression(n, x));
  }
  static fromExp(exp) {
    const list = new MutableListExpression();
    list.down.addDown(exp.cloneTree());
    return list;
  }
  clone() {
    const other = new MutableListExpression();
    other.copy(this);
    return other;
  }
  enumerator() {
    return new MutableListEnumerator(this);
  }
  evaluate() {
    return this.down.enumerator().collect();
  }
  toList() {
    return this.evaluate();
  }
  head() {
    const e = this.down.enumerator();
    if (!e.moveNext()) return undefined;
    return e.current();
  }
  tail() {
    this.down.addDown(new SliceExpression(1));
  }
  take(n) {
    this.down.addDown(new SliceExpression(0, n));
  }
  drop(n) {
    this.down.addDown(new SliceExpression(n));
  }
  slice(i, j) {
    this.down.addDown(new SliceExpression(i, j));
  }
  init() {
    this.down.addDown(new InitExpression());
  }
  length() {
    const e = this.down.enumerator();
    let i = 0;
    while (e.moveNext()) i++;
    return i;
  }
  nil() {
    const e = this.down.enumerator();
    return !e.moveNext();
  }
  get(index) {
    if (index < 0) return undefined;
    let i = 0;
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (index == i) return e.current();
      i++;
      if (i > index) return undefined;
    }
  }
  cons(item) {
    this.prepend(item);
  }
  prependRange(items) {
    if (items != null) {
      for (let item of items) {
        this.prepend(item);
      }
    }
  }
  prepend(item) {
    if (item instanceof MutableListExpression) {
      this.down.addFirst(item.down);
    } else if (item instanceof Expression) {
      this.down.addFirst(item);
    } else {
      this.down.addFirst(new ContentExpression(item));
    }
  }
  appendRange(items) {
    if (items != null) {
      for (let item of items) {
        this.append(item);
      }
    }
  }
  append(item) {
    if (item instanceof MutableListExpression) {
      this.down.addLast(item.down);
    } else if (item instanceof Expression) {
      this.down.addLast(item);
    } else {
      this.down.addLast(new ContentExpression(item));
    }
  }
  map(fn) {
    this.down.addDown(new MapExpression(fn));
  }
  filter(fn) {
    this.down.addDown(new FilterExpression(fn));
  }
  reverse() {
    this.down.addDown(new ReverseExpression());
  }
  concat() {
    this.down.addDown(new ConcatExpression());
  }
  concatMap(fn) {
    this.down.addDown(new MapExpression(fn));
    this.down.addDown(new ConcatExpression());
  }
  zipWith(fn, xs) {
    this.down.addDown(new ZipExpression(fn, xs.exp.down));
  }
  foldr(fn, x) {
    if (fn.length == 0) {
      if (x === undefined) return fn();
      return x;
    }
    const e = this.down.enumerator();
    if (fn.length == 1) {
      if (x === undefined && e.moveNext()) return fn(e.current());
      return x;
    }
    return fold();
    function fold() {
      if (!e.moveNext()) {
        return x;
      } else {
        return fn(e.current(), fold());
      }
    }
  }
  foldl(fn, x) {
    if (fn.length == 0) {
      if (x === undefined) return fn();
      return x;
    }
    const e = this.down.enumerator();
    let item = x;
    while (e.moveNext()) {
      item = fn(item, e.current());
    }
    return item;
  }
  scanr(fn, x) {
    this.down.addDown(new ScanRightExpression(fn, x));
  }
  scanl(fn, x) {
    this.down.addDown(new ScanLeftExpression(fn, x));
  }
  elem(x) {
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (e.current() === x) return true;
    }
    return false;
  }
  elemIndex(x) {
    let index = 0;
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (e.current() === x) return index;
      index++;
    }
    return -1;
  }
  find(fn) {
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (fn(e.current())) return e.current();
    }
    return undefined;
  }
  findIndex(fn) {
    let index = 0;
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (fn(e.current())) return index;
      index++;
    }
    return -1;
  }
  any(fn) {
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (fn(e.current())) return true;
    }
    return false;
  }
  all(fn) {
    const e = this.down.enumerator();
    while (e.moveNext()) {
      if (!fn(e.current())) return false;
    }
    return true;
  }
  the() {
    let item = undefined;
    const e = this.down.enumerator();
    if (!e.moveNext()) {
      return item;
    }
    item = e.current();
    while (e.moveNext()) {
      if (e.current() !== item) return undefined;
    }
    return item;
  }
  last() {
    const e = this.down.enumerator();
    let last = undefined;
    while (e.moveNext()) {
      last = e.current();
    }
    return last;
  }
  toString() {
    return 'MutableListExpression';
  }
}

class MutableListEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.items != null) return false;
    this.items = this.exp;
    return true;
  }
  reset() {
    this.items = null;
  }
  current() {
    if (this.items == null) throw Errors.ErrorEnumeratorReset;
    return this.items;
  }
}

// ***************
//     Tools
// ***************

class Errors {
  static ErrorAssertImplemented = operation => {
    return `Assertion error: '${operation}' must be implemented`;
  };
  static ErrorInvalidOperation = operation => {
    return `Invalid operation: ${operation}`;
  };
  static ErrorEnumeratorReset = Errors.ErrorInvalidOperation(
    'the enumerator has been reset'
  );
}

class ExpressionWalker {
  constructor(exp) {
    this.exp = exp;
  }
  *walk() {
    yield* this.dfs();
  }
  *dfs() {
    const stack = [];
    stack.push(this.exp);
    while (stack.length > 0) {
      let exp = stack.pop();
      yield exp;
      exp = exp.down;
      if (exp == null) continue;
      exp = exp.left;
      const last = exp;
      do {
        stack.push(exp);
        exp = exp.left;
      } while (exp != last);
    }
  }
}

class ExpressionPrinter {
  constructor(exp) {
    this.exp = exp;
  }
  print(projector, printer, indentationSelector) {
    this.dfs(projector, printer, indentationSelector);
  }
  dfs(projector, printer, indentationSelector) {
    if (projector == null) projector = exp => exp.toString();
    if (printer == null) printer = text => console.log(text);
    if (indentationSelector == null)
      indentationSelector = depth => '\t'.repeat(depth);
    const walker = new ExpressionWalker(this.exp);
    let prev = null;
    let depth = 0;
    for (let exp of walker.dfs()) {
      let text = null;
      if (prev != null && prev.right != exp) {
        if (prev.down == exp) {
          depth++;
        } else {
          let parent = exp;
          let currentDepth = 0;
          while (parent.up != null) {
            currentDepth++;
            parent = parent.up;
          }
          depth = currentDepth;
        }
      }
      text = indentationSelector(depth) + projector(exp);
      printer(text);
      prev = exp;
    }
  }
}

class ExpressionCloner {
  constructor(exp) {
    this.exp = exp;
  }
  cloneTree() {
    const map = [];
    const walker = new ExpressionWalker(this.exp);
    for (let exp of walker.walk()) {
      map.push({ source: exp, target: exp.clone() });
    }
    for (let pair of map) {
      const isContainer = pair.source instanceof ContainerExpression;
      const up = map.find(p => p.source === pair.source.up) || null;
      const left = map.find(p => p.source === pair.source.left) || null;
      const right = map.find(p => p.source === pair.source.right) || null;
      const down = isContainer
        ? map.find(p => p.source === pair.source.down) || null
        : null;
      pair.target.up = up != null ? up.target : null;
      pair.target.left = left != null ? left.target : null;
      pair.target.right = right != null ? right.target : null;
      if (isContainer) pair.target.down = down != null ? down.target : null;
    }
    return map.find(p => p.source === this.exp).target;
  }
}

class ExpressionMath {
  constructor() {}
  static PI() {
    return List.fromExp(new PIExpression());
  }
  static PRIME() {
    return List.fromExp(new PrimeExpression());
  }
  static FIB() {
    return List.fromExp(new FibonacciExpression());
  }
}

// PI Expression

class PIExpression extends Expression {
  constructor() {
    super();
  }
  clone() {
    const other = new PIExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
  }
  enumerator() {
    return new PIEnumerator(this);
  }
  toString() {
    return 'PIExpression';
  }
}

class PIEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.x == -1) {
      this.x = 0;
      return true;
    }
    if (this.x == 0) {
      this.x++;
    } else {
      this.x += 2;
      this.s = -this.s;
    }
    this.a += this.s * (Math.pow(1 / 2, this.x) / this.x);
    this.b += this.s * (Math.pow(1 / 3, this.x) / this.x);
    return true;
  }
  reset() {
    this.x = -1;
    this.a = 0;
    this.b = 0;
    this.s = 1;
  }
  current() {
    if (this.x == -1) throw Errors.ErrorEnumeratorReset;
    return 4 * (this.a + this.b);
  }
}

// Prime Expression

class PrimeExpression extends Expression {
  constructor() {
    super();
  }
  clone() {
    const other = new PrimeExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
  }
  enumerator() {
    return new PrimeEnumerator(this);
  }
  toString() {
    return 'PrimeExpression';
  }
}

class PrimeEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  isPrime() {
    for (let i = 2, s = Math.sqrt(this.prime); i <= s; i++)
      if (this.prime % i === 0) return false;
    return this.prime > 1;
  }
  moveNext() {
    this.prime++;
    while (!this.isPrime()) {
      this.prime++;
    }
    return true;
  }
  reset() {
    this.prime = 1;
  }
  current() {
    if (this.prime == 1) throw Errors.ErrorEnumeratorReset;
    return this.prime;
  }
}

// Fibonacci Expression

class FibonacciExpression extends Expression {
  constructor() {
    super();
  }
  clone() {
    const other = new FibonacciExpression();
    other.copy(this);
    return other;
  }
  copy(exp) {
    super.copy(exp);
  }
  enumerator() {
    return new FibonacciEnumerator(this);
  }
  toString() {
    return 'FibonacciExpression';
  }
}

class FibonacciEnumerator extends Enumerator {
  constructor(exp) {
    super(exp);
    this.reset();
  }
  moveNext() {
    if (this.items == null) {
      this.items = [];
      this.items.push(0);
      this.items.push(1);
    } else {
      let temp = this.items[0];
      this.items[0] = this.items[1];
      this.items[1] = this.items[0] + temp;
    }
    return true;
  }
  reset() {
    this.items = null;
  }
  current() {
    if (this.items == null) throw Errors.ErrorEnumeratorReset;
    return this.items[0];
  }
}

// **************
//      API
// **************

class List {
  constructor(items) {
    this.exp = new MutableListExpression();
    if (items != null) {
      for (let item of items) {
        if (item instanceof List) {
          this.exp.down.addLast(item.exp.cloneTree());
        } else if (item instanceof Expression) {
          this.exp.down.addLast(item.cloneTree());
        } else {
          this.exp.down.addLast(new ContentExpression(item));
        }
      }
    }
  }
  static get empty() {
    return new List([]);
  }
  static get PI() {
    return ExpressionMath.PI();
  }
  static get PRIME() {
    return ExpressionMath.PRIME();
  }
  static get FIB() {
    return ExpressionMath.FIB();
  }
  static fromList(list) {
    return new List(list);
  }
  static repeat(n) {
    return List.fromExp(new RepeatExpression(n));
  }
  static iterate(fn, x) {
    return List.fromExp(new IterateExpression(fn, x));
  }
  static cycle(xs) {
    return List.fromExp(new CyclicExpression(xs));
  }
  static replicate(n, x) {
    return List.fromExp(new ReplicateExpression(n, x));
  }
  static fromExp(exp) {
    const list = new List();
    list.exp.down.addDown(exp.cloneTree());
    new ExpressionPrinter(list.exp).print();
    return list;
  }
  clone() {
    const other = new List();
    other.copy(this);
    return other;
  }
  copy(list) {
    this.exp = list.exp.cloneTree();
  }
  enumerator() {
    return this.exp.down.enumerator();
  }
  toList() {
    return this.exp.toList();
  }
  head() {
    return this.exp.head();
  }
  tail() {
    const list = this.clone();
    list.exp.tail();
    return list;
  }
  take(n) {
    const list = this.clone();
    list.exp.take(n);
    return list;
  }
  drop(n) {
    const list = this.clone();
    list.exp.drop(n);
    return list;
  }
  slice(i, j) {
    const list = this.clone();
    list.exp.slice(i, j);
    return list;
  }
  init() {
    const list = this.clone();
    list.exp.init();
    return list;
  }
  length() {
    return this.exp.length();
  }
  nil() {
    return this.exp.nil();
  }
  get(index) {
    return this.exp.get(index);
  }
  cons(item) {
    return this.prepend(item);
  }
  prependRange(items) {
    if (items != null) {
      for (let item of items) {
        this.prepend(item);
      }
    }
  }
  prepend(item) {
    const list = this.clone();
    if (item instanceof List) {
      list.exp.prepend(item.exp.cloneTree());
    } else if (item instanceof MutableListExpression) {
      list.exp.prepend(item.down.cloneTree());
    } else if (item instanceof Expression) {
      list.exp.prepend(item.cloneTree());
    } else {
      list.exp.prepend(item);
    }
    return list;
  }
  appendRange(items) {
    if (items != null) {
      for (let item of items) {
        this.append(item);
      }
    }
  }
  append(item) {
    const list = this.clone();
    if (item instanceof List) {
      list.exp.append(item.exp.cloneTree());
    } else if (item instanceof MutableListExpression) {
      list.exp.append(item.down.cloneTree());
    } else if (item instanceof Expression) {
      list.exp.append(item.cloneTree());
    } else {
      list.exp.append(item);
    }
    return list;
  }
  map(fn) {
    const list = this.clone();
    list.exp.map(fn);
    return list;
  }
  filter(fn) {
    const list = this.clone();
    list.exp.filter(fn);
    return list;
  }
  reverse() {
    const list = this.clone();
    list.exp.reverse();
    return list;
  }
  concat() {
    const list = this.clone();
    list.exp.concat();
    return list;
  }
  concatMap(fn) {
    const list = this.clone();
    list.exp.concatMap(fn);
    return list;
  }
  zipWith(fn, xs) {
    const list = this.clone();
    list.exp.zipWith(fn, xs);
    return list;
  }
  foldr(fn, x) {
    return this.exp.foldr(fn, x);
  }
  foldl(fn, x) {
    return this.exp.foldl(fn, x);
  }
  scanr(fn, x) {
    const list = this.clone();
    list.exp.scanr(fn, x);
    return list;
  }
  scanl(fn, x) {
    const list = this.clone();
    list.exp.scanl(fn, x);
    return list;
  }
  elem(x) {
    return this.exp.elem(x);
  }
  elemIndex(x) {
    return this.exp.elemIndex(x);
  }
  find(fn) {
    return this.exp.find(fn);
  }
  findIndex(fn) {
    return this.exp.findIndex(fn);
  }
  any(fn) {
    return this.exp.any(fn);
  }
  all(fn) {
    return this.exp.all(fn);
  }
  the() {
    return this.exp.the();
  }
  last() {
    return this.exp.last();
  }
  toString() {
    return 'List';
  }
}
