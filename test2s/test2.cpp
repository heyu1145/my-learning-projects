#include <iostream>
#include <cmath>
using namespace std;

int main(){
  cout << "hello!" << endl;
  cout << "Please input a number: ";
  double Input;
  cin >> Input;
  if (cin.fail()){
  cout << "Please dont insert a string!" << endl;
  cin.clear();
  cin.ignore(10000, '\n');
  return 1;
  }
  cout << "The number is ";
  bool isOdd = false;
  double A = fmod(Input, 2.0);
  A = round(A * 1e10) / 1e10;
  if (A == 0){
    cout << "Even" << endl;
  }else if (A == 1){
    cout << "Odd" << endl;
    isOdd = true;
  }else{
    cout << "Decimal,Remainder: " << A << endl;
  }
  cout << "The Number has ";
  bool isPositive = false;
  if (Input > 0){
    double B = sqrt(Input);
    isPositive = true;
    cout << "two roots: " << B << "and" << -B << endl;
  }else if (Input == 0){
    int B = 0;
    cout << "one root: " << B << endl;
  }else{
    cout << "no real root" << endl;
    double B = sqrt(-Input);
    cout << "Two of Imaginary roots: " << B << "i and " << -B << "i" << endl;
  }
  int int_Input = (int)Input;
  cout << "The number is ";
  if (round(Input * 1e10) / 1e10 == 2) {
    cout << "a prime" << endl;
  } else if (int_Input == 1) {
    cout << "NOT a prime" << endl;
  } else if (isOdd and isPositive){
    double B = (int)sqrt(int_Input);
    int match = -1;
    for (int i = 3;i < B+1;i = i + 2) {
      if (int_Input%i == 0) {
        cout << "NOT a prime" << endl;
        match = i;
        break;
      }
    }
    if (match == -1) {
      cout << "a prime" << endl;
    }
  } else {
    cout << "NOT a prime" << endl;
  }
  return 0;
}
