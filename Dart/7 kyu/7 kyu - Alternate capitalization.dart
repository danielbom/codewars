// https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/dart
// My solution

List<String> capitalize(String text) {
  List<String> result = ["", ""];

  for (var i = 0; i < text.length; i++) {
    result[i % 2] += text[i].toUpperCase();
    result[(i + 1) % 2] += text[i].toLowerCase();
  }

  return result;
}

// ...
List<String> capitalize(String x) => [0, 1]
    .map((conversionRemainder) => x
        .split('')
        .asMap()
        .entries
        .map((entry) => entry.key % 2 == conversionRemainder
            ? entry.value.toUpperCase()
            : entry.value)
        .join())
    .toList();
