// https://www.codewars.com/kata/56c04261c3fcf33f2d000534/train/c
// My solution
#include <math.h>

double v(int k, int n) {
  //                    1
  // v(k, n) = ----------------------  
  //           k * (n + 1) ** (2 * k)  
  double expoent = 2.0 * k;
  double base = n + 1.0;
  double power = pow(base, expoent);
  double numerator = 1.0;
  double denominator = k * power;
  return numerator / denominator;
}


double doubles(int maxk, int maxn) {
  double sum = 0.0;
  for (int k = 1; k <= maxk; k++) 
    for (int n = 1; n <= maxn; n++) 
      sum += v(k, n);
  return sum;
}

// And
#include <math.h>

double v(int k, int n) {
  //                    1
  // v(k, n) = ----------------------  
  //           k * (n + 1) ** (2 * k)  
  double expoent = 2.0 * k;
  double base = n + 1.0;
  double power = pow(base, expoent);
  double numerator = 1.0;
  double denominator = k * power;
  return numerator / denominator;
}

double doubles(int maxk, int maxn) {
  double sum = 0.0;
  for (int k = 1; k <= maxk; k++) {
    for (int n = 1; n <= maxn; n++) {
      double result = v(k, n);
      if (result <= 1E-16) break;
      sum += result;
    }
  }
  return sum;
}

// ...
#include <math.h>

double doubles(int maxk, int maxn) {
  double res = 0;
  
  for(auto i = 1; i <= maxk; i++)
    for(auto j = 1; j <= maxn; j++)
      res += 1.0 / (i * pow(j+1, 2*i)); 

  return res;
}

// ...
#include <math.h>

double doubles(int maxk, int maxn) {
  double *uNarr = (double *) calloc(maxn, sizeof(double));
  double *kNarr = (double *) calloc(maxn, sizeof(double));
  
  double u = 0.0;
  double s = 0.0;

  for (int k = 1; k <= maxk; k++) {
    u = 0.0;
    for (int n = 1; n <= maxn; n++) {
      if (k == 1) {
        uNarr[n - 1] = pow((double)(n + 1.0), 2.0);
        kNarr[n - 1] = uNarr[n - 1];
        u += (1.0 / uNarr[n - 1]);
        continue;
      }
      kNarr[n - 1] *= uNarr[n - 1];
      u += (1.0 / kNarr[n - 1]);
    }

    u /= (double) k; 
    s += u;
  }

  free(kNarr);
  free(uNarr);
  return s;
}

// ...
#include <math.h>

#define EPS 1e-16

double doubles(int maxk, int maxn) {
  double sum = 0;
  
  for (double k = 1; k <= maxk; k++) { 
    for (double n = 1; n <= maxn; n++) {
      double increment = pow(n + 1, -2 * k) / k;
      if (increment < EPS) break;
      sum += increment;
    }
  }
  return sum;
}
