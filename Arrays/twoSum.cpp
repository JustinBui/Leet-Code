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

        return result;
    }
};

int main()
{
    vector<int> numbers = {-3, 4, 3, 90};
    int target = 0;

    Solution mySol;

    vector<int> newArr = mySol.twoSum(numbers, target);
    for (int i = 0; i < newArr.size(); ++i)
    {
        cout << newArr[i] << ", ";
    }
    cout << endl;

    return 0;
}