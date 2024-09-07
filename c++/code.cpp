#include <iostream>
#include <unistd.h>
using namespace std;

int main()
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