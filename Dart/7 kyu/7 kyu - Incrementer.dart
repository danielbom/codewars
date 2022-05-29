// https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/dart
// My solution
List<int> incrementer(List<int> nums) {
  List<int> result = [];
  for (int i = 0; i < nums.length; i++) {
    result.add((nums[i] + i + 1) % 10);
  }
  return result;
}

// ...
List<int> incrementer(List<int> nums) {
  return nums.asMap().entries.map((e) => (e.value + e.key + 1) % 10).toList();
}

// ...
List<int> incrementer(List<int> nums) => Iterable<int>.generate(nums.length)
    .map((i) => (nums[i] + ++i) % 10)
    .toList();

// ...
List<int> incrementer(List<int> nums) =>
    [for (var i = 0; i < nums.length; i++) (nums[i] + i + 1) % 10];

// ...
List<int> incrementer(List<int> nums) {
  return List.generate(nums.length, (i) => (nums[i] + i + 1) % 10);
}
