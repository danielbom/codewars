// https://www.codewars.com/kata/58acfe4ae0201e1708000075/train/dart
// My solution
bool inviteMoreWomen(List<int> genders) {
  return genders.fold<int>(0, (x, y) => x + y) > 0;
}

// ...
bool inviteMoreWomen(List<int> l) {
  return l.reduce((a, b) => a + b) > 0;
}

// ...
bool inviteMoreWomen(List<int> l) => l.reduce((x, y) => x + y) > 0;
