// https://www.codewars.com/kata/eliminate-the-intruders-bit-manipulation/train/c
// My solution
long eliminate_unset_bits(const char* number){
    long r = 0, k = 1;
    for( int i = 0; number[i]; i++) {
        if (number[i] == '1') {
            r += k;
            k <<= 1;
        }
    }
    return r;
}

// ...
long eliminate_set_bits(const char *number) {
    int n = 0;
    while (*number)
        n += *number++ == '1';
    return (1l << n) - 1;
}

// ...
long eliminate_set_bits(const char* number) {
    int ones = 0;
    for (int i = 0; i < strlen(number); i++)
        if (number[i] == '1') ones++;
    return (long)pow(2, ones) - 1;
}

// ...
long eliminate_unset_bits(const char* number) {
    long ret = 0;
    for (const char *d = number; *d; d++)
        if (*d == '1')
            ret = ret << 1 | 1;
    return ret;  
}