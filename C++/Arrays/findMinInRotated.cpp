// I THOUGHT OF THIS SOLUTION ON MY OWN
// Solution: https://www.youtube.com/watch?v=nIVW4P8b1VA

#include <iostream>
#include <vector>
#include <algorithms>

using namespace std;

int findMin(vector<int> &);

int main()
{
    vector<int> input = {11, 13, 15, 17};
    cout << findMin(input) << endl;

    return 0;
}

int findMin(vector<int> &nums)
{
    if (nums.size() == 1)
        return nums[0];
    else if (nums.size() == 2)
        return min(nums[0], nums[1]);
    else
    {
        int center = (nums.size() - 1) / 2;
        int cutoff = center;
        int lowest = nums[cutoff];

        // Cutoff value is less than both surrounding vals
        if (nums[cutoff] < nums[cutoff - 1] && nums[cutoff] < nums[cutoff + 1])
            lowest = nums[cutoff];
        else if (nums[center - 1] < nums[center + 1])
        { // Left cutoff
            while (nums[cutoff] <= lowest)
            {
                cutoff--;
                if (cutoff < 0)
                    cutoff = nums.size() - 1;

                if (nums[cutoff] < lowest)
                    lowest = nums[cutoff];
            }
        }
        else if (nums[center - 1] > nums[center + 1])
        { // Right cutoff
            while (nums[cutoff] <= lowest)
            {
                cutoff++;
                if (cutoff > nums.size() - 1)
                    cutoff = 0;

                if (nums[cutoff] < lowest)
                    lowest = nums[cutoff];
            }
        }
        return lowest;
    }
}