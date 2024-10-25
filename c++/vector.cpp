#include <iostream>
#include <vector>
using namespace std;

int main()
{

    vector<int> vec = {1, 2, 3, 4, 5}; //* vector delcleration
    vec.push_back(3);                  //! adding a value to the vector
    cout << "Vector values after push back" << endl;
    for (int i : vec) //? for each loop
    {
        cout << i << endl;
    }
    cout << "size after pust back :" << vec.size() << endl;
    vec.pop_back(); //! removing value from vector
    cout << "Vector values after pop back" << endl;
    for (int i : vec) //? for each loop
    {
        cout << i << endl;
    }
    cout << "size after pop back :" << vec.size() << endl;
    cout << "acessing value on a particular index :" << vec.at(3) << endl;
    return 0;
}