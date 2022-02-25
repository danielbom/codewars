// https://www.codewars.com/kata/twice-linear/train/python
// My solution
#include <stdlib.h>
int dblLinear(int n)
{
  int xi = 0, yi = 0;
  int *arr = calloc(n*10, sizeof(int));
  arr[0] = 1;
  int filled = 1;
  for(int i = 0; i < n; ++i)
  {
    int x = arr[xi]*2+1;
    int y = arr[yi]*3+1;
    int m = x < y ? x : y;
    arr[filled++] = m;
    if(m == x) ++xi;
    if(m == y) ++yi;
    
  }
  return arr[n];
}

// ...
#include <stdlib.h>
int dblLinear(int n) {
    int* arr = calloc(n + 2, sizeof(int));
    arr[0] = 1;
    int y, z;
    int yi = 0, zi = 0; int cnt = 0;
    while (cnt <= n) {
      y = 2 * arr[yi] + 1;
      z = 3 * arr[zi] + 1;
      cnt++;
      if(y > z) {
        arr[cnt] = z;
        zi++;
      } else if (z > y) {
        arr[cnt] = y;
        yi++;
      } else {
          arr[cnt] = y;
          yi++; zi++;
      }
    }
    int res = arr[n];
    free(arr);
    return res;
}

// ...
#include <stdlib.h>
int dblLinear(int n) {
    int i = 0, j = 0, c = 1;
    int *tab = malloc(sizeof(int) * (n + 1));
    tab[0] = 1;
    while (c <= n)
    {
      if (tab[i] * 2 + 1 == tab[j] * 3 + 1)
        tab[c++] = tab[i++] * 2 + 1 + tab[j++] * 0;
      else if (tab[i] * 2 + 1 < tab[j] * 3 + 1)
        tab[c++] = tab[i++] * 2 + 1;
      else
        tab[c++] = tab[j++] * 3 + 1;
    }
    return tab[n];
}