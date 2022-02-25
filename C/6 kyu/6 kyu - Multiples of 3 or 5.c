// https://www.codewars.com/kata/multiples-of-3-or-5/train/c
// My solution
int soma_i(int n){
  if(n <= 0) return 0;
  return (n*n + n)/2;
}

int solution(int n) {
    return soma_i((n-1)/3)*3 + soma_i((n-1)/5)*5 - soma_i((n-1)/15)*15;
}

// ...
int solution(int number) {
    int sum = 0;
    for(int i = 0; i < number; i++)
        if( (i % 3) == 0 || (i % 5) == 0)
            sum += i;
    return sum;
}

// ...
int sum(int mult, int n)
{
    return mult * n * (n + 1) / 2;
}

int solution(int number)
{
    int n3 = number / 3;
    int n5 = number / 5;
    int n15 = number / 15;

    int m3 = number % 3;
    int m5 = number % 5;

    if (m3 == 0) --n3;
    if (m5 == 0) --n5;
    if (m3 == 0 && m5 == 0) --n15;

    return sum(3, n3) + sum(5, n5) - sum(15, n15);
}

// ...
/*
 * 计算等差数列
 */
int accumulate(int base, int count)
{
    return (base + base * count) * count / 2;
}

int solution(int number)
{
    int sum = 0, numberSubOne = number - 1;
    sum += accumulate(3, numberSubOne / 3);
    sum += accumulate(5, numberSubOne / 5);
    sum -= accumulate(15, numberSubOne / 15);
    return sum;
}