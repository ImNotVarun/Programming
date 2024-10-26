#include <iostream>
using namespace std;
void hello(int &a, int &b)
{
    cout << "Enter value for a " << endl;
    cin >> a;
    cout << "Enter value for b" << endl;
    cin >> b;
}

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
int reverce(int arr[], int size)
{
    int start = 0;
    int end = size - 1;
    while (start <= end)
    {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
    return 0;
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
    // int marks[] = {32, 23, 345, 45, 232, 12};
    // int size = sizeof(marks) / sizeof(marks[0]);
    // int target = 345;
    // int index = linear(marks, size, target);
    // if (index == -1)
    // {

    //     cout << "NO value found" << endl;
    // }
    // else
    // {
    //     cout << "Value Found on " << index;
    // }

    //! reverce of an array using pointer linear search

    // int arr[] = {1, 2, 3, 4, 5};
    // int size = sizeof(arr) / sizeof(arr[0]);
    // int string_reverce = reverce(arr, size);
    // for (int i = 0; i < size; i++)
    // {
    //     cout << arr[i] << " ";
    // }

    //! sum and product of an array
    // int arr[] = {1, 2, 3, 4, 5};
    // int sum = 0;
    // int pro = 1;
    // for (int i = 0; i < size; i++)
    // {
    //     sum = sum + i;
    //     pro = pro * arr[i];
    // }
    // cout << "Sum of the array is :" << sum << endl;
    // cout << "Product of the array is :" << pro << endl;

    //! swaping the maximum and minimum number from an array
    // int arr[] = {1, 2, 3, 4, 5};
    // int size = sizeof(arr) / sizeof(arr[0]);
    // int start = 0;
    // int end = size - 1;
    // int smallest = INT8_MAX;
    // int maximum = INT8_MIN;
    // // finding the maximum and minimum
    // for (int i = 0; i < size; i++)
    // {
    //     if (arr[i] > maximum)
    //     {
    //         maximum = arr[i];
    //     }
    //     if (arr[i] < smallest)
    //     {
    //         smallest = arr[i];
    //     }
    // }
    // for (int i = 0; i < size; i++)
    // {
    //     if (arr[i] == maximum)
    //     {
    //         arr[i] = smallest;
    //     }
    //     else if (arr[i] == smallest)
    //     {
    //         arr[i] = maximum;
    //     }
    // }
    // for (int i = 0; i < size; i++)
    // {
    //     cout << arr[i] << " ";
    // }
    // cout << "Maximum will be :" << maximum << endl;
    // cout << "Smallest will be :" << smallest << endl;

    //! printing a unique valur from the array
    // int arr[] = {1, 2, 3, 1, 2, 3, 4};
    // int size = sizeof(arr) / sizeof(arr[0]);
    // for (int i = 0; i < size; i++)
    // {
    //     int count = 0;
    //     for (int j = 0; j < size; j++)
    //     {
    //         if (arr[i] == arr[j])
    //         {
    //             count++;
    //         }
    //     }
    //     if (count == 1)
    //     {
    //         cout << "Unique Value is :" << arr[i] << endl;
    //     }
    // }

    //! print intersection of 2 arrays
    // int arr[] = {1, 2, 3, 4};
    // int arr2[] = {3, 4, 4, 5, 6};
    // int size = sizeof(arr) / sizeof(arr[0]);
    // int size2 = sizeof(arr2) / sizeof(arr2[0]);
    // for (int i = 0; i < size; i++)
    // {
    //     int count = 0;
    //     for (int j = 0; j < size2; j++)
    //     {
    //         if (arr[i] == arr2[j])
    //         {
    //             count++;
    //         }
    //     }
    //     if (count >= 1)
    //     {
    //         cout << arr[i] << endl;
    //     }
    // }



    return 0;
}
