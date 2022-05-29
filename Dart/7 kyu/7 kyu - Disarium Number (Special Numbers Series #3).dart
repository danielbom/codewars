// https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/dart
// My solution
import 'dart:math';

extension IntX on int {
  Iterable<int> digits() sync* {
    int n = this;
    while (n > 0) {
      yield n % 10;
      n = n ~/ 10;
    }
  }
}

bool isDisariumNumber(int n) {
  int i = 1;
  int sum = 0;
  n.digits().toList().reversed.forEach((d) {
    sum += pow(d, i).toInt();
    i++;
  });
  return sum == n;
}

String disariumNumber(int n) => isDisariumNumber(n) ? "Disarium !!" : "Not !!";

// ...
import 'dart:math';

String disariumNumber(n) {
  String sN = n.toString();
  int sum = 0;
  for(int i = 0; i < sN.length; ++i){
    sum += pow(int.parse(sN[i]), i+1);
  }
  return (sum == n) ? "Disarium !!" : "Not !!";
}

// ...
import 'dart:math';
String disariumNumber(int n) => n
            .toString()
            .split('')
            .asMap()
            .map((i, x) => MapEntry(i, pow(int.parse(x), i + 1)))
            .values
            .toList()
            .reduce((x, y) => x + y) ==
        n
    ? "Disarium !!"
    : "Not !!";