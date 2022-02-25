// https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/cpp
// My solution
#include <vector>

std::vector<int> invert(std::vector<int> values)
{
    std::vector<int> inverted;
    for (int value : values)
        inverted.push_back(-value);
    return inverted;
}
// ...
#include <vector>
#include <algorithm>
#include <functional>

std::vector<int> invert(std::vector<int> values)
{
    transform(values.begin(), values.end(), values.begin(), std::negate<int>());
    ;
    return values;
}