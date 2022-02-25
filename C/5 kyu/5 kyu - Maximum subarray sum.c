// https://www.codewars.com/kata/maximum-subarray-sum/train/c
// My solution
include <stddef.h>
#include <stdlib.h>

int findMaxCrossingSubArray( const int* array, int left, int middle, int right )
{
    int max_l = array[middle], sum = 0;
    // ... ,m-2, m-1, m
    for ( int i = middle; i >= left ; --i )
    {
        sum += array[i];
        if ( sum > max_l )
            max_l = sum;
    }
    
    int max_r = array[middle+1];
    sum = 0;
    // m+1, m+2, m+3, ...
    for ( int i = middle+1; i <= right; ++i )
    {
        sum += array[i];
        if ( sum > max_r )
            max_r = sum;
    }
    return max_l + max_r;
}

int findMaxSubArray( const int* array, int left, int right )
{
    if ( left == right ) return array[left];

    int middle = (right + left) / 2;
    int max_l = findMaxSubArray(array, left, middle);
    int max_r = findMaxSubArray(array, middle+1, right);
    int max_m = findMaxCrossingSubArray(array, left, middle, right);
    
    if ( max_l >= max_r && max_l >= max_m ) return max_l;
    if ( max_r >= max_l && max_r >= max_m ) return max_r;
    return max_m;
}

int maxSequence( const int* array, size_t n )
{
    if ( n <= 0 ) return 0;
    int max = findMaxSubArray( array, 0, n-1 );
    return max > 0 ? max : 0;
}

// ...
#include <stddef.h>

int maxSequence(const int* array, size_t n) {
    int max_so_far = 0;
    int max_ending_here = 0;
    for(int i =0; i< n; i++){
        max_ending_here += array[i];
        if(max_ending_here < 0)
        max_ending_here = 0;
        if(max_so_far < max_ending_here)
        max_so_far = max_ending_here;
    }
    return max_so_far;
}

// ...
#include <stddef.h>

int maxSequence(const int* array, size_t n) {
    int max_num = 0;
    int cur_max = -99999;
    for(int i = 1; i < n ; i++) {
        int cm = cur_max + array[i];
        cur_max = cm > array[i] ? cm : array[i];
        max_num = cur_max > max_num ? cur_max : max_num;
    }
    return max_num;
}