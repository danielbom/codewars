// https://www.codewars.com/kata/string-repeat/train/java
// My solution
public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        if(repeat > 0) return string + repeatStr(repeat-1, string);
        return "";
    }
}

// ...
public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < repeat; i++) {
            sb.append(string);
        }
        return sb.toString();
    }
}

// ...
public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        return java.util.stream.IntStream
            .range(0, repeat)
            .mapToObj(i -> string)
            .collect(java.util.stream.Collectors.joining())
            .toString();
    }
}

// ...
import java.util.Collections;
public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        return (repeat > 0) ? String.join("", Collections.nCopies(repeat, string)) : "";
    }
}