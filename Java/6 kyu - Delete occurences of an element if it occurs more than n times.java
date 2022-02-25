// https://www.codewars.com/kata/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times/train/java
// My solution
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

public class EnoughIsEnough {
	public static int[] deleteNth(int[] elements, int maxOccurrences) {
		Map<Integer, Integer> map = new HashMap<>();
        int[] returned = new int[elements.length];
        int i = 0;
        for(int e: elements) {
            map.merge(e, 1, Integer::sum);
            if(map.getOrDefault(e, 0) <= maxOccurrences)
                returned[i++] = e;
        }
		return Arrays.copyOf(returned, i);
	}
}

// ...
import java.util.*;

public class EnoughIsEnough {
    public static int[] deleteNth(int[] elements, int max) {
        if (max < 1) return new int[0];
        
        final HashMap<Integer,Integer> map = new HashMap<>();
        final List<Integer> list = new ArrayList<>();
        
        for (final Integer i : elements) {
            final Integer v = map.put(i, map.getOrDefault(i, 0) + 1);
            if (v == null || v < max) list.add(i);
        }
        
        return list.stream().mapToInt(i->i).toArray();
    }
}

// ...
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class EnoughIsEnough {
    private static boolean shouldAdd(final Map<Integer, Integer> counts, final int element, final int maxOcurrences) {
        if (counts.getOrDefault(element, 0) < maxOcurrences) {
            counts.merge(element, 1, Integer::sum);
            return true;
        }
        return false;
    }

    static int[] deleteNth(final int[] elements, final int maxOcurrences) {
        final Map<Integer, Integer> counts = new HashMap<>();
        return Arrays.stream(elements)
            .filter(element -> shouldAdd(counts, element, maxOcurrences))
            .toArray();
    }
}

// ...
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

public class EnoughIsEnough {
    public static int[] deleteNth(int[] elements, int maxOccurrences) {
        Map<Integer, Integer> occurrence = new HashMap<>();
        return IntStream.of(elements)
            .filter(motif -> occurrence.merge(motif, 1, Integer::sum) <= maxOccurrences)
            .toArray();
    }
}

// ...
import java.util.Arrays;
import java.util.HashMap;

public class EnoughIsEnough {
    public static int[] deleteNth(int[] elements, int maxOcurrences) {
        //Code here ;)
        HashMap<Integer, Integer> map = new HashMap<>();
        return Arrays.stream(elements)
        .filter(i -> {
            map.merge(i, 1, Integer::sum);
            return map.get(i) <= maxOcurrences;
            })
        .toArray();
    }
}