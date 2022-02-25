// https://www.codewars.com/kata/remove-exclamation-marks/train/csharp
// My solution
using System;

public class Kata {
  public static string RemoveExclamationMarks (string s) {
    return s.Replace ("!", "");
  }
}

// ...
using System;

public class Kata {
  public static string RemoveExclamationMarks (string s) {
    return string.IsNullOrEmpty (s) ? s : s.Replace ("!", "");
  }
}