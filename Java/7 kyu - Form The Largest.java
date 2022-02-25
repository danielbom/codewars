// https://www.codewars.com/kata/form-the-largest/train/java
// My solution
import java.util.Comparator;
import java.util.stream.Collectors;

public class Solution {
    public static long maxNumber(long n) {
        return Long.parseLong(
              String.valueOf(n)
        	        .chars()
        	        .mapToObj(i -> String.valueOf(Character.getNumericValue(i)))
        	        .sorted(Comparator.reverseOrder())
        	        .collect(Collectors.joining()));
    }
}

// ...
import java.util.stream.Collectors;
import java.util.Arrays;

public class Solution {
    public static long maxNumber(long n) {
        return Long.parseLong(
                Arrays.stream((n + "")
                        .split(""))
                        .sorted((x,y)->y.compareTo(x))
                        .collect(Collectors.joining()));
    }
}

// ...
import java.util.*;

public class Solution {
    public static long maxNumber(long n) {
        char[] ary = (""+n).toCharArray();  
        Arrays.sort(ary); 
        return new Long(new StringBuilder(new String(ary)).reverse().toString());
    }
}

// ...
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;

public class Solution {
    public static long maxNumber(long n) {
        String[] strings = String.valueOf(n).split("");
        String s = Arrays.stream(strings)
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.joining(""));
        return Long.valueOf(s);
    }
}