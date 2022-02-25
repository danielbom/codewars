// https://www.codewars.com/kata/isograms/train/java
// My solution
public class isogram {
    public static boolean isIsogram(String str) {
        int[] map = new int[26];
        int n = str.length();
        String pstr = str.toLowerCase();
        for(int i = 0; i < n; i++)
        {
            map[pstr.charAt(i) - 'a']++;
            if (map[pstr.charAt(i) - 'a'] > 1) return false;
        }
        return true;
    } 
}

// ...
public class isogram {
    public static boolean  isIsogram(String str) {
        return str.length() == str.toLowerCase().chars().distinct().count();
    } 
}

// ...
import java.util.HashSet;
import java.util.Set;

public class isogram {
    public static boolean isIsogram(String str) {
        Set<Character> letters = new HashSet<Character>();
        for (int i = 0; i < str.length(); ++i) {
            if (letters.contains(str.toLowerCase().charAt(i))) {
                return false;        
            }
            letters.add(str.charAt(i));
        }
        return true;
    }
}