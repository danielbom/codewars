// https://www.codewars.com/kata/sum-of-positive/train/c
// My solution
#include <stddef.h>

int positive_sum(const int *v, size_t n){
    int* p = v, s = 0;
    for(int i=0; i<n; i++, p++)
        if(*p > 0) s += *p;
    return s;
}

// ...
int positive_sum(const int *v, int n){
    return v[--n] > 0 ? (v[n] + (n <= 0 ? 0: positive_sum(v, n))) : (0 + (n <= 0 ? 0: positive_sum(v, n)));
}
