// https://www.codewars.com/kata/5a4d303f880385399b000001/train/dart
// My solution
Iterable<int> digits(int number) sync* {
  while (number > 0) {
    yield number % 10;
    number = number ~/ 10;
  }
}

int factorial(int n) {
  var result = 1;
  while (n >= 2) {
    result = result * n;
    n--;
  }
  return result;
}

bool isStrong(int n) {
  var factorialSum = digits(n).map(factorial).reduce((x, y) => x + y);
  return factorialSum == n;
}

String strong(int n) => isStrong(n) ? "STRONG!!!!" : "Not Strong !!";

// ...
String strong(n) {
  final sum = n
      .toString()
      .split('')
      .map((num) => factorial(int.parse(num)))
      .fold(0, (a, b) => a + b);
  return n == sum ? "STRONG!!!!" : "Not Strong !!";
}

int factorial(int n) => n == 0 ? 1 : n * factorial(n - 1);

// ...
String strong(int n) {
  final num = n
      .toString()
      .split('')
      .map((digit) => int.parse(digit).factorial())
      .reduce((prev, current) => prev + current);

  return num == n ? 'STRONG!!!!' : 'Not Strong !!';
}

extension IntTool on int {
  int factorial() {
    if (this == 0) return 1;

    var result = 1;

    for (int i = 2; i <= this; i++) {
      result *= i;
    }

    return result;
  }
}
