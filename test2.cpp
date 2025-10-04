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
  double A = fmod(Input, 2.0);
  A = round(A * 1e10) / 1e10;
  if (A == 0){
    cout << "Even" << endl;
  }else if (A == 1){
    cout << "Odd" << endl;
  }else{
    cout << "Decimal,Remainder: " << A << endl;
  }
  cout << "The Number has ";
  if (Input > 0){
    double B = sqrt(Input);
    cout << "two roots: " << B << "and" << -B << endl;
  }else if (Input == 0){
    int B = 0;
    cout << "one root: " << B << endl;
  }else{
    cout << "no real root" << endl;
    double B = sqrt(-Input);
    cout << "Two of Imaginary roots: " << B << "i and " << -B << "i" << endl;
  }
  return 0;
}
