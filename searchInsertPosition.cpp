// https://leetcode.com/problems/search-insert-position/

#include <iostream>
#include <vector>

using namespace std;

int searchInsert(vector<int> &, int);

int main()
{
    vector<int> numbers = {2, 3, 4, 10, 40};
    int target = 10;

    int result = searchInsert(numbers, target);
    cout << result << endl;

    return 0;
}

int searchInsert(vector<int> &nums, int target)
{
    int start = 0, end = nums.size() - 1, index;

    while (start != end)
    {
        index = (end + start) / 2;

        if (nums[index] == target)
            return index;

        else if (target > nums[index])
            start = index;

        else if (target < nums[index])
            end = index;
    }

    // If index was not found
    if (target > nums[index])
        index++;
    else
        index--;

    return index;
}