// https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/cpp
// My solution
#include <vector>
#include <numeric>

int sum(std::vector<int> nums) {
    return std::accumulate(nums.begin(), nums.end(), 0);
}

// ...
#include <vector>

int sum(std::vector<int> nums) {
    int count = 0;
    for (int &i : nums)
        count += i;
    return count;
}