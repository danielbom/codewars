// https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/java
// My solution
public class Kata {
    public static int[] digitize(long n) {
        String string = String.valueOf(n);
        int[] array = new int[string.length()];
        int strLength = string.length();
        for(int i = strLength; i > 0 ; i--)
            array[strLength - i] = Character.getNumericValue(string.charAt(i - 1));
        return array;
    }
}

// ...
public class Kata {
    public static int[] digitize(long n) {
        return new StringBuilder().append(n)
                                .reverse()
                                .chars()
                                .map(Character::getNumericValue)
                                .toArray();
    }
}

// ...
import java.lang.Math;
public class Kata {
    public static int[] digitize(long n) {
        String s = String.valueOf(n);
        int length = s.length();
        int[] array = new int[length];
        for ( int i = 0; i < length; i++)
            array[i] = (int) (s.charAt(length - i - 1)) - 48;
        return array;
    }
}

// ...
import java.util.Arrays;
import java.util.Stack;

public class Kata {
    public static int[] digitize(long n) {
        Stack<Integer> digits = new Stack<>();

        while (n > 0) {
            digits.push((int) (n % 10));
            n /= 10;
        }

        return digits.stream().mapToInt(Integer::intValue).toArray();
    }
}

// ...
public class Kata {
    public static int[] digitize(long n) {
        char[] array = String.valueOf(n).toCharArray();
        int[] result = new int[array.length];
        
        for(int i =0; i < array.length;i++)
            result[array.length-1-i] = Integer.valueOf(String.valueOf(array[i]));
        
        return result;
    }
}