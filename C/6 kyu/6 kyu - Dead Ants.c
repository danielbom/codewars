// https://www.codewars.com/kata/dead-ants/train/c
// My solution
#include <stdio.h>

int countOccurrencesOfAnt(const char* ants){
  char* ant = "ant\0", *p;
  int count = 0;
  for(p = ants; *p; p++){
    char* f = strstr(p, ant);
    if(f){
      p = f+2;
      count++;
    }
  }
  return count;
}

int max3(int a, int b, int c){
  int maior = a;
  if(maior < b) maior = b;
  if(maior < c) maior = c;
  return maior;
}

int deadAntCount(const char* ants){
  int count = countOccurrencesOfAnt(ants);
  int a, n, t;
  a = n = t = 0;
  for(char* p = ants; *p; p++){
    if(*p == 'a') a++;
    else if(*p == 'n') n++;
    else if(*p == 't') t++;
  }
  return max3(a,n,t) - count;
}

// ...
int deadAntCount(const char* ants){
    printf("Str:%s | ", ants); 
    int dead_ants = 0;
    int no_of_ants[] = {0, 0, 0};
    while(*ants){
        if(isalpha(*ants)){
            if(*ants == 'a' && *(ants+1) == 'n' && *(ants+2) == 't'){
                ants += 2; 
            }
            else if (*ants == 'a')
                no_of_ants[0]++;
            else if (*ants == 'n')
                no_of_ants[1]++;
            else if (*ants == 't')
                no_of_ants[2]++;
            ants++;
        }
        else
            ants++;
    }
    dead_ants = no_of_ants[0] > no_of_ants[1] ? no_of_ants[0] : no_of_ants[1];
    dead_ants = no_of_ants[2] > dead_ants ? no_of_ants[2] : dead_ants ;
    return dead_ants;
}

// ...
#include <assert.h>
#include <string.h>

int count(const char *haystack, const char *needle)
{
    assert(haystack);
    assert(needle);
    int result = 0;
    for (const char *cp = strstr(haystack, needle); cp; cp = strstr(cp + 1, needle))
        ++result;
    return result;
}

int deadAntCount(const char* ants)
{
    assert(ants);
    int a = count(ants, "a"), n = count(ants, "n"), t = count(ants, "t");
    int max = (a > n)? (a > t)? a : (n > t)? n : t : (n > t)? n : t;
    return max - count(ants, "ant");
}
