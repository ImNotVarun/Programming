#include <iostream>
using namespace std;
int minimum();
int sumofdigit();
int main()
{
    // minimum();
    sumofdigit();
    return 0;
}

int minimum()
{
    int num1, num2;
    cout << "Enter Number one" << endl;
    cin >> num1;
    cout << "Enter Number two" << endl;
    cin >> num2;
    if (num1 < num2)
    {
        cout << "This Number is the smallest " << num1 << endl;
    }
    else
    {
        cout << "This Number is the smallest " << num2 << endl;
    }
    return 0;
}

//! calculation sum of a digit

int sumofdigit()
{
    int num;
    cout << "Enter a Number" << endl;
    cin >> num;

    return 0;
}