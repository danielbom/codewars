// https://www.codewars.com/kata/growth-of-a-population/train/c
// My solution
int nbYear(int p0, double percent, int aug, int p) {
    int anos = 0;
    while(p0 < p){
        p0 += (p0 * percent / 100) + aug;
        anos++;
    }
    return anos;
}

// ...
int nbYear(int p0, double percent, int aug, int p) {
    int counter = 0;
    percent /= 100;
    while (p0 < p){
      p0 += p0 * percent + aug;
      counter++;
    }
    
    return counter;
}

// ...
int nbYear(int p0, double percent, int aug, int p) {
    if(p0 >= p) return 0;
    else return nbYear((p0 + p0 * percent/100 + aug), percent, aug, p) + 1;
}

// ...
#include <math.h>
// say we start wtih x0, 'p' is a add ratio and 'a' is people added
// then we can write:
// x1 = x0(1+p)   + a
// x2 = x0(1+p)^2 + a(1+p) + a
// x3 = x0(1+p)^3 + a(1+p)^2 + a(1+p) + a
// * remembering that Sum(i=0..n-1, x^i) = [x^n-1]/[x-1]
// xn = x0(1+p)^n + a*[(1+p)^n-1]/p = (x0 + a/p)(1+p)^n - a/p
// written differently: (x0 + a/p)(1+p)^n >= N + a/p <=> (1+p)^n >= [N + a/p] / [x0 + a/p]
// taking log base 1+p: n >= log( [N+a/p] / [x0 + a/p] )
// * remembering that log[base](v) = ln(v)/ln(base)
static inline int solve(int x0, double p, int a, int N) {
    const double lp = log(1+p), lv = log(N+a/p) - log(x0 + a/p);
    return (int)(ceil(lv/lp));
}
// this is from kata
int nbYear(int p0, double percent, int aug, int p) {
    // if percent added is 0 we increase populace only by people coming
    // NB how do we handle case of populace decreasing>
    return percent > 0 ? solve(p0, percent/100.0, aug, p) : (p - p0 + aug-1) / aug;
}

// ...
#include <math.h>
// Direct solution (without loops and recursion)
int nbYear(int p0, double percent, int aug, int p) {
    return (percent /= 100)
      ? ceil(log1p((p - p0) / (p0 + aug / percent)) / log1p(percent))
      : (p - p0 + aug - 1) / aug;
}