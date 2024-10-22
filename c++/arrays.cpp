#include <iostream>
using namespace std;

int main()
{
    // int marks[] = {};
    // int total_marks = 0;
    // for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
    // {
    //     total_marks += marks[i];
    //     cout << marks[i] << endl;
    // }

    // int size = 5;
    // int marks[size];
    // for (int i = 0; i < size; i++)
    // {
    //     cin >> marks[i];
    // }
    // for (int i = 0; i < size; i++)
    // {
    //     cout << marks[i] << endl;
    // }

    int marks[] = {23, 34, 45, 1, 67};
    int smallest = INT8_MAX;
    for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
    {
        if (smallest < marks[i])
        {
            continue;
        }
        else
        {
            smallest = marks[i];
        }
    }
    cout << smallest << endl;
    return 0;
}