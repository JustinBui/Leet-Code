#include <iostream>
#include <vector>
#include "binarySearchTree.hpp"

using namespace std;

// Solution: https://www.youtube.com/watch?v=0K0uCMYq5ng
class Solution
{
public:
    TreeNode *helper(vector<int> &nums, int l, int r)
    {
        if (l > r)
            return nullptr;

        int m = (l + r) / 2;
        TreeNode *newNode = new TreeNode(nums[m]);
        newNode->left = helper(nums, l, m - 1);
        newNode->right = helper(nums, m + 1, r);

        return newNode;
    }

    TreeNode *sortedArrayToBST(vector<int> &nums)
    {
        return helper(nums, 0, nums.size() - 1);
    }
};

int main()
{
    Solution mySol;

    vector<int> arr = {-10, -3, 0, 5, 9};
    TreeNode *res = mySol.sortedArrayToBST(arr);

    return 0;
}
