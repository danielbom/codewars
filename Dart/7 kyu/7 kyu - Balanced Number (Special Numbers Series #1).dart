// https://www.codewars.com/kata/5a4e3782880385ba68000018/train/dart
// My solution
String balancedNum(int num) {
  var numStr = num.toString();
  var middle = (numStr.length / 2).floor();

  if (numStr.length.isEven) middle -= 1;

  int sum = 0;
  for (var i = 0, j = numStr.length - 1; i < middle; i++, j--) {
    sum += int.parse(numStr[i]) - int.parse(numStr[j]);
  }

  return sum == 0 ? "Balanced" : "Not Balanced";
}

// ...
String balancedNum(numb) {
  final s = numb.toString().split('').map(int.parse).toList();
  final len = (s.length ~/ 2) - (s.length % 2 == 1 ? 0 : 1);
  return s.sublist(0, len).fold(0, (acc, item) => acc + item) ==
          s.sublist(s.length - len).fold(0, (acc, item) => acc + item)
      ? 'Balanced'
      : 'Not Balanced';
}

// ...
Iterable<int> digits(int n) sync* {
  while (n > 0) {
    yield n % 10;
    n = n ~/ 10;
  }
}

String balancedNum(int numb) {
  var d = digits(numb).toList();
  var t = (d.length - 1) ~/ 2;

  if (t == 0) return 'Balanced';

  return d.take(t).reduce((x, y) => x + y) ==
          d.reversed.take(t).reduce((x, y) => x + y)
      ? "Balanced"
      : "Not Balanced";
}
