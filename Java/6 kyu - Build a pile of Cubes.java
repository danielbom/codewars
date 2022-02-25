// https://www.codewars.com/kata/build-a-pile-of-cubes/train/java
// My solution :(
import java.math.BigInteger;

public class ASum {
    public static BigInteger ten = new BigInteger("10");
    public static BigInteger one = new BigInteger("1");
    private static BigInteger calc(BigInteger n) {
        return n.multiply(n.add(one)).shiftRight(1).pow(2);
    }
  
	public static long findNb(long arg) {
        if(arg <= 0) return -1;
        BigInteger m = new BigInteger(String.valueOf(arg));
        BigInteger v = new BigInteger("1");
        BigInteger i = new BigInteger("1");
        while(v.compareTo(m) < 0)
        {
            i = i.multiply(ten);
            v = calc(i);
        }
        if(v.compareTo(m) == 0) return i.divide(ten).longValue();
        i = i.divide(ten);
        v = calc(i);
        BigInteger k = new BigInteger(String.valueOf(i));
        i = i.subtract(k);
        while(v.compareTo(m) < 0) {
            i = i.add(k);
            v = calc(i);
            if(v.compareTo(m) > 0 && k.compareTo(one) > 0) {
                i = i.subtract(k);
                k = k.divide(ten);
                v = calc(i);
            }
        }
        v = calc(i);
        return v.compareTo(m) == 0 ? i.longValue() : -1;
	}	
}

// ...
public class ASum {
    public static long findNb(long m) {
        long mm = 0, n = 0;
        while (mm < m) mm += ++n * n * n;
        return mm == m ? n : -1;
    }
}

// ...
public class ASum {
    public static long findNb(long m) {
        long n = 1;
        while (m > 1) m -= ++n * n * n;
        return m == 1 ? n : -1;
    }

// ...
public class ASum {
    public static long findNb(long m) {
        long ex=(long)Math.sqrt((long) Math.sqrt(m)*2);  
        if((ex*(ex+1)/2)*(ex*(ex+1)/2)==m)
            return ex;
        else
            return -1;
    }  
}