// https://www.codewars.com/kata/who-likes-it/train/java
// My solution
class Solution {
    public static String whoLikesIt(String... names) {
        if(names.length == 0)
            return "no one likes this";
        if(names.length == 1)
            return names[0] + " likes this";
        if(names.length == 2)
            return names[0] + " and " + names[1] + " like this";
        if(names.length == 3)
            return names[0] + ", " + names[1] + " and " + names[2] + " like this";
        return names[0] + ", " + names[1] + " and " +
              String.valueOf(names.length - 2) +" others like this";
    }
}

// ...
class Solution {
    public static String whoLikesIt(String... names) {
        switch (names.length) {
            case 0:
                return "no one likes this";
            case 1:
                return String.format("%s likes this", names[0]);
            case 2:
                return String.format("%s and %s like this", names[0], names[1]);
            case 3:
                return String.format("%s, %s and %s like this", names[0], names[1], names[2]);
            default:
                return String.format("%s, %s and %d others like this", names[0], names[1], names.length - 2);
        }
    }
}

// ...
import java.util.Arrays;
import java.util.List;

class Solution {
    public static String whoLikesIt(String... names) {
        //Do your magic here
        
        StringBuilder output = new StringBuilder();
        
        List<String> values = Arrays.asList(names);
        
        if (values.isEmpty()) {
          output.append("no one likes this");
        } else if (values.size() == 1) {
          output.append(values.get(0))
          .append(" likes this"); 
        } else if (values.size() == 2) {
          output.append(values.get(0))
          .append(" and ")
          .append(values.get(1))
          .append(" like this");
        } else if (values.size() == 3) {
          output.append(values.get(0))
          .append(", ")
          .append(values.get(1))
          .append(" and ")
          .append(values.get(2))
          .append(" like this");
        } else {
          output.append(values.get(0))
          .append(", ")
          .append(values.get(1))
          .append(" and ")
          .append(values.size() - 2)
          .append(" others like this");        
        }
        
        return output.toString();
    }
}