#include <iostream>
using namespace std;


int main() {
  int a = -2;
  int b = 8;
  int c = a*a+b;
  cout << c << endl;
  for (int i = c; i < b; i = i - a) {
    cout << i << ' ';
  }
  cout << "hello world from C++!" << endl;
  return 0;
}
