// https://www.codewars.com/kata/printer-errors/train/java
// My solution
public class Printer {
    public static String printerError(String s) {
        return String.format("%d/%d", s.replaceAll("[a-m]","").length(), s.length());
    }
}

// ...
public class Printer {
    public static String printerError(String s) {
        return s.replaceAll("[a-m]", "").length() + "/" + s.length();
    }
}

// ....
public class Printer {
    public static String printerError(String s) {
        long errs = s.chars().filter( ch -> ch > 'm').count();
        return errs+"/"+s.length();
    }
}