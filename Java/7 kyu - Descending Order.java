// https://www.codewars.com/kata/descending-order/train/java
// My solution
import java.util.Arrays;
import java.util.Collections;

public class DescendingOrder {
    public static int sortDesc(final int num) {
        String[] sorted = String.valueOf(num).split("");
        Arrays.sort( sorted, Collections.reverseOrder() );
        return Integer.valueOf(String.join("", sorted));
    }
}

// ...
import java.util.Comparator;
import java.util.stream.Collectors;

public class DescendingOrder {
    public static int sortDesc(final int num) {
        return Integer.parseInt(String.valueOf(num)
                                      .chars()
                                      .mapToObj(i -> String.valueOf(Character.getNumericValue(i)))
                                      .sorted(Comparator.reverseOrder())
                                      .collect(Collectors.joining()));
    }
}

// ...
public class DescendingOrder {
  public static int sortDesc(final int num) {
        if (num < 0) throw new IllegalArgumentException("Negative number: " + num);

        return Integer.parseInt(Integer.toString(num).codePoints()
                .sorted()
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .reverse()
                .toString());
  }
}