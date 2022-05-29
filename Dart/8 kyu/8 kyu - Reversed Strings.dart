// https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/dart
// My solution
String solution(String str) {
  return str.codeUnits.reversed.map((code) => String.fromCharCode(code)).join();
}

// ...
String solution(str) {
  return str.split('').reversed.join('');
}

// ...
solution(str) => str.split('').reversed.join('');

// ...
String solution(String str) {
  return new String.fromCharCodes(str.runes.toList().reversed);
}
