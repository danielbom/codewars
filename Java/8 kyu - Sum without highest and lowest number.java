// https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/java
// My solution
public class Kata {
    public static int sum(int[] numbers) {
        if(numbers == null || numbers.length <= 1) return 0;
        int min, max, sum = 0;
        min = max = numbers[0];
        for(int i = 0; i < numbers.length; i++) {
            if(min > numbers[i]) min = numbers[i];
            if(max < numbers[i]) max = numbers[i];
            sum += numbers[i];
        }
        return sum - min - max;
    }
}

// ...
import static java.util.stream.IntStream.of;
public class Kata {
    public static int sum(int[] numbers) {
        return (numbers == null || numbers.length <= 2) ? 0 : of(numbers).sum() - of(numbers).max().getAsInt() - of(numbers).min().getAsInt();
    }
}

// ...
public class Kata {
  public static int sum(int[] numbers) {
        if (numbers == null || numbers.length < 2) {
            return 0;
        }
        int lowest = numbers[0];
        int highest = numbers[0];
        int sum = 0;
        for (int i:numbers) {
            lowest = Math.min(lowest, i);
            highest = Math.max(highest, i);
            sum +=i;
        }
        return sum - lowest - highest;
    }
}

// ...
import java.util.Arrays;
public class Kata
{
    public static int sum(int[] numbers) {
        if (numbers == null || numbers.length < 2) return 0;
        return Arrays.stream(numbers).sorted().skip(1).limit(numbers.length - 2).sum();
    }
}