#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main() {
    cout << "Quadratic Equation Calculator" << endl;
    cout << "Please input an equation in format (ax^2+bx+c=0): " << endl;
    
    string GeneralEquation;
    getline(cin, GeneralEquation);
    
    if (GeneralEquation.empty()) {
        cout << "Please input an equation!" << endl;
        return 1;
    }
    
    size_t caret_pos = GeneralEquation.find("^");
    if (caret_pos == string::npos) {
        cout << "Invalid equation format! Missing '^'." << endl;
        return 1;
    }
    
    // Extract coefficient a
    string A_str;
    if (caret_pos >= 2) {
        A_str = GeneralEquation.substr(0, caret_pos - 2);
    } else {
        A_str = "1";
    }
    double a = stod(A_str);
    
    // Extract coefficient b
    size_t x_after_caret = GeneralEquation.find("x", caret_pos + 1);
    string B_str = "0";
    
    if (x_after_caret != string::npos) {
        size_t plus_pos = GeneralEquation.find("+", caret_pos + 2);
        size_t minus_pos = GeneralEquation.find("-", caret_pos + 2);
        size_t operator_pos = string::npos;
        
        if (plus_pos != string::npos && plus_pos < x_after_caret) {
            operator_pos = plus_pos;
        } else if (minus_pos != string::npos && minus_pos < x_after_caret) {
            operator_pos = minus_pos;
        }
        
        if (operator_pos != string::npos) {
            B_str = GeneralEquation.substr(operator_pos, x_after_caret - operator_pos);
        } else if (caret_pos + 2 < x_after_caret) {
            B_str = GeneralEquation.substr(caret_pos + 2, x_after_caret - caret_pos - 2);
        }
    }
    double b = stod(B_str);
    
    // Extract coefficient c
    size_t equals_pos = GeneralEquation.find("=");
    if (equals_pos == string::npos) {
        cout << "Invalid equation format! Missing '='." << endl;
        return 1;
    }
    
    string C_str = "0";
    if (x_after_caret != string::npos) {
        size_t start_pos = x_after_caret + 1;
        size_t plus_pos = GeneralEquation.find("+", x_after_caret);
        size_t minus_pos = GeneralEquation.find("-", x_after_caret);
        
        if (plus_pos != string::npos && plus_pos < equals_pos) {
            start_pos = plus_pos;
        } else if (minus_pos != string::npos && minus_pos < equals_pos) {
            start_pos = minus_pos;
        }
        
        if (start_pos < equals_pos) {
            C_str = GeneralEquation.substr(start_pos, equals_pos - start_pos);
        }
    }
    double c = stod(C_str);
    
    // Display coefficients
    cout << "\nEquation: " << GeneralEquation << endl;
    cout << "Coefficients: a = " << a << ", b = " << b << ", c = " << c << endl;
    
    // === YOUR CALCULATION PART ADDED HERE ===
    double D = b * b - 4 * a * c;
    cout << "Discriminant D = " << D << endl;
    
    if (D < 0) {
        cout << "Equation has no real roots" << endl;
        return 0;
    } else if (D == 0) {
        double x = -b / (2 * a);
        cout << "Equation has one real root: " << x << endl;
        return 0;
    } else {
        double d = sqrt(D);
        double x1 = (-b + d) / (2 * a);
        double x2 = (-b - d) / (2 * a);
        cout << "Equation has two real roots: " << endl;
        cout << "x1 = " << x1 << endl;
        cout << "x2 = " << x2 << endl;
        return 0;
    }
}
