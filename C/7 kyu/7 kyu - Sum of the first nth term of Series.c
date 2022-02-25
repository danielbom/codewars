// https://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/c
// My solution
#include <stddef.h>
#include <math.h>

char *series_sum( const size_t n ) {
    switch(n) {
        case (0): return strdup("0.00");
        case (1): return strdup("1.00");
        case (2): return strdup("1.25");
    }
    double a = 1.25, k = 7;
    for( int i = 2; i < n; i++ ) {
        a = a + 1/k;
        k += 3;
    }
    char *buffer = calloc( 32, sizeof(char) );
    snprintf( buffer, 32, "%.2lf", a );
    return buffer;
}

// ...
char *series_sum(const int n) {
    double result = n ? 1. : 0.;
    char *s = (char *)malloc(10 * sizeof(char));

    for (int i = 1; i < n; i++) result += 1. / (3 * i + 1);
    sprintf(s, "%.2lf", result);
    return s;
}