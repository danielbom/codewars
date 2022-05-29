// https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/dart
// My solution
List<int> countBy(int x, int n) {
  return List.generate(n, (index) => (index + 1) * x);
}

// ...
List<int> countBy(int x, int n) {
  return [for (var i = 1; i <= n; i++) x * i];
}
