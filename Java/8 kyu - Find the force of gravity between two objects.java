// https://www.codewars.com/kata/find-the-force-of-gravity-between-two-objects/train/java
// My solution
import java.util.HashMap;

public class Solution {
    
    static final HashMap<String, Double> CONVENTIONS = 
        new HashMap<String, Double>() {{
            put("m" , 1.0);
            put("cm", 1e-2);
            put("mm", 1e-3);
            put("μm", 1e-6);
            put("ft", 0.3048);
            put("kg", 1.0);
            put("g" , 1e-3);
            put("mg", 1e-6);
            put("μg", 1e-9);
            put("lb", 0.453592);
        }};
    
    static final Double G = 6.67e-11;
    
    public static double solution(double[] arrVal, String[] arrUnit) {
        double m1 = arrVal[0] * CONVENTIONS.get(arrUnit[0]);
        double m2 = arrVal[1] * CONVENTIONS.get(arrUnit[1]);
        double r = arrVal[2] * CONVENTIONS.get(arrUnit[2]);
        return G * m1 * m2 / (r*r);
    }

}