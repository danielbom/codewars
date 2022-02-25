// https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/cpp
// My solution
#include <vector>
#include <string>

class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        int row_length = nFloors * 2 - 1;
        std::string row(row_length, ' ');
        std::vector<std::string> tower(nFloors, row);

        int k = row_length / 2;
        for (int i = 0; i < nFloors; i++)
        {
            tower[i][k] = '*';
            for (int j = 0; j < i; j++)
            {
                tower[i][k + j + 1] = '*';
                tower[i][k - j - 1] = '*';
            }
        }

        return tower;
    }
};
// ...
class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        std::vector<std::string> ret;
        for (int i = 0; i < nFloors; i++)
        {
            ret.push_back(std::string(nFloors - i - 1, ' ') +
                          std::string((i * 2) + 1, '*') +
                          std::string(nFloors - i - 1, ' '));
        }
        return ret;
    }
};
// ...
class Kata
{
public:
    std::vector<std::string> towerBuilder(const size_t &nFloors)
    {
        const size_t center = nFloors - 1;
        std::string floor(2 * nFloors - 1, ' ');
        std::vector<std::string> tower;
        for (size_t shift = 0; shift <= center; ++shift)
        {
            floor.replace(center + shift, 1, "*");
            floor.replace(center - shift, 1, "*");
            tower.push_back(floor);
        }
        return tower;
    }
};
// ...
class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        int n = nFloors;
        std::vector<std::string> res;

        for (auto i = 0; i < n; ++i)
        {
            res.push_back(
                std::string(n - i - 1, ' ') +
                std::string(i * 2 + 1, '*') +
                std::string(n - i - 1, ' '));
        }
        return res;
    }
};
// ...
#include <cstring>
class Kata
{
public:
    std::vector<std::string> towerBuilder(size_t nFloors)
    {
        std::vector<std::string> res{nFloors, std::string(nFloors * 2 - 1, ' ')};
        for (std::size_t i = 0; i < nFloors; ++i)
            std::memset((void *)res[i].data() + nFloors - i - 1, '*', i * 2 + 1);
        return res;
    }
};
// ...
#include <vector>
#include <algorithm>
using namespace std;

class Kata
{
public:
    vector<string> towerBuilder(int n)
    {
        int i = 1;
        vector<string> v(n);
        generate(v.begin(), v.end(), [&]() {
            string sp(n - i, ' ');
            return sp + string(i++ * 2 - 1, '*') + sp;
        });
        return v;
    }
};
#include <vector>
#include <string>

class Kata
{
public:
    std::vector<std::string> towerBuilder(int n)
    {
        std::vector<std::string> r;
        int i = 1;
        while (--n >= 0)
        {
            r.push_back(std::string(n, ' ') + std::string(i, '*') + std::string(n, ' '));
            i += 2;
        }
        return r;
    }
};
// ...
class Kata
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
        int l = nFloors * 2 - 1;
        std::string floor(l, '*');
        std::vector<std::string> tower(nFloors);
        for (int i = 0; i < nFloors; ++i)
        {
            tower[nFloors - i - 1] = floor;
            floor[i] = floor[--l] = ' ';
        }
        return tower;
    }
};