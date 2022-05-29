// https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/dart
// My solution
import 'dart:math';

List<int> evenNumbers(List<int> arr, int n) {
  var evens = arr.where((it) => it.isEven).toList();
  return evens.sublist(max(evens.length - n, 0));
}
