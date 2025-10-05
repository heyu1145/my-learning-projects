#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  cout << "Please Input An integer less than or Equal to 5 digits" << endl;
  double dou_a;
  cin >> dou_a;
  if (cin.fail()) {
    cout << "Please Input a integer!";
    return 1;
  }
  int a = (int)dou_a;
  if (a != dou_a) {
    cout << "Dont Input a Decimal!";
    return 1;
  }
  if (a < 0 or a > 99999) {
    cout << "The number is too small or too large!" << endl;
  string str_a = to_string(a);
  cout << "it has " << str_a.length() << " chars" << endl;
  vector<char> char_a;
  for (int i = 0;i < str_a.length();i++) {
    char_a.push_back(str_a.at(i));
    cout << "char " << i+1 << " : " << str_a.at(i) << endl;
  }
  reverse(char_a.begin(),char_a.end());
  cout << "number after reverse: ";
  for (char i : char_a) {
    cout << i;
  }
  cout << endl;
  return 0;
}
