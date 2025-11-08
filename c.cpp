#include <climits>
#include <cstdio>
#include <vector>
using namespace std;

int x, y;
int num;
long long lines_total = 0;
long max_total = 0;
long min_total = 0;
vector<int> a = {};
int main() {
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  scanf("%d %d", &x, &y);
  for (int i = 0; i < x; i++) {
    int max_num = INT_MIN;
    int min_num = INT_MAX;
    for (int n = 0; n < y; n++) {
      scanf("%d", &num);
      lines_total += num;
      if (num > max_num)
        max_num = num;
      if (num < min_num)
        min_num = num;
    }
    max_total += max_num;
    min_total += min_num;
  }
  printf("%lld %ld %ld", lines_total, max_total, min_total);
  return 0;
}
