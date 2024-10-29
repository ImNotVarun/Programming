#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> nums = {2, 1, 0, 0, 1, 2};
    int mid = 1, st = 0, n = nums.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (nums[i] >nums[j])
            {
                swap(nums[i], nums[j]);
            }
        }
    }
    for (int j = 0; j < nums.size(); j++)
    {
        cout << nums[j] << endl;
    }

    //! got it wrong
    // for(int i=0;i<size;){
    //     if(nums[i]>mid){
    //         nums.push_back(nums[i]);
    //         i++;
    //     }
    //     else if(nums[i]<mid){
    //         nums.insert(nums.begin()+st,nums[i]);
    //         i++;
    //     }
    //     else{
    //         i++;
    //     }
    // }
    // for (int j = 0; j < nums.size(); j++) {
    //     cout << nums[j] << endl;
    // }

    return 0;
}