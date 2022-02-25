// https://www.codewars.com/kata/statistics-for-an-athletic-association/train/c
// My solution
#include <string.h>
#include <stdlib.h>

#define odd(x) x % 2 == 1

char *secs_to_hhmmss(int secs)
{
    int h = secs / 3600;
    secs -= h * 3600;
    int m = secs / 60;
    secs -= m * 60;
    int s = secs;
    
    char *buffer;
    asprintf(&buffer, "%02u|%02u|%02u", h,m,s);
    return buffer;
}

int cmpint(const void *a, const void *b)
{
    int _a = *(int *)a;
    int _b = *(int *)b;
    return _a > _b ? 1 : (_a < _b ? -1 : 0);
}

char* stat(char* strg) {
    // General buffer and your iterator
    char buffer[99] = {0};
    int j;
    // Calculating the number of elements
    int n = 1;
    for(char *ptr = strg; *ptr; ++ptr) n += *ptr == ' ';
    // Allocating memory to convert values to integers
    int *sec_times = malloc(n*sizeof(int));
    // Iterator to (sec_times)
    int i = 0;
    // Parsing string and converting values
    int h, m, s, sum = 0;
    for(char* ptr=strg; *ptr; ++ptr)
    {
        buffer[j++] = *ptr;
        if(*ptr == ' ')
        {
            buffer[j] = '\0';
            j = 0;
            
            sscanf(buffer, "%d|%d|%d", &h,&m,&s);
            sec_times[i] = 3600 * h + 60 * m + s;
            sum += sec_times[i++];
        }
    }
    // Last term
    buffer[j] = '\0';
    sscanf(buffer, "%d|%d|%d", &h,&m,&s);
    sec_times[i] = 3600 * h + 60 * m + s;
    sum += sec_times[i++];
    
    // Sorting array
    qsort(sec_times, n, sizeof(int), &cmpint);
    // Getting results
    int lowest = sec_times[0];
    int biggest = sec_times[n-1];
    int range = biggest - lowest;
    
    int avg = sum / n;
    
    int median = odd(n) ? sec_times[n/2] : (sec_times[n/2]+sec_times[(n/2)-1]) / 2.0;

    // Converting results and formatting output    
    char *srange = secs_to_hhmmss(range);
    char *savg = secs_to_hhmmss(avg);
    char *smedian = secs_to_hhmmss(median);
    snprintf(buffer, 99, "Range: %s Average: %s Median: %s", srange, savg, smedian);
    free(srange);
    free(savg);
    free(smedian);
    
    free(sec_times);
    return strdup(buffer);
}

// ...
#include <stdlib.h> /* malloc free qsort */
#include <stdio.h> /* sscanf snprintf */
#include <string.h> /* strlen */

int compare(const void * a, const void * b) {
  return  *(const int*)a -  *(const int*)b;
}

char * stat(char * strg) {
    int * times;
    char * cursor, * result;
    size_t length, n;
    int time, i, h, m, s, sum, average, range, median;
    
    length = strlen(strg);
    n = (length + 2) / 10;
    times = malloc(n * sizeof(int));
    result = malloc(51 * sizeof(char));

    cursor = strg;
    for(i = sum = 0; cursor < strg + length  && sscanf(cursor, "%d|%d|%d", &h, &m, &s) == 3; i++) {
        time = 3600 * h + 60 * m + s;
        sum += time;
        times[i] = time;
        cursor += 10;
    }
    
    qsort(times, n, sizeof(int), compare);
    
    average = sum / n;
    range = times[n - 1] - times[0];
    median = n % 2 == 0 ? (times[n / 2 - 1] + times[n / 2]) / 2: times[n / 2];
    
    free(times);

    snprintf(result, 51, "Range: %02d|%02d|%02d Average: %02d|%02d|%02d Median: %02d|%02d|%02d",
        range / 3600, range % 3600 / 60, range % 60,
        average / 3600, average % 3600 / 60, average % 60,
        median / 3600, median % 3600 / 60, median % 60);

    return result;
}