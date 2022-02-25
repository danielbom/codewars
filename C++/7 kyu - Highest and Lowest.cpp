// https://www.codewars.com/kata/554b4ac871d6813a03000035/train/cpp
// My solution
#include <string>
#include <sstream>
#include <iostream>

std::string highAndLow(const std::string& numbers){
    std::stringstream stream(numbers);
    std::string number;
    int max = 0;
    int min = 0;
    int count = 0;
    while (std::getline(stream, number, ' ')) {
        int x = std::stoi(number);
        if (count == 0) max = min = x;
        if (x > max) max = x;
        if (x < min) min = x;
        count++;
    }
    return std::to_string(max) + " " + std::to_string(min);
}
// ...
#include <string>
#include <sstream>
#include <limits>

std::string highAndLow(const std::string& numbers){
    std::stringstream ss(numbers);
    int temp;
    int min = std::numeric_limits<int>::max();
    int max = std::numeric_limits<int>::min();
    while (ss >> temp) {
        min = (temp < min) ? temp : min;
        max = (temp > max) ? temp : max;
    };
    return std::to_string(max) + " " + std::to_string(min);
}
// ...
#include <algorithm>
#include <iterator>
std::string highAndLow(const std::string& numbers){
    std::istringstream in(numbers);
    auto minmax = std::minmax_element(
        std::istream_iterator<int>(in),
        std::istream_iterator<int>());
    std::stringstream out;
    out << *minmax.second << ' ' << *minmax.first;
    return out.str();
}
// ...
#include <string>
#include <sstream>

std::string highAndLow(const std::string& numbers){
    std::istringstream in(numbers);
    const auto [min, max] = std::minmax_element(
        std::istream_iterator<int>(in),
        std::istream_iterator<int>());
    std::ostringstream out;
    out << *max << ' ' << *min;
    return out.str();
}
// ...
#include <string>
#include <sstream>

std::string highAndLow(const std::string& numbers){
    std::istringstream numberStream{numbers};
    std::vector<int> vNumbers;
    int currentNumber;
    
    while(numberStream>>currentNumber){
        vNumbers.push_back(currentNumber);
    }
    
    std::sort(vNumbers.begin(), vNumbers.end());
    
    return std::to_string(vNumbers.back()) + " "+std::to_string(vNumbers.front());
}
// ...
#include <string>
#include <vector>

std::string highAndLow(const std::string& numbers) {
    std::vector<int> nums;
    std::istringstream iss(numbers);
    std::copy(std::istream_iterator<int>(iss), {}, std::back_inserter(nums));
    auto [min, max] = std::minmax_element(std::begin(nums), std::end(nums));
    return std::to_string(*max) + " " + std::to_string(*min);
}