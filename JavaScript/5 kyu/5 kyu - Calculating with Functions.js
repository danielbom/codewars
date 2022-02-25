// https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/javascript
// My solution
const callWith = value => fn => typeof fn === "function" ? fn(value) : value;

const zero  = callWith(0);
const one   = callWith(1);
const two   = callWith(2);
const three = callWith(3);
const four  = callWith(4);
const five  = callWith(5);
const six   = callWith(6);
const seven = callWith(7);
const eight = callWith(8);
const nine  = callWith(9);

const plus      = b => a => a + b;
const minus     = b => a => a - b;
const times     = b => a => a * b;
const dividedBy = b => a => Math.floor(a / b);

// And
const callWithValue = value => (fn = null) => fn == null ? value : fn(value);
const callWithFn = fn => val1 => val2 => fn(val2, val1);

const zero = callWithValue(0);
const one = callWithValue(1);
const two = callWithValue(2);
const three = callWithValue(3);
const four = callWithValue(4);
const five = callWithValue(5);
const six = callWithValue(6);
const seven = callWithValue(7);
const eight = callWithValue(8);
const nine = callWithValue(9);

const plus = callWithFn((a, b) => a + b);
const minus = callWithFn((a, b) => a - b);
const times = callWithFn((a, b) => a * b);
const dividedBy = callWithFn((a, b) => Math.floor(a / b));

// ...
const
  id = x => x,
  number = x => (f = id) => f(x),
  [zero, one, two, three, four, five, six, seven, eight, nine] =
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map(number),
  plus = x => y => y + x,
  minus = x => y => y - x,
  times = x => y => y * x,
  dividedBy = x => y => y / x;

// ...
function zero(a) {if (a) return eval(0 + a); return 0}
function one(a) {if (a) return eval(1 + a); return 1}
function two(a) {if (a) return eval(2 + a); return 2}
function three(a) {if (a) return eval(3 + a); return 3}
function four(a) {if (a) return eval(4 + a); return 4}
function five(a) {if (a) return eval(5 + a); return 5}
function six(a) {if (a) return eval(6 + a); return 6}
function seven(a) {if (a) return eval(7 + a); return 7}
function eight(a) {if (a) return eval(8 + a); return 8}
function nine(a) {if (a) return eval(9 + a); return 9}

function plus(a) {return "+" + a}
function minus(a) {return "-" + a }
function times(a) {return "*" + a }
function dividedBy(a) {return "/" + a }

// ...
