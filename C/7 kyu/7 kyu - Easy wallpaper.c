// https://www.codewars.com/kata/easy-wallpaper/train/r
// My solution
#include <math.h>

const char* wallPaper(double l, double w, double h)
{
    static const char *const numbers[21] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"};
    
    if(l == 0 || w == 0 || h == 0) return numbers[0];

    double extra_length = 1.15; // percent
    l *= extra_length;
    w *= extra_length;
    double wall_area = ( l * h * 2 ) + ( w * h * 2 ); // square meters

    double standard_width_of_roll = 0.52;  // meters
    double standard_length_of_roll = 10.0; // meters
    double roll_area = standard_width_of_roll * standard_length_of_roll; // square meters
    
    int rolls = ceil(wall_area / roll_area);
    
    return numbers[rolls];
}

// ...
#include <math.h>

char* wallPaper(double l, double w, double h)
{
    char *numbers[21] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"};
    if (l == 0 || w == 0 || h == 0)
        return "zero";
    double r = (( (l + w) * 2 * h) / 5.2) * 1.15;
    return numbers[(long)ceil(r)];
}