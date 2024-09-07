#include <iostream>
#include <unistd.h>
using namespace std;

int age_verification();
int loops();
int main()
{
    // age_verification();
    loops();
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