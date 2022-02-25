// https://www.codewars.com/kata/caesars-cypher-2/train/c
// My solution
char jump13(char c){
    char r = c;
    if(c >= 'a' && c <= 'z'){
        for(int i=0; i<13; i++){
            r++;
            if(r > 'z') r = 'a';
        }
    }
    else if(c >= 'A' && c <= 'Z'){
        for(int i=0; i<13; i++){
            r++;
            if(r > 'Z') r = 'A';
        }
    }
    return r;
}

void rot13(char* str, int tam){
    for(int i=0; i<tam; i++){
        str[i] = jump13(str[i]);
    }
}

// ...
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
 
void rot13(char *s) {
    char *p=s; int up;
    while(*p) {
        up = toupper(*p);
        if (up >= 'A' && up <= 'M') *p+=13;
        else if(up >='N' && up <= 'Z') *p-=13;
        ++p;
    }
}

// ...
#include <ctype.h>
#include <stddef.h>

void rot13(char* str, int stringSize)
{
    for(size_t i = 0; i < stringSize - 1; i++)
    {
        if (!isalpha(str[i]))
        {
            continue;
        }
    
        if (islower(str[i]))
        {
            str[i] = (str[i] % 97 + 13) % 26 + 97;
        }
        else
        {
            str[i] = (str[i] % 65 + 13) % 26 + 65;
        }
    }
}

// ...
static const int ROTATE_13 = 13;
static const int ALPHABET_SIZE = 26;

void rot13(char* str, int len) {
    for (int i = 0; i < len; i++) {
        int ltr = str[i];
        if (isalnum(ltr)) {
            if (isupper(ltr)) {
                ltr -= 'A';
                ltr += ROTATE_13;
                ltr %= ALPHABET_SIZE;
                ltr += 'A';
                str[i] = ltr;
            } else {
                ltr -= 'a';
                ltr += ROTATE_13;
                ltr %= ALPHABET_SIZE;
                ltr += 'a';
                str[i] = ltr;
            }
        }
    }
}

// ...
