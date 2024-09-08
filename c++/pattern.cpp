//! All pattern question

#include <iostream>
using namespace std;
int Q1();
int main()
{
    Q1();
    return 0;
}

int Q1()
{
    int num;
    cout << "enter a number" << endl;
    cin >> num;
    for (int i = 0; i <= num; i++)
    {
        for (int j = 1; j <= num; j++)
        {
            cout << j << " ";
        }
        cout << endl;
    }

    return 0;
}