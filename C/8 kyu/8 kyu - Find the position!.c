// https://www.codewars.com/kata/find-the-position/train/c
// My solution
#include <string.h>

char* position(char ch) {
    char buffer[50];
    int result = -1;
    if ( ch >= 'a' && ch <= 'z' ) result = ch - 'a' + 1;
    if ( ch >= 'A' && ch <= 'Z' ) result = ch - 'A' + 1;
    sprintf( buffer, "Position of alphabet: %d", result );
    return strdup(buffer);
}
// ...
char* position(char alphabet) {
  char *sentence = malloc(25 * sizeof(char));  
  sprintf(sentence, "Position of alphabet: %d", (int)tolower(alphabet) - 96);
 
  return sentence;
}