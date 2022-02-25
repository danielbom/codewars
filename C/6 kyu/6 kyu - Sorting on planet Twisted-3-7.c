// https://www.codewars.com/kata/sorting-on-planet-twisted-3-7/train/c
// My solution
int trade3for7(int x){
    char r[13];
    sprintf(r, "%d", x);
    for ( char* p = r; *p; p++ )
        *p = *p == '3' ? '7' : (*p == '7'? '3' : *p);
    return atoi(r);
}

int cmp(const void * a, const void * b) {
    return ( trade3for7(*(int*)a) - trade3for7(*(int*)b) );
}

int* sortTwisted37(int* array, int n){
    int* copy = malloc (n*sizeof(int));
    memcpy(copy, array, sizeof(int)*n);
    qsort(copy, n, sizeof(int), cmp);
    return copy;
}

// ...
int twister(int number) {
    int twist = 0, tens = 1, digit;
    while(number) {
        digit = number % 10;
        number /= 10;
        if     (digit == 3) digit = 7;
        else if(digit == 7) digit = 3;
        twist += digit * tens;
        tens *= 10;
    }
    return twist;
}

int comp37(const int *ain, const int *bin) {
    return   twister(abs(*ain)) * ((*ain < 0) ? -1 : 1)
           - twister(abs(*bin)) * ((*bin < 0) ? -1 : 1);
}

int* sortTwisted37(int* array, int arrayLength) {    
    int *twisted = malloc(arrayLength * sizeof(int));
    for(int i=0; i<arrayLength; i++) twisted[i] = array[i];
    qsort(twisted, arrayLength, sizeof(int), comp37);
    return twisted;
}