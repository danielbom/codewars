// https://www.codewars.com/kata/two-to-one/train/c
// My solution
static int contains( char *str, char chr ) {
    for ( ; *str ; str++ )
        if ( *str == chr )
            return 1;
    return 0;
}

char* longest(char* s1, char* s2) {
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    char *result = calloc( 27, sizeof( char ) ) ;
    int n = 0;
    for ( char *alpha = alphabet; *alpha; alpha++ )
        if ( contains( s1, *alpha ) || contains( s2, *alpha ) )
            result[n++] = *alpha;
    return result;
}

// And
char* longest(char* s1, char* s2) {
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    char *result = calloc( 27, sizeof( char ) ) ;
    int n = 0;
    for ( char *alpha = alphabet; *alpha; alpha++ )
        if ( strchr( s1, *alpha ) || strchr( s2, *alpha ) )
            result[n++] = *alpha;
    return result;
}
// And
char* longest(char* s1, char* s2) {
    char *result = calloc( 27, sizeof( char ) ) ;
    int n = 0;
    for ( char alpha = 'a'; alpha <= 'z'; alpha++ )
        if ( strchr( s1, alpha ) || strchr( s2, alpha ) )
            result[n++] = alpha;
    return result;
}

// ...
char* longest(char* s1, char* s2) {
    char letters [26] = {0}, *temp, *final = temp = (char *) calloc(sizeof(char), 26);;
    while(*s1) letters[*(s1++) - 'a']++;
    while(*s2) letters[*(s2++) - 'a']++;
    
    for(int i = 0; i < 26; i++)
        if(letters[i])
            *(temp++) = 'a' + i;
        
    return final;
}
// ...
