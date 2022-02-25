// https://www.codewars.com/kata/financing-plan-on-planet-xy140z-n/train/c
// My solution
typedef unsigned long long ull;
ull finance(ull n) {
    ull sum = 0;
    for(int i=0; i<=n; i++)
        for(int j=i*2; j <= n+i; j++)
            sum += j;
    return sum;
}

// ...
unsigned long long finance(unsigned long long n) {
    return n * (n+1) * (n+2) / 2;
}

// ...
unsigned long long finance(unsigned long long n) {
    /* The problem here amounts to a couple of sums of sequences,
     * specifically related to triangular numbers. Geometrically, the
     * sequence for the solution of finance(n) can be illustrated as
     * follows, where t(x) is the triangle number x, here shown for
     * finance(3):
     *
     *   t(2)       o
     *             o o
     *
     * - t(1)       x
     * + t(4)      o o
     *            o o o
     *           o o o o
     *
     * - t(2)       x
     *             x x
     * + t(6)     o o o
     *           o o o o
     *          o o o o o
     *         o o o o o o
     *
     * In other words, finance(n) is the sum of t(2x) for x in 1..n,
     * minus the sum of t(x-1) for x in 1..n. This can be rewritten
     * mathematically as follows without the use of an iterative loop
     * in the code:
     *
     * t(x) = (x²+x)/2
     *
     *        n /            \
     * f(n) = Σ( t(2n)-t(n-1) )
     *        1 \            /
     *
     *        n / (2n)² + 2n     (n-1)² + (n-1) \
     *      = Σ( ------------ - ---------------- )
     *        1 \      2                2       /
     *
     *        n / 3n² + 3n \
     *      = Σ( ---------- )
     *        1 \    2     /
     *
     *         3  n /      \
     *      = --- Σ( n² + n )
     *         2  1 \      /
     *
     *         3   /                                                 \
     *      = --- ( (1² + 2² + 3² + ... + n²) + (1 + 2 + 3 + ... + n) )
     *         2   \                                                 /
     *
     *         3     n(n+1)(2n+1)     3     n²+n
     *      = --- * -------------- + --- * ------
     *         2          6           2       2
     *
     *
     * This simplifies to this expression, which we implement:
     *
     *         n³ + 3n² + 2n
     * f(x) = ---------------
     *               2
     */
     return (n*n*n + 3*n*n + 2*n)/2;
}

