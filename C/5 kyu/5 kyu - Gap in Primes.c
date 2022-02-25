// https://www.codewars.com/kata/gap-in-primes/train/c
// My solution
#include <stdbool.h>
#include <stdlib.h>

bool prime(int num, int mod){
    if (num < mod*mod )  return true;
    if ( num%mod == 0 ) return false;
    return mod == 2 ? prime(num, 3) : prime(num, mod+2);
}

bool is_prime(int num){
    return prime(num, 2);
}

long long* gap(int g, long long m, long long n) {
    int i, p; // variaveis temporarias
    long long *r = (long long*) calloc (2, sizeof(long long)); // retorno
    
    for(i=m; i<=n; i++)
        if(is_prime(i))
            break;
    // primeiro primo
    p = i;
    // buscando o gap
    for(;i<=n;i++)
        if(is_prime(i)){
            if(i-p == g) break;
            p = i;
        }
    // se encontrou altera a resposta
    if(i-p == g && i != n+1){
        r[0] = p;
        r[1] = i;
    }
    return r;
}

// ...
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isPrime(long long n) {
  if (n % 2 == 0) return false;
  for (int i = 3; i * i <= n ; i += 2)
    if (n % i == 0) return false;
  return true;
}
long long* gap(int g, long long m, long long n) {
    long long* candidates = (long long*)calloc(2, sizeof(long long));
    candidates[0] = 0; candidates[1] = 0;
    long long i = m;
    for (; i <= n; i++) {
        if (candidates[1] - candidates[0] == (long long)g) {
            return candidates;
        }
        if (isPrime(i)) {
            candidates[0] = candidates[1];
            candidates[1] = i;
        }
    }
    candidates[0] = 0; candidates[1] = 0;
    return candidates;
}