// https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/cpp
// My solution
std::vector<int> digitize(unsigned long n) {
    std::vector<int> digits;
    while(n > 0) {
        digits.push_back(n % 10);
        n = n / 10;
    }
    return digits;
}

// ...
std::vector<int> digitize(unsigned long n) {        
    std::vector<int> rod;
    do {
        rod.push_back(n % 10);
    } while (n /= 10);
    return rod;
}

// ...
#include <vector>
#include <string>
using namespace std;

vector<int> digitize(unsigned long n) {
    vector<int> result;
    string digits = to_string(n);
    for (int i = digits.length()-1; i >= 0; i--) {
        int item = digits[i]-'0';
        result.push_back(item);
    }
    return result;
}

// ...
