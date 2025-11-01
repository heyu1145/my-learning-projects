#include <iostream>
#include <string>
using namespace std;

string ford(int num1,char a,int num2) {
    switch(a) {
        case '+':
            return to_string(num1 + num2);
        case '-':
            return to_string(num1 - num2);
        case '*':
            return to_string(num1 * num2);
        case '/':
            if (num2 == 0) return "inf";
            return to_string(num1 / num2);
        default:
            return "unknown";
    }
}

int main() {
    int n1,n2;
    char b;
    cout << "请输入数字1: \n";
    cin >> n1;
    if (cin.fail()) {
        n1 = 1;
        cout << "输入失败! 默认输入1\n";
    }
    cout << "请输入符号: \n";
    cin >> b;
    if (cin.fail()) {
        b = '+';
        cout << "输入失败! 默认输入+\n";
    }
    cout << "请输入数字2: \n";
    cin >> n2;
    if (cin.fail()) {
        n2 = 1;
        cout << "输入失败! 默认输入1\n";
    }
    string result = ford(n1,b,n2);
    if (result == "unknown") {
        cout << "我不会, 长大后再学习" << endl;
        return 0;
    }
    cout << "结果为: " << result << endl;
    return 0;
}
