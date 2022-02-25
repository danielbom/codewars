// https://www.codewars.com/kata/tribonacci-sequence/train/java
// My solution
import java.util.Arrays;

public class Xbonacci {
  public double[] tribonacci(double[] s, int n) {
      double[] t = new double[n];
      if(n == 0) return t;
      t[0] = s[0];
      if(n == 1) return t;
      t[1] = s[1];
      if(n == 2) return t;
      t[2] = s[2];
      for (int i = 3; i < n; i++) {
          t[i] = t[i-1] + t[i-2] + t[i-3];
      }
      return t;
  }
}

// ...
import java.util.Arrays;

public class Xbonacci {
    public double[] tribonacci(double[] s, int n) {
        double[] tritab=Arrays.copyOf(s, n);
        for(int i=3;i<n;i++){
            tritab[i]=tritab[i-1]+tritab[i-2]+tritab[i-3];
        }
        return tritab;
    }
}
