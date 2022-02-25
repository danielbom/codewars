// https://www.codewars.com/kata/reversed-sequence/train/java
// My solution
public class Sequence {
    public static int[] reverse(int n) {
        int[] array = new int[n];
        for (int i = 0; i < n; i++)
            array[i] = n - i;
        return array;
    }
}

// ...
import java.util.stream.IntStream;

public class Sequence{
    public static int[] reverse(int n){
        return IntStream.range(-n, 0).map(Math::abs).toArray();
    }
}

// ...
import java.util.stream.IntStream;

public class Sequence{
    public static int[] reverse(int n){
        return IntStream.iterate(n, i -> i - 1).limit(n).toArray();
    }
}

// ...
import java.util.stream.IntStream;

public class Sequence {
    public static int[] reverse(int n) {
        return IntStream.range(0, n).map(x -> n - x).toArray();
    }
}