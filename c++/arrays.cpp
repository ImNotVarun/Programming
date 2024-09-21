#include <iostream>
using namespace std;

int main()
{
    int marks[] = {23, 34, 54, 32, 12, 34};
    int total_marks = 0;
    for (int i = 0; i < sizeof(marks) / sizeof(marks[0]); i++)
    {
        total_marks += marks[i];
        cout << marks[i] << endl;
    }

    return 0;
}