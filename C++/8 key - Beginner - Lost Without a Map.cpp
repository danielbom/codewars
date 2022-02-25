// https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/cpp
// My solution
#include <vector>

std::vector<int> maps(const std::vector<int> &values)
{
    std::vector<int> twofold;
    for (auto value : values)
        twofold.push_back(value * 2);
    return twofold;
}
// ...
#include <vector>
#include <algorithm>

std::vector<int> maps(const std::vector<int> &values)
{
    std::vector<int> v(values.begin(), values.end());
    std::transform(v.begin(), v.end(), v.begin(), [](int x) {
        return 2 * x;
    });
    return v;
}
