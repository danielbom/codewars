// https://www.codewars.com/kata/product-of-consecutive-fib-numbers/train/c
// My solution
typedef unsigned long long ull;

ull* productFib(ull prod) {
    ull* res = (ull*) calloc (3, sizeof(ull));
    res[0] = res[1] = 1;
    while(res[0]*res[1] < prod){
        res[2] = res[0]+res[1];
        res[0] = res[1];
        res[1] = res[2];
    }
    res[2] = res[0]*res[1] == prod;
    return res;
}

// ...
#include <stdlib.h>

typedef unsigned long long ull;

typedef struct { ull n, f, fn1; } FibState;

void initFibGenerator(FibState *fs) {
    fs->n = 1;
    fs->f = 1;
    fs->fn1 = 0;
}

void stepFibGenerator(FibState *fs) {
    (fs->n)++;
    ull temp = fs->f;
    fs->f += fs->fn1;
    fs->fn1 = temp;
}

unsigned long long* pack(ull fn, ull fn1, ull flag) {
    ull* r = (ull*) malloc(3 * sizeof(ull));
    r[0] = fn;
    r[1] = fn1;
    r[2] = flag;
    return r;
}

unsigned long long* productFib(const ull prod) {
    ull p;
    FibState fs;
    initFibGenerator(&fs);
    while ((p = fs.f * fs.fn1) < prod) {
        stepFibGenerator(&fs);
    }
    return pack(fs.fn1, fs.f, prod == p);
}

// ...
#include <malloc.h>
#include <math.h>

#define uint64 long unsigned
#define float128 long double

#define sqrt5  2.236067977499789696409173668731276235440618359611525724270897245l  // √5
#define phi    1.618033988749894848204586834365638117720309179805762862135448623l  // (1+√5) / 2
#define logPhi 0.962423650119206894995517826848736846270368668771321039322036338l  // ln(phi) * 2


uint64* productFib(uint64 prod) {
    float128 Fl    = prod;
    float128 temp1 = powl(phi, roundl(logl(5 * Fl - 1)/logPhi - 0.5)) / sqrt5;
    float128 temp2 = temp1 * phi;

    Fl -= roundl(temp1) * roundl(temp2);
    if ( Fl > 0 ) Fl -= roundl(temp1 = temp2) * roundl(temp2 *= phi);
    
    uint64* r = malloc(3 * sizeof(uint64));
    r[0] = roundl(temp1);
    r[1] = roundl(temp2);
    r[2] = 0.0 == Fl ;
    return r;
}