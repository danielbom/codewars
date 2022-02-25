// https://www.codewars.com/kata/exclamation-marks-series-number-6-remove-n-exclamation-marks-in-the-sentence-from-left-to-right/train/c
// My solution
#include <stdlib.h>

char* remove(const char* string, int n) {
  char buffer[1024] = {0};
  for(int i = 0, j = 0; string[i]; i++) {
    if (n > 0 && string[i] == '!') n--;
    else buffer[j++] = string[i];
  }
  return strdup(buffer);
}

// ...
#include <stdlib.h>

char *remove(char *s, int n) {
  char* r = (char*)calloc(strlen(s) + 1, sizeof(char));
  for (int i = 0, j = 0; i < strlen(s); i++)
    if (s[i] != '!' || --n < 0)
        r[j++] = s[i];
  return r;
}

// ...
#include <stdlib.h>

char *remove(char *strin, int n) {

    char *res = calloc(strlen(strin), 1);
    char *tmp = res;

    do {
        if(*strin == '!' && n-- > 0)
            continue;
        *tmp++ = *strin;
    } 
    while(*(++strin));
    
    return res;
}