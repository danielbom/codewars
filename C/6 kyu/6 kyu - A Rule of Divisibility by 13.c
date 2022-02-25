// https://www.codewars.com/kata/a-rule-of-divisibility-by-13/train/c
// My solution
#define LL long long

LL sum_sequence(LL num)
{
    LL sequence[6] = {1L,10L,9L,12L,3L,4L}, sum = 0L;
    int length_sequence = 6;

    for(int i = 0; num; ++i)
    {
        sum += (num % 10) * sequence[i % length_sequence];
        num /= 10;
    }
    return sum;
}
        
LL thirt(LL n)
{
    LL previous = sum_sequence(n);
    for(int i = 0; i < 100 && previous != n; ++i)
    {
        n = previous;
        previous = sum_sequence(n);
    }
    return n;
}

// And
#define LL long long
LL sum_seq(LL num)
{
    static LL sequence[6] = {1L,10L,9L,12L,3L,4L};
    static int i = -1, n = 6;
    return (num % 10) * sequence[(i = (i + 1) % n)] + (num == 0 ? i=-1,0 : sum_seq(num/10));
}
LL thirt(LL n)
{
    LL p = sum_seq(n);
    while((n = p) != (p = sum_seq(n)));
    return n;
}

// ...
long long thirt(long long n)
{
    int remainders[6] = {1, 10, 9, 12, 3, 4};
    int iRem = 0;
    long long m = n, sum = 0;
    
    while (n > 0)
    {
      sum += (n % 10) * remainders[iRem++];
      n /= 10;
      if (iRem >= 6) iRem = 0;
    }
    
    return (sum == m)?(m):(thirt(sum));
}