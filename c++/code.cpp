#include <iostream>
#include <unistd.h>
using namespace std;

int age_verification();
int loops();
int pattern();
int nth();
int fac();

int main()
{
    // age_verification();
    // loops();
    // pattern();
    // nth();
    fac();
    return 0;
}

int age_verification()
{
    int age;
    cout << "---------------Checking Are you 18+ or Not ----------------" << endl;
    sleep(1);
    cout << "---------------Checking you bank detail for the age verification---------------" << endl;
    sleep(1);
    cout << "---------------Please wait cheaking info---------------" << endl;
    sleep(1);
    cout << "---------------Check completed ---------------" << endl;
    sleep(1);
    cout << "---------------Enter you age ---------------" << endl;
    sleep(1);
    cin >> age;
    if (age < 18)
    {
        cout << "Your are not an adult to visit this adult website " << endl;
    }
    else
    {
        cout << "You have passed the test by cheating so you are not allowed to visit this adult website until your 18+" << endl;
    }
    return 0;
}

int loops()
{
    int n = 5;
    int count = 0;

    // for loops for printing 1 to 5 numbers
    for (int i = 0; i <= n; i++)
    {
        cout << "The Numbers are = " << i << endl;
    }

    // while loops for doing the same thing
    while (n >= count)
    {
        cout << count << endl;
        count++;
    }

    //? adding numbers from the nth position
    int num1;
    int sum = 0;
    cout << "ENter the number" << endl;
    cin >> num1;
    for (int i = 0; i <= num1; i++)
    {
        sum = i + sum;
    }
    cout << sum << endl;
    return 0;
}

//! printing pattern questions

int pattern()
{
    int row;
    int col;

    // printing only *
    cout << "Enter Rows" << endl;
    cin >> row;
    for (int i = 0; i < row; i++)
    {
        cout << "*";
    }

    // printing rows and coloums
    cout << "Enter Rows" << endl;
    cin >> row;
    cout << "Enter col" << endl;
    cin >> col;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}

//! sum of all number up to nth which is divisible by 3

int nth()
{
    int num;
    int sum = 0;
    cout << "Enter a number " << endl;
    cin >> num;
    for (int i = 1; i <= num; i++)
    {
        cout << i << endl;
        if (i % 3 == 0)
        {
            sum = sum + i;
        }
    }
    cout << sum << endl;

    return 0;
}

//! factorial of a Number only for small numbers
int fac()
{

    int num;
    int fac = 1;
    cout << "Enter a number " << endl;
    cin >> num;
    for (int i = 1; i <= num; i++)
    {
        fac = fac * i;
    }
    cout << fac << endl;

    return 0;
}