// https://www.codewars.com/kata/maximum-length-difference/train/c
// My solution
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int mod(int a, int b){
    if (a-b >= 0)
        return a-b;
    return b-a;
}

int mxdiflg(
    const char **firstArray, size_t firstArrayLength, 
    const char **secondArray, size_t secondArrayLength){
    
    if(firstArrayLength == 0 || secondArrayLength == 0) return -1;

    int n1[firstArrayLength], n2[secondArrayLength], i, j, m=0;
    
    for(i=0 ; i<firstArrayLength ; i++) n1[i] = strlen(firstArray[i]);
    
    for(i=0 ; i<secondArrayLength ; i++) n2[i] = strlen(secondArray[i]);
    
    for(i=0 ; i<firstArrayLength ; i++){
        for(j=0 ; j<secondArrayLength ; j++){
            if( mod( n1[i], n2[j] ) > m ) {
                m = mod( n1[i], n2[j] );
            }
        }
    }

    return m;
}

// ...
#include <string.h>
#include <stdlib.h>
#include <limits.h>

void max_and_min_of_array
(const char **array, size_t length, int *result_max, int *result_min)
{
  *result_max = 0;
  *result_min = INT_MAX;
  for(size_t i=0;i<length;i++)
    {
      int len_of_item = strlen(array[i]);
      if(len_of_item > *result_max) *result_max = len_of_item; 
      if (len_of_item < *result_min) *result_min = len_of_item;
    }
}

int mxdiflg(
            const char **firstArray, size_t firstArrayLength,
            const char **secondArray, size_t secondArrayLength)
{
  if(firstArrayLength == 0 || secondArrayLength == 0) return -1;

  int fa_max = 0, fa_min = 0;
  int sa_max = 0, sa_min = 0;
  max_and_min_of_array(firstArray, firstArrayLength, &fa_max, &fa_min);
  max_and_min_of_array(secondArray, secondArrayLength, &sa_max, &sa_min);

  int fmax_smin = abs(fa_max - sa_min);
  int smax_fmin = abs(sa_max - fa_min);

  return fmax_smin - smax_fmin  > 0 ? fmax_smin : smax_fmin;
}

// ...
#include <string.h>
#define max(a,b) a > b ? a : b

int minMaxLg (const char **a, size_t l, int * min, int * max) {
    int tmp, i;
    *min = *max = strlen(a[0]);
    for (i = 1; i < l; i++) {
        tmp = strlen(a[i]);
        if (tmp > *max) *max = tmp;
        else if (tmp < *min) *min = tmp;
    }
}

int mxdiflg (const char **a1, size_t l1, const char **a2, size_t l2) {
    int min1, min2, max1, max2;
    int sol1, sol2;
    
    if (l1 == 0 || l2 == 0) return -1;
    
    minMaxLg (a1, l1, &min1, &max1);
    minMaxLg (a2, l2, &min2, &max2);
    
    sol1 = max1 - min2;
    sol2 = max2 - min1;
    
    return max (sol1, sol2);
}

// ...
#include <stdlib.h>
#include <limits.h>


int mxdiflg(const char **arr0, size_t len0, 
            const char **arr1, size_t len1) {

    int min[2] = { INT_MAX, INT_MAX },  max[2] = {0, 0};
    
    #define WORST_PRACTISE(i)                 \
    while (len##i --> 0) {                    \
        int tmp = strlen( *arr##i++ );        \
        min[i] = tmp < min[i] ? tmp : min[i]; \
        max[i] = tmp > max[i] ? tmp : max[i]; \
    }
    
    WORST_PRACTISE(0)
    WORST_PRACTISE(1)
    #undef WORST_PRACTISE       

    return (max[0] == 0 || max[1] == 0) ? -1 :
    max[0]-min[1] > max[1]-min[0] ? max[0]-min[1] : max[1]-min[0];
}

// ...
#include <string.h>

int mxdiflg(
  const char **firstArray, size_t firstArrayLength, 
  const char **secondArray, size_t secondArrayLength
)
{
    int max_diff = -1;
    for (int i = 0; i < firstArrayLength; i++) {
        for (int j = 0; j < secondArrayLength; j++) {
            int diff = strlen(firstArray[i]) - strlen(secondArray[j]);
            if (diff < 0) { diff = -1*diff; }
            if (diff > max_diff) { max_diff = diff; }
        }
    }

    return max_diff;
}

// ...
#include <math.h>
#include <string.h>
int mxdiflg(const char **arr1, size_t l1, const char **arr2, size_t l2){
    if(l1 == 0 || l2 == 0) return -1;
    int max = 0, trial;
    for(int i = 0; i < l1; i++){
        for(int j = 0; j < l2; j++){
            trial = abs(strlen(arr1[i]) - strlen(arr2[j]));
            if(trial > max)
                max = trial;
        }
    }
    return max;
}
