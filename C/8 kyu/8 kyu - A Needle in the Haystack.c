// https://www.codewars.com/kata/a-needle-in-the-haystack/train/c
// My solution
#include <stddef.h>
#include <string.h>

char *find_needle(const char **haystack, size_t n)
{
    int i;
    for(i=0; i < n; i++) if(strcmp(haystack[i], "needle") == 0) break;
    char *buffer;
    asprintf(&buffer, "found the needle at position %d", i);
    return buffer;
}

// ...
#include <stdio.h>

char *find_needle(const char **haystack, size_t count)
{
    for(int i=0; i<count;++i)
    {
        if(!strcmp(haystack[i], "needle")) // strcmp will return 0 if true, so we need '!' to it to work
        {
            char* buff;
            asprintf(&buff, "found the needle at position %d", i);
            return buff;
        }
    }
}

// ...
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

char *find_needle(const char **haystack, size_t count)
{
    while (strcmp(haystack[--count], "needle"));
    char *buf = malloc(128);
    sprintf(buf, "found the needle at position %d", count);
    return buf;
}