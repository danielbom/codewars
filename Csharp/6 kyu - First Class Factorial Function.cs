// https://www.codewars.com/kata/57a09ca2e298a75f3300013d/train/csharp
// My solution
namespace FunctionalFactorial {
  using System;
  public class Factorial
  {
    public static Func<int, int> GetFactorialFunction()
    {
      return (x) => {
        int result = 1;
        while (x > 0) result *= x--;
        return result;
      };
    }
  }
}

// ...
namespace FunctionalFactorial {
  using System;
  public class Factorial
  {
    public static Func<int, int> GetFactorialFunction()
    {
      int Factorial(int n) => n <= 0 ? 1 : n * Factorial(n - 1);
      return Factorial;
    }
  }
}