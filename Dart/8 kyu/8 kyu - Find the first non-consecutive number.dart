// https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/dart
// My solution
int? firstNonConsecutive(List<int> arr) {
  if (arr.length <= 2) return null;

  var factor = 1;

  for (var i = 1; i < arr.length; i++) {
    if (arr[i] - arr[i - 1] != factor) {
      return arr[i];
    }
  }

  return null;
}

// ...
int? firstNonConsecutive(List<int> arr) {
  int s = arr.first;

  for (int i = 0; i < arr.length; i++) {
    if (arr[i] != s + i) {
      return arr[i];
    }
  }

  return null;
}
