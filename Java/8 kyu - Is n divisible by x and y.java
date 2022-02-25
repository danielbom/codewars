// https://www.codewars.com/kata/is-n-divisible-by-x-and-y/train/java
// My solution
public class DivisibleNb {
	public static boolean isDivisible(long n, long x, long y) {
        return n % x == 0 && n % y == 0;
	}
}