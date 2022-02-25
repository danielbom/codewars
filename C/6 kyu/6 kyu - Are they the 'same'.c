// https://www.codewars.com/kata/are-they-the-same/train/c
// My solution
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

void sort(int *number, int n) {
    /* Sort the given array number, of length n */
    int temp = 0, j, i;
    for (i = 1; i < n; i++) {
        for (j = 0; j < n - i; j++) {
            if (number[j] > number[j + 1]) {
                temp = number[j];
                number[j] = number[j + 1];
                number[j + 1] = temp;
            }
        }
    }
}
bool comp(int* a, int* b, int sizeArray) {  
    sort(a, sizeArray);
    sort(b, sizeArray);

    for(int i=0; i<sizeArray; i++){
        if( a[i]*a[i] != b[i] ){
            return false;
        }
    }
    return true;
}

// ...
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define true  1
#define false 0

int compare_ints (const void *a, const void *b);
// given numbers being supposed >= 0
bool comp(int* a, int* b, size_t sizeArray) {
    qsort (a, sizeArray, sizeof (int), compare_ints);
    qsort (b, sizeArray, sizeof (int), compare_ints);
    for (int k = 0; k < sizeArray; k++)
        if (a[k] * a[k] != b[k]) return false;
    return true;
}

// ...
#include <stdbool.h>
#include <stdlib.h>
bool comp(int* a, int* b, size_t sizeArray) {
    int i, suma, sumb;

    // check if sum of both array elements with conditions is the same
    suma = 0; sumb = 0;
    for (i = 0; i < sizeArray; i++) {
        suma += a[i] * a[i];
        sumb += b[i];
    }
    
    return (suma == sumb);
}

// ...
#include <stddef.h>
#include <stdbool.h>
bool comp(const int *a, const int *b, size_t n)
{
    int i, j, cmp = 0;
    if (!a || !b || !n)
        return false;
    while (n--) {
        i = *a++, j = *b++;
        if ((!i || !j) && i != b)
            return false;
        cmp += i * i - j;
    }
    return !cmp;
}

// ...
#include <stdbool.h>
bool comp(const int *a, const int *b, int n)
{
    int cmp = 0;
    while (n--) cmp += *a * *a++ - *b++;
    return cmp == 0;
}