// https://www.codewars.com/kata/sort-one-three-two/train/c
// My solution
#include <stdlib.h>

char* int_to_name(int i){
    char* unidade[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    char* dez[] = {"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    char* dezena[] = {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
    char cem[] = "hundred", espaco[] = " ";

    char* r = calloc(256, 1);
    if(i == 0) {
        strcat(r, unidade[0]);
    }
    if(i >= 100){
        strcat(r, unidade[i/100]);
        strcat(r, espaco);
        strcat(r, cem);
        i %= 100;
        if(i) strcat(r, espaco);
    }
    if(i < 20 && i > 10){
        strcat(r, dez[i-11]);
        i -= i;
    }
    else{
        if( i / 10 >= 1 ){
            strcat(r, dezena[ (i/10) - 1]);
            i %= 10;
            if(i) strcat(r, espaco);
        }
        if( i > 0 ){
            strcat(r, unidade[i]);
        }
    }
    return r;
}

int cmp(void* a, void* b){
    char* stra = int_to_name(*(int*) a); // Dont freed
    char* strb = int_to_name(*(int*) b); // Dont freed
    return strcmp(stra, strb);
}

int *sort(const int *array, int length){
    if(array == NULL) return NULL;
    int* v = malloc(length*sizeof(int));
    memcpy(v, array, length*sizeof(int));
    qsort(v, length, sizeof(int), cmp);
    return v ;
}

// ...
#include <stdlib.h>

static const char *names0to19[] = {
    "zero",    "one",     "two",       "three",    "four",
    "five",    "six",     "seven",     "eight",    "nine",
    "ten",     "eleven",  "twelve",    "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
};
static const char *names20to90[] = {
    "zero",  "ten",   "twenty",  "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"
};

static char *numberToName(int n)
{
    if ( n == 0 ) return strdup(names0to19[0]);
    char *name = (char *)calloc(40, sizeof(char));
    int   len  = 0;
    if ( n > 99 ) { len += sprintf(name+len, "%s hundred ", names0to19 [n / 100]); n %= 100; }
    if ( n > 19 ) { len += sprintf(name+len, "%s ",         names20to90[n /  10]); n %=  10; }
    if ( n >  0 )   len += sprintf(name+len, "%s ",         names0to19 [n]);
    name[len-1] = '\0';
    return name;
}

static int compareNames(const void *a, const void *b)
{
    char *name1 = numberToName(*(int *)a),
         *name2 = numberToName(*(int *)b);
    int cmp = strcmp(name1, name2);
    free(name1); free(name2);
    return cmp;
}

int *sort(const int *array, int length)
{
    if ( !array || !length ) return NULL;
    int *sortedArray = (int *)malloc(length * sizeof(int));
    memcpy(sortedArray, array, length * sizeof(int));
    qsort(sortedArray, length, sizeof(int), compareNames);
    return sortedArray;
}

// ...
#include <stdlib.h>

void print_int(char *s, int num) {
    char *single[10] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    char *dozen[10] = { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };
    char *tens[10] = { "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "" };
    
    int pos = 0;
    int val = num / 100;
    if (val != 0) {
        pos += sprintf(s, "%s hundred", single[val]);
        num -= val * 100;
        if (num > 0) {
            s[pos] = ' ';
            pos++;
        }
    }
    val = num / 10;
    if (val != 0) {
        if (val == 1) {
            num -= 10;
            sprintf(s + pos, "%s", tens[num]);
            return;
        }
        pos += sprintf(s + pos, "%s", dozen[val]);
        num -= val * 10;
        if (num > 0) {
            s[pos] = ' ';
            pos++;
        }
        else {
            return;
        }
    }
    if (num != 0 || pos == 0) {
        pos += sprintf(s + pos, "%s", single[num]);
    }
}

int cmp(const void *l, const void *r) {
    char ls[64] = {0}, rs[64] = {0};
    print_int(ls, *((int *)l));
    print_int(rs, *((int *)r));
    return strcmp(ls, rs);
}

int *sort(const int *array, int length)
{
    if (array == NULL || length == 0) {
        return NULL;
    }

    int *res = (int *)malloc(length * sizeof(int));
    memcpy(res, array, (length * sizeof(int)));
    
    qsort(res, length, sizeof(int), cmp);
    
    return res;
}

