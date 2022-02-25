// https://www.codewars.com/kata/5865918c6b569962950002a1/train/c
// My solution
#include <stddef.h>

size_t str_count(const char *str, char letter) {
  int count = 0;
  for (char *ptr = str; *ptr; ptr++)
    if (*ptr == letter) 
      count++;
  return count;
}
