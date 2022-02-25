// https://www.codewars.com/kata/mumbling/train/c
// My solution
#include <string.h>
#include <stdlib.h>

int soma_i(int n);
char *accum(const char *source);
char *mult(const char c, int n);
//char *accum(const char *source);
int soma_i(int n){
    return (n*n + n) / 2;
}
char *mult(const char c, int n){
    char* m = malloc(n+1);
    m[0] = toupper(c);
    char cl = tolower(c);
    for(int i=1; i<n; i++) m[i] = cl;
    m[n] = '\0';
    return m;
}
char *accum(const char *source){
    int tam = strlen(source);
    char* retorno = malloc( soma_i(tam)+tam );
    retorno[0] = '\0';
    // Primeira letra
    char *tmp = mult(source[0], 1);
    strcat(retorno, tmp);
    free(tmp);
    // Letras seguintes antecedidas por traco '-'
    for(int i = 1; source[i]; i++){
        tmp = mult(source[i], i+1);
        strcat(retorno, "-\0");
        strcat(retorno, tmp);
        free(tmp);
    }
    return retorno;
}

// ...
#include <malloc.h>
#include <string.h>
#include <ctype.h>

char *accum(const char *source) {
    int len = strlen(source);
    char *str = (char*)malloc(len * (len + 1));
    int i = 0;

    for (int j = 0; j < len; j++, i++) {
        for (int k = 0; k < (j + 1); k++, i++) str[i] = !k ? toupper(source[j]) : tolower(source[j]);
        str[i] = '-';
    }
    str[i-1] = '\0';
    return str;
}

// ...
char *accum(const char *sc) {
    int s = (3 + strlen(sc)) * strlen(sc) / 2;
    char* str = malloc(s);
    for (int i = 0, sci = 0; i < s; i++, sci++) {
        str[i] = toupper(sc[sci]);
        for (int j = 0; j < sci; j++) {
            str[++i] = tolower(sc[sci]);
        }
        str[++i] = '-';
    }
    str[s - 1] = '\0';
    return str;
}
