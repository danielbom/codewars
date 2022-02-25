// https://www.codewars.com/kata/thinkful-string-drills-repeater/train/c
// My solution
#include <stdlib.h>

char* repeater( const char* string, int n ) {
  char* buffer = calloc( strlen( string ) * n + 1, sizeof(char) );
  while( n-- ) strcat( buffer, string );
  return buffer;
}

// ...
#include <stdlib.h>
#include <string.h>

char* repeater(const char* strin, int n) {
    int len = strlen(strin);
    char *strout = calloc(1024, sizeof(char));

    for (int i = 0, end = len * n; i < end; ++i)
        strout[i] = strin[i % len];
    return strout;
}