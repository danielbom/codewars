// https://www.codewars.com/kata/56d31aaefd3a52902a000d66/train/javascript
// My solution
function radLadies(name) {
  const match = name.toUpperCase().match(/[A-Z !]/g);
  return match && match.join("");
}
