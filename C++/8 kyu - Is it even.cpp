// https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/cpp
// My solution
#include <math.h>

bool is_even(double n) {
    double number, fractpart, intpart;
    number = std::abs(n);
    fractpart = modf(number, &intpart);
    return fractpart == 0 && (int)std::abs(intpart) % 2 == 0;
}
// ...
#include <cmath>

bool is_even(double n) {
    return fmod(n, 2) == 0;
}
// ...
#include <cmath>
bool is_even(double n) {
    if (ceil(n) != floor(n))
        return false;
    return ((int)n) % 2 == 0;
}