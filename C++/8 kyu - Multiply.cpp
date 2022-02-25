// https://www.codewars.com/kata/multiply/train/cpp
// My solution
int multiply(int a, int b)
{
    return a * b;
}

// ...
auto multiply = [](int a, int b) { return a*b; };

// ...
#include <functional>

std::multiplies<int> multiply;

// ...
template <class T>
inline const T multiply(const T a, const T b)
{
    return a * b;
}

// ...
template <class T>
T multiply(T a,T b){
    return a * b;
}

