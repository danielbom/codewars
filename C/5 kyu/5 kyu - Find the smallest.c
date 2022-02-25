// https://www.codewars.com/kata/find-the-smallest/train/c
// My solution
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;

static void shifting_digit( char* str, int from, int to )
{
    char digit = str[from];
    if ( from < to ) // Insertion Sort, 1 step
    {
        for ( int k = from+1; k <= to; k++ )
            str[k-1] = str[k];
    }
    else // Insertion Sort Reverse, 1 step
    {
        for ( int k = from-1; k >= to; k-- )
            str[k+1] = str[k];
    }
    str[to] = digit;
}

ll* smallest( ll n ) {
    struct result {
        ll value, from, to;
    } *res = calloc(1, sizeof(struct result)), local;
    res->value = n;
    
    char buffer[20], copy[20];
    sprintf( buffer, "%lld", n ); // Casting
    strcpy( copy, buffer );       // Record
    
    int length = strlen( buffer );
    for ( local.from = 0; local.from < length; local.from++ )
    {
        for ( local.to = 0; local.to < length; local.to++ )
        {
            shifting_digit( buffer, local.from, local.to ); // Changing
            sscanf( buffer, "%lld", &local.value );         // Casting
            if ( local.value < res->value && local.from != local.to+1)
                memcpy(res, &local, sizeof(struct result));
            strcpy( buffer, copy );                         // Restore
        }
    }
    return res;
}

// Other ways
#include <stdlib.h>

int countDigits(long long n);
long long moveDigit(long long n, int i, int j, int totalDigits);
long long calcMultiplierForDigit(int digit, int totalDigits);

long long* smallest(long long n)
{
  int totalDigits = countDigits(n);
  long long smallest = n;
  int smallestI = 1;
  int smallestJ = 1;
  
  // Loop through the digits to try taking
  for (int i = 1; i <= totalDigits; ++i)
  {
    // Loop through the digit positions where we'll put it
    for (int j = 1; j <= totalDigits; ++j)
    {
      long long test;
      
      if(j == i)
        continue;
      
      test = moveDigit(n, i, j, totalDigits);

      if(test < smallest)
      {
        smallest = test;
        smallestI = i;
        smallestJ = j;
      }
    }
  }
  
  long long * result = malloc(sizeof(long long) * 3);
  if(!result)
    return NULL;
    
  result[0] = smallest;
  result[1] = smallestI - 1;
  result[2] = smallestJ - 1;
  
  return result;
}

int countDigits(long long n)
{
  int digits = 1;
  while(n > 10)
  {
    n /= 10;
    ++digits;
  }
  
  return digits;
}

long long moveDigit(long long n, int i, int j, int totalDigits)
{
  // Take digit from position 'i' and insert it at position 'j'

  // Calculate the multiplier for the digit positions
  long long iMult = calcMultiplierForDigit(i, totalDigits);
  long long jMult = calcMultiplierForDigit(j, totalDigits);
      
  // Determine the value of the selected digit 'i'
  long long iValue = (n / iMult) % 10;
      
  // Split the sequence below and above digit 'i'
  long long below = n % iMult;
  long long above = n / (iMult * 10);
  
  // Reconstruct the number, with digit 'i' removed
  n = below + (above * iMult);  

  // Split the sequence below and at insertion point 'j'
  below = n % jMult;
  above = n / jMult;

  // Insert digit value at position 'j'  
  n = below + (above * jMult * 10) + (iValue * jMult);
      
  return n;
}

long long calcMultiplierForDigit(int digit, int totalDigits)
{
  long long mult = 1;
  
  for(int i = totalDigits; i > digit; --i)
    mult *= 10;
    
  return mult;
}