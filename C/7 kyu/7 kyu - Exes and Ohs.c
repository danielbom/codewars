// https://www.codewars.com/kata/exes-and-ohs/train/c
// My solution
#include <stdbool.h>

bool xo (const char* str){
    int i, k=0;
    for(i=0; str[i]; i++){
        if     (str[i] == 'x' || str[i] == 'X') k++;
        else if(str[i] == 'o' || str[i] == 'O') k--;
    }
    return (k==0);
}

// ...
#include <stdbool.h>

bool xo (const char* str)
{
    unsigned x = 0, o = 0;
    for (char *p = str; *p; p++) {
        if      (tolower(*p)=='x') x++;
        else if (tolower(*p)=='o') o++;
    }
    return x == o;
}