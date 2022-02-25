// https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/java
// My solution
import java.util.Arrays;

public class Counter {
    public int countSheeps(Boolean[] arrayOfSheeps) {
        return (int) Arrays
            .asList(arrayOfSheeps)
            .parallelStream()
            .filter(s -> s != null && s)
            .count();
    }
}

// Me 2
import java.util.Arrays;

public class Counter {
    public int countSheeps(Boolean[] arrayOfSheeps) {
        return (int) Arrays.stream(arrayOfSheeps)
            .filter(s -> s != null && s)
            .count();
    }
}

// ...
public class Counter {
    public int countSheeps(Boolean[] arrayOfSheeps) {
        int count = 0;
        for (Boolean b : arrayOfSheeps) if (b) count++;
        return count;
    }
}

// ...
import java.util.Arrays;

public class Counter {
    @Deprecated
    public int countSheeps(Boolean[] arrayOfSheeps) {
        return (int) countSheep(arrayOfSheeps);
    }
    
    public static long countSheep(Boolean[] arrayOfSheep) {
        return Arrays.stream(arrayOfSheep)
                .filter(sheep -> sheep == Boolean.TRUE)
                .count();
    }
}