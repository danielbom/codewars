// https://www.codewars.com/kata/bit-counting/train/c
// My solution
#include <stddef.h>

size_t countBits(unsigned value){
    int i, c=0;
    for(i=1; i <= value ; i*=2)
        if(value & i) c++;  
    return c;
}

// ...
#include <stddef.h>

size_t countBits(unsigned value)
{
    size_t count = 0;
    for (; value; value >>= 1) if ( value & 1 ) count++;
    return count;
}

// ...
#include <stddef.h>

size_t countBits(unsigned value)
{
     unsigned bits;
     bits = value - ((value >> 1) & 033333333333) - ((value >> 2) & 011111111111);
     return ((bits + (bits >> 3)) & 030707070707) % 63;
}

// ...
#include <stddef.h>

size_t countBits(unsigned value) {
    return __builtin_popcount(value);
}

// ...
#include <stddef.h>

size_t countBits(unsigned value){
    return ((value % 2 == 1) ? 1 : 0) + (value ? countBits(value / 2) : 0);
}