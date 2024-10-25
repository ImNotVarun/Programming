#include <iostream>
#include <vector>
using namespace std;

int main()
{

    // vector<int> vec = {1, 2, 3, 4, 5}; //* vector delcleration
    // vec.push_back(3);                  //! adding a value to the vector
    // cout << "Vector values after push back" << endl;
    // for (int i : vec) //? for each loop
    // {
    //     cout << i << endl;
    // }
    // cout << "size after pust back :" << vec.size() << endl;
    // vec.pop_back(); //! removing value from vector
    // cout << "Vector values after pop back" << endl;
    // for (int i : vec) //? for each loop
    // {
    //     cout << i << endl;
    // }
    // cout << "size after pop back :" << vec.size() << endl;
    // cout << "acessing value on a particular index :" << vec.at(3) << endl;

    // vector<int> prices = {7, 1, 5, 3, 6, 4};
    // int smallest = INT8_MAX;
    // int largest = INT8_MIN;
    // for (int i : prices)
    // {
    //     if (i < smallest)
    //     {
    //         smallest = i;
    //     }
    // }
    // bool foundsmall=false;
    // for (int j :prices)
    // {
    //     if (foundsmall || j == smallest) {
    //         foundsmall = true;
    //     }
    //     if (j > largest)
    //     {
    //         largest = j;
    //     }
    // }
    // int ans = largest - smallest;
    // return ans;

    //! subarrays
    int arr[5] = {1, 2, 3, 4, 5};
    int size = 5;
    for (int i = 0; i < size; i++)
    {
        for (int j = i; j < size; j++)
        {
            for (int k = i; k <= j; k++)
            {
                cout << arr[i];
            }
            cout << " ";
        }
        cout << endl;
    }
}