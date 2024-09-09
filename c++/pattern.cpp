//! All pattern question

#include <iostream>
using namespace std;
int Q1();
int Q2();
int Q3();
int Q4();
int main()
{
    // Q1();
    // Q2();
    // Q3();
    Q4();
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

//! printing  sequentical order of number in different rows
int Q2()
{
    int num1 = 1;
    int rows;
    cout << "Enter Rows" << endl;
    cin >> rows;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < rows; j++)
        {
            cout << num1;
            num1++;
        }
        cout << endl;
    }

    return 0;
}

/* printing
0
11
222
3333
44444
*/
int Q3()
{
    int rows;
    cout << "Enter the rows" << endl;
    cin >> rows;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cout << i;
        }
        cout << endl;
    }

    return 0;
}

//! floyd's triangle printing

int Q4()
{
    int rows;
    cout << "Enter Rows" << endl;
    cin >> rows;
    int num1 = 1;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cout << num1;
            num1++;
        }
        cout << endl;
    }

    return 0;
}