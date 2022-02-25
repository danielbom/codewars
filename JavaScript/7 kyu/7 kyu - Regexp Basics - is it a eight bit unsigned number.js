// https://www.codewars.com/kata/567e8f7b4096f2b4b1000005/train/javascript
// My solution
String.prototype.eightBitNumber = function() {
  return /^[1-9]\d*$|^0$/.test(this) && parseInt(this) < 256;
}

// ...
String.prototype.eightBitNumber = function () {
  return String(+this) == this && +this >= 0 && +this <=255;
};