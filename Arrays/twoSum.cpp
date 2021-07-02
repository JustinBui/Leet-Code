#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> myMap;
        int complement;
        vector<int> result;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] <= target)
            {
                complement = target - nums[i]; // Complement of nums[i]
                map<int, int>::iterator it = myMap.find(nums[i]);
                if (it != myMap.end()) // Key (As complement of nums[i]) is found
                {
                    result.push_back(i);
                    result.push_back(it->second);
                    break;
                }
                else
                {
                    myMap.insert(pair<int, int>(complement, i)); // <Complement of index, index>
                }
            }
        }

        for (auto it = result.begin(); it != result.end(); ++it)
            cout << *it << ", ";
        cout << endl;

        return result;
    }
};

int main()
{
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;

    Solution mySol;

    vector<int> newArr = mySol.twoSum(numbers, target);
    for (int i = 0; i < newArr.size(); ++i)
    {
        cout << newArr[i] << ", ";
    }
    cout << endl;

    return 0;
}