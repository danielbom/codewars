// https://www.codewars.com/kata/scramblies/train/c
// My solution
#include <stdbool.h>

bool scramble(const char *str1, const char *str2)
{
    int bitmap[26] = {0};
    char *ptr;
    // bitmap: Estrutura de dados para contar os caracteres da 'str1' de forma eficiente
    // ptr: Ponteiro para se deslocar pelas strings
    
    for(ptr = str1; *ptr; ptr++) // Contando os caracteres da string
        ++bitmap[*ptr - 'a'];

    // Verificando se existe caracteres suficientes na string 'str1' para se obter
    // string 'str2'
    for(ptr = str2; *ptr; ptr++)
    {
        if(bitmap[*ptr - 'a'] == 0) return false;
        else --bitmap[*ptr - 'a']; // Caso tenha o caracter, é necessário descontá-lo
    }
    
    return true;
}

// ...
#include <limits.h>
#include <stdbool.h>

bool scramble(const char *str1, const char *str2)
{
    int count1[CHAR_MAX - CHAR_MIN + 1] = {0};
    for (; *str1; ++str1) ++count1[*str1 - CHAR_MIN];
    for (; *str2; ++str2)
        if (--count1[*str2 - CHAR_MIN] < 0)
            return false;
    return true;
}

// ....
#include <stdbool.h>
#include <string.h>

bool scramble(const char *str1, const char *str2)
{
    int* alp = calloc(26, sizeof(int));
    for(int j = 0; str1[j]; j++) 
        alp[str1[j] - 'a']++;
    for(int j = 0; str2[j]; j++)
        alp[str2[j] - 'a']--;
    for(int j = 0; j < 26; j++)
        if(alp[j] < 0) return false;
    return true;
}