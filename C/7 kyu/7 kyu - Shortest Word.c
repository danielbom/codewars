// https://www.codewars.com/kata/shortest-word/train/c
// My solution
#include <sys/types.h>
#include <string.h>

ssize_t find_short(const char *s) {
  int minLength = 65000;
  int length = 0;
  
  for(int i = 0; s[i]; i++) {
    if(s[i] == ' ') {
      if (minLength > length) {
        minLength = length;
      }
      length = 0;
    } else {
      length++;
    }
  }
  
  return minLength > length ? length : minLength;
}

// ...
#include <sys/types.h>
#include <string.h>

ssize_t find_short(const char *s) {
  char * word = strtok(s, " ");
  int len = strlen(word);
  while (word != NULL) {
    if (strlen(word) < len) len = strlen(word);
    word = strtok(NULL, " ");
  }
  return len;
}
