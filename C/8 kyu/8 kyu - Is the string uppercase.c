// https://www.codewars.com/kata/is-the-string-uppercase/train/c
// My solution
#include <stdbool.h>

bool is_uppercase(const char *source) {
    for (char *ptr = source; *ptr; ptr++)
        if (isalpha(*ptr) && !isupper(*ptr))
            return false;
    return true;
}
// ...
#include <stdbool.h>

bool is_uppercase(const char *source) {
    for (int i = 0; i < strlen(source); i++) {
        if (islower(*(source + i))) {
            return false;
        }
    }
    return true;
}