#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int sum = nums[0], maxSum = sum;
        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i] + sum > nums[i])
            {
                sum = nums[i] + sum;
            }
            else
            {
                sum = nums[i];
            }

            if (maxSum < sum)
            {
                maxSum = sum;
            }
        }

        return maxSum;
    }
};

int main()
{
    Solution entity;

    vector<int> numbers = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

    cout << entity.maxSubArray(numbers) << endl;

    return 0;
}