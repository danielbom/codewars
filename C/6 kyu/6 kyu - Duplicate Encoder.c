// https://www.codewars.com/kata/duplicate-encoder/train/c
// My solution
#include <stdlib.h>

char *DuplicateEncoder(char * s){
    char* res = strdup(s), map[256] = {0};
    for ( char *p = s; *p; ++p ) ++map[tolower(*p)];
    for ( char *p = res; *p; ++p ) *p = map[tolower(*p)] == 1 ? '(' : ')';
    return res;
}