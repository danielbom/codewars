// https://www.codewars.com/kata/alphabet-war/train/c
// My solution
static int attack_power(char letter)
{
    char dark_side[5]  = "sbpw"; // (Left)  Negative wins
    char light_side[5] = "zdqm"; // (Right) Positive wins
    for(int i = 0; i < 5; i++)
    {
        if(letter == dark_side[i]) return -(i+1);
        if(letter == light_side[i]) return i+1;
    }
    return 0;
}

char *alphabet_war(const char *fight)
{
    int points = 0;
    for(char* ptr = fight; *ptr; ptr++)
        points += attack_power(*ptr);
    
    if(points > 0) return "Right side wins!";
    if(points < 0) return "Left side wins!";
    return "Let's fight again!";
}

// ...
char *alphabet_war(const char *fight)
{
    int score = 0;
    while (*fight) {
        switch (*fight++) {
            case 'w': score -= 4; break;
            case 'p': score -= 3; break;
            case 'b': score -= 2; break;
            case 's': --score; break;
            case 'z': ++score; break;
            case 'd': score += 2; break;
            case 'q': score += 3; break;
            case 'm': score += 4; break;
        }
    }
    return !score ? "Let's fight again!" : score > 0 ? "Right side wins!" : "Left side wins!";
}

// ...
char *alphabet_war(const char *fight)
{
    int left = 0,right = 0;
    char letters [26] = {0};
    while(*fight)letters[*(fight++) - 'a']++;        
    left = letters[22] * 4 + letters[15] * 3 + letters[1] * 2 +letters[18]; //w,p,b,s
    right = letters[12] * 4 + letters[16] * 3 + letters[3] * 2 +letters[25];//m,q,d,z
    if(left == right) return "Let's fight again!";
    else if(left > right) return "Left side wins!";
    else return "Right side wins!";
}

// ...
char *alphabet_war(const char *fight)
{
    char *left = "sbpw";
    char *right = "zdqm";
    int res = 0;
    
    for(int i = 0; i < strlen(fight); i++) {
      res += strchr(left, fight[i]) ? strchr(left, fight[i]) - left + 1 : 0;
      res -= strchr(right, fight[i]) ? strchr(right, fight[i]) - right + 1 : 0;
    }
    
    if(res > 0) return "Left side wins!";
    if(res < 0) return "Right side wins!";
    
    return  "Let's fight again!";
}

// ...
#include <string.h>

struct letter_scores {
  int   score;
  char  letter;
};

#define FIGTHER_LETTERS_MAX  (8u)

const struct letter_scores scores[] =
    { {-4,'w'}, {-3,'p'}, {-2,'b'}, {-1,'s'},
      {4,'m'}, {3,'q'}, {2,'d'}, {1,'z'} };

static inline int letter_get_score(char * letter)
{
  int res = 0;
  for (size_t idx = 0; idx < FIGTHER_LETTERS_MAX; idx ++)
    if (scores[idx].letter == *letter)
    {
      res = scores[idx].score;
      break;
    }
  return res;
}

static const char * str_lwins = "Left side wins!";
static const char * str_rwins = "Right side wins!";
static const char * str_draw = "Let's fight again!";

char *alphabet_war(const char *fight)
{
  int res = 0;
  
  for (size_t idx = 0; idx < strlen(fight); idx ++)
    res += letter_get_score(&fight[idx]);
  
  return (res < 0) ? str_lwins : (res > 0) ? str_rwins : str_draw;
}