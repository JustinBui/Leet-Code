// https://leetcode.com/problems/search-insert-position/

#include <iostream>
#include <vector>

using namespace std;

int searchInsert(vector<int> &, int);

int main()
{
    vector<int> numbers = {1, 3};
    int target = 2;

    int result = searchInsert(numbers, target);
    cout << result << endl;

    return 0;
}

int searchInsert(vector<int> &nums, int target)
{
    int start = 0, end = nums.size() - 1, index;

    while (start <= end)
    {
        index = start + (end - start) / 2;

        if (nums[index] == target)
            return index;

        else if (target > nums[index])
            start = index + 1;

        else if (target < nums[index])
            end = index - 1;
    }

    if (target > nums[index])
        index++;

    return index;
}