// https://www.codewars.com/kata/54da539698b8a2ad76000228/solutions/cpp
// My solution
#include <vector>

bool isValidWalk(std::vector<char> walk) {
    if (walk.size() != 10)
        return false;
    int x, y;
    x = y = 0;
    for (auto direction : walk) {
        switch (direction) {
        case 'n': x += 1; break;
        case 's': x -= 1; break;
        case 'w': y += 1; break;
        case 'e': y -= 1; break;
        }
    }
    return x == 0 && y == 0;
}
// ...
#include <vector>
#include <algorithm>

bool isValidWalk(std::vector<char> walk)
{
    return walk.size() == 10 and
           std::count(walk.begin(), walk.end(), 'e') == std::count(walk.begin(), walk.end(), 'w') and
           std::count(walk.begin(), walk.end(), 'n') == std::count(walk.begin(), walk.end(), 's');
}
// ...
#include <vector>

bool isValidWalk(std::vector<char> walk) {
    if (walk.size() != 10)
        return false;
    int x = 0, y = 0;
    for (char c : walk) {
        switch (c) {
        case 'n': y++; break;
        case 's': y--; break;
        case 'e': x++; break;
        case 'w': x--; break;
        }
    }
    if (x == 0 && y == 0)
        return true;
    else
        return false;
}
// ...
#include <vector>

bool isValidWalk(std::vector<char> walk)
{
    //your code here
    int ns = 0;
    int we = 0;
    for (int i = 0; i < walk.size(); i++) {
        switch (walk[i]) {
            case 'n': ns++; break;
            case 's': ns--; break;
            case 'w': we++; break;
            case 'e': we--; break;
        }
    }
    return (ns == 0 and we == 0 and walk.size() == 10);
}