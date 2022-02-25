// https://www.codewars.com/kata/alphabet-war-airstrike-letters-massacre/train/python
// My solution
#include <string.h>

int attack_power(char l)
{
    char dark_side[4] = "sbpw";  // (Left) Negative win
    char light_side[4] = "zdqm"; // (Right) Positive win
    for(int i = 0; i < 4; i++)
    {
        if(l == dark_side[i]) return -(i+1);
        else if(l == light_side[i]) return i+1;
    }
    return 0;
}

char *alphabet_war(const char *fight)
{
    size_t length = strlen(fight);
    int points = 0;
    if(length == 1)
        points = attack_power(fight[0]);
    else if(length == 2 && fight[0] != '*' && fight[1] != '*')
        points = attack_power(fight[0]) + attack_power(fight[1]);
    else
    {
        if(fight[0] != '*' && fight[1] != '*')
            points += attack_power(fight[0]);
        if(fight[length-1] != '*' && fight[length-2] != '*')
            points += attack_power(fight[length-1]);
    
        for(char* ptr = fight + 1; *(ptr + 1); ptr++)
            points += *(ptr - 1) != '*' && *(ptr + 1) != '*' ? attack_power(*ptr) : 0;
    }
    
    if(points > 0) return "Right side wins!";
    if(points < 0) return "Left side wins!";
    return "Let's fight again!";
}

// And
int attack_power(char l)
{
    char dark_side[4] = "sbpw";  // (Left) Negative win
    char light_side[4] = "zdqm"; // (Right) Positive win
    for(int i = 0; i < 4; i++)
    {
        if(l == dark_side[i]) return -(i+1);
        if(l == light_side[i]) return i+1;
    }
    return 0;
}
char *alphabet_war(const char *fight)
{
    int points = 0;
    for ( char* ptr = fight; *ptr; ++ptr )
    {
        if ( *(ptr+1) == '*' ) continue;
        if ( *ptr == '*' && *(ptr+1) && ptr++) continue;
        points += attack_power(*ptr);
    }
    if(points > 0) return "Right side wins!";
    if(points < 0) return "Left side wins!";
    return "Let's fight again!";
}
// ...
char *alphabet_war(const char *fight)
{
    static const char alpha[] = { 'w', 'p', 'b', 's', 'z', 'd', 'q', 'm' };
    static const int power[] =  { -4,  -3,  -2,  -1,   1,   2,   3,   4  };
    unsigned i, n = sizeof alpha;
    int score;
    for (score=0; *fight; ++fight) {
        if (*(fight+1) == '*')
            continue;
        else if (*fight == '*') {
            if (*(fight+1))
                ++fight;
            continue;
        }
        for (i=0u; i < n; ++i) {
            if (*(alpha+i) == *fight) {
                score += *(power+i);
                break;
            }
        }
    }
    return !score ? "Let's fight again!" : score > 0 ? "Right side wins!" : "Left side wins!";
}