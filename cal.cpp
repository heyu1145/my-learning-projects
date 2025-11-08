#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);

  int n, b, max = -1e8;
  int total = 0;
  int min = 1e8;

  cin >> n;
  if (n == 1) {
    cin >> b;
    max = b;
    min = b;
    total = b;
    goto skip;
  }
  for (int i = 0; i < n; i++) {
    cin >> b;
    total += b;
    if (b > max) {
      max = b;
    }
    if (b < min) {
      min = b;
    }
  }
skip:
  cout << max << ' ' << min << ' ' << total << ' ' << total / n << "\n";
}
