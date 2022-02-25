// https://www.codewars.com/kata/highest-scoring-word/train/c
// My solution
#include <string.h>

static int scoreWord(char* word) {
    int score = 0;
    for ( char* letter = word ; *letter ; letter++ ) {
        score += *letter - 'a' + 1;
    }
    return score;
}

char  *highestScoringWord(const char *str)
{
    char *copy = strdup( str );
    
    char *token = strtok( copy, " " );
    char *result = strdup( token );  // Malloc
    int highScore = scoreWord( result );
    
    while( token != NULL ) {
        int newScore = scoreWord( token );
        if ( newScore > highScore ) {
            free( result );  // Free
            result = strdup( token ); // Malloc
            highScore = newScore;
        }
        token = strtok( NULL, " " );
    }
    free( copy );
    return result;
}