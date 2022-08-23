#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int leftPtr = 0,                  // Pointers further means more width to
            rightPtr = height.size() - 1, // maximize area potentially.
            maxArea = 0;

        while (leftPtr != rightPtr)
        {
            int w = rightPtr - leftPtr;
            int h = min(height[leftPtr], height[rightPtr]);

            int area = w * h;
            if (area > maxArea)
                maxArea = area;

            // Updating pointers going toward each other.
            if (height[leftPtr] < height[rightPtr])
                leftPtr++;
            else if (height[rightPtr] < height[leftPtr])
                rightPtr--;
            else if (height[leftPtr] == height[rightPtr])
                leftPtr++;
        }

        return maxArea;
    }
};

int main()
{
    Solution entity;

    vector<int> numbers = {1, 8, 6, 2, 5, 4, 8, 3, 7};

    cout << entity.maxArea(numbers) << endl;

    return 0;
}