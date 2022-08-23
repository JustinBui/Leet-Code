#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

// https://leetcode.com/problems/3sum/
vector<vector<int>> threeSum(vector<int> &);

int main()
{
    vector<int> numbers = {-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4};
    vector<vector<int>> vectsOfVects = threeSum(numbers);

    for (int i = 0; i < vectsOfVects.size(); ++i)
    {
        cout << "[";
        for (int x = 0; x < vectsOfVects[i].size(); ++x)
        {
            cout << vectsOfVects[i][x] << " ";
        }
        cout << "]" << endl;
    }

    return 0;
}

vector<vector<int>> threeSum(vector<int> &nums)
{
    vector<vector<int>> result = {};
    sort(nums.begin(), nums.end());

    if (nums.size() >= 3)
    {
        for (int i = 0; i < nums.size() - 2; ++i)
        {

            if ((i == 0) || (i != 0 && nums[i - 1] != nums[i])) // Prevents duplicate i value
            {
                int left = i + 1;
                int right = nums.size() - 1;

                while (left < right)
                {

                    if (nums[left] + nums[right] + nums[i] == 0)
                    {
                        result.push_back({nums[left], nums[right], nums[i]});
                        left++;
                    }
                    else if (nums[left] + nums[right] + nums[i] > 0)
                        right--;

                    else if (nums[left] + nums[right] + nums[i] < 0)
                        left++;

                    // Prevents returning duplicate vectors
                    while (right != i && right != nums.size() - 1 && nums[right + 1] == nums[right])
                    {
                        right--;
                    }
                    while (left != nums.size() - 1 && left != i + 1 && nums[left - 1] == nums[left])
                    {
                        left++;
                    }
                }
            }
        }
    }

    return result;
}