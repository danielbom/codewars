// https://www.codewars.com/kata/convert-to-binary/train/c
// My solution
unsigned long long to_binary(unsigned short num) {
    unsigned long long result = 0, mul = 1;
    while (num) {
        result += num % 2 != 0 ? mul : 0;
        mul *= 10;
        num /= 2;
    }
    return result;
}
// ...
unsigned long long to_binary(unsigned long long num)
{
    unsigned long long b = 0;
    unsigned long long x = 1;
    while (num > 0){
        b += (num & 1) * x;
        x *= 10;
        num >>= 1;
    }
    return b;
}
// ...
unsigned long long to_binary(unsigned short num)
{
    if (num == 1 || num == 0)
        return (num);
    return (num % 2 + 10 * to_binary(num / 2));
}