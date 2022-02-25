// https://www.codewars.com/kata/58334362c5637ad0bb0001c2/train/javascript
// My solution
const f = (I, V, X) =>
  ["(", I, X, "|", V, I, "{0,3}|", I, V, "|", I, "{1,3})?"].join("");
const _1 = f("I", "V", "X");
const _10 = f("X", "L", "C");
const _100 = f("C", "D", "M");
const _1000 = "(M{1,5})?";
const strict = r => "^" + r + "$";
const romanExpr = strict(_1000 + _100 + _10 + _1);
const regexValidRoman = new RegExp(romanExpr);

function validRoman(str) {
  return str.length > 0 && regexValidRoman.test(str);
}

function validRomans(arr) {
  return arr.filter(validRoman);
}

// ...
function validRomans(arr) {
  var regex = /^M{0,4}(C[DM]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$/;
  
  return arr.filter(x => x && regex.test(x));
}
