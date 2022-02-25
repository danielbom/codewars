// https://www.codewars.com/kata/roman-numerals-encoder/train/c
// My solution
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *solution(int n) {
    if(n < 0 || n > 5000) return "";

    char* r = calloc(15,sizeof(char));
    char* p = r;
    while(n>0){
        if(n >= 1000 ){
            *p++ = 'M';
            n -= 1000;
        }
        else if(n >= 500){
            if(n < 900){
                *p++ = 'D';
                n -= 500;
            }
            else{
                *p++ = 'C'; *p++ = 'M';
                n -= 900;
            }
        }
        else if(n >= 100){
            *p++ = 'C';
            if(n < 400){
                n -= 100;
            }
            else{
                *p++ = 'D';
                n -= 400;
            }
        }
        else if(n >= 50){
            if(n < 90){
                *p++ = 'L';
                n -= 50;
            }
            else{
                *p++ = 'X'; *p++ = 'C';
                n-= 90;
            }
        }
        else if(n >= 10){
            *p++ = 'X';
            if(n < 40){
                n -= 10;
            }
            else{
                *p++ = 'L';
                n -= 40;
            }
        }
        else if(n >= 5){
            if(n < 9){
                *p++ = 'V';
                n -= 5;
            }
            else{
                *p++ = 'I'; *p++ = 'X';
                n -= 9;
            }
        }
        else{
            *p++ = 'I';
            if(n < 4){
                n -= 1;
            }
            else{
                *p++ = 'V';
                n -= 4;
            }
        }
    }
    
    return r;
}

// ...
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *solution(int n) {
    // Your code here
    char *re;
    re=(char*)calloc(sizeof(char),50);
    int base[13]={ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    char* str[13]={ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                    "V", "IV", "I"};
    int i=0;
    while(n!=0){
        if(n>=base[i]){
            n-=base[i];
            strcat(re,str[i]);
        }else{
            i++;
        }
    }
    return re;
}

// ...
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *solution(int n) {
    char *re = (char*)calloc(50, sizeof(char));
    int base[13]={ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    char* str[13]={ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX",
                    "V", "IV", "I"};
    
    for(int i = 0; n!=0; i++)
        while(n>=base[i] && (n = n - base[i])+1)
            strcat(re,str[i]);
    return re;
}

// ...
#include <stdio.h>

char *solution(int n) {
    static const char *const roman_num[4][10] = {
        {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" },
        {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" },
        {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" },
        {"", "M", "MM", "MMM" }
    };
    static char buf[32];
    
    sprintf(buf, "%s%s%s%s", roman_num[3][n / 1000],
                            roman_num[2][n / 100 % 10],
                            roman_num[1][n / 10 % 10],
                            roman_num[0][n % 10]);
    return buf;
}