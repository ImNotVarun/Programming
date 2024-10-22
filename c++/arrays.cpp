#include <iostream>
using namespace std;
// void hello(int &a, int &b);
// void hello(int &a, int &b)
// {
//     cout << "Enter value for a " << endl;
//     cin >> a;
//     cout << "Enter value for b" << endl;
//     cin >> b;
// }
int linear(int marks[], int size, int target)
{
    for (int i = 0; i < size; i++)
    {
        if (marks[i] == target)
        {
            return i;
        }
    }
    return -1;
}

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

    //! finding minimum value from the array
    // int marks[] = {23, 34, 45, 1, 67};
    // int smallest = INT8_MAX;
    // for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
    // {
    //     if (smallest < marks[i])
    //     {
    //         continue;
    //     }
    //     else
    //     {
    //         smallest = marks[i];
    //     }
    // }
    // cout << smallest << endl;

    //! finding maximum value from array
    // int marks[] = {23, 34, 45, 1, 67};
    // int maximum = INT8_MIN;
    // for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
    // {
    //     if (maximum > marks[i])
    //     {
    //         continue;
    //     }
    //     else
    //     {
    //         maximum = marks[i];
    //     }
    // }
    // cout << maximum << endl;

    //! finding tha smallest and largestt
    // int marks[] = {23, 345, 45, 555, -2};
    // int smallest = INT8_MAX;
    // int maximum = INT8_MIN;

    // for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
    // {
    //     if (marks[i] > maximum)
    //     {
    //         maximum = marks[i];
    //     }
    //     if (marks[i] < smallest)
    //     {
    //         smallest = marks[i];
    //     }
    // }
    // cout << smallest << endl;
    // cout << maximum << endl;

    //! pass by reference example

    // int a = 23;
    // int b = 45;

    // hello(a, b);
    // int sum = a + b;
    // cout << sum << endl;

    //! linear search example
    int marks[] = {32, 23, 345, 45, 232, 12};
    int size = sizeof(marks) / sizeof(marks[0]);
    int target = 345;
    int index = linear(marks, size, target);
    if (index == -1)
    {

        cout << "NO value found" << endl;
    }
    else
    {
        cout << "Value Found on " << index;
    }

    return 0;
}
