#include <iostream>
#include <vector>
#include "binarySearchTree.hpp"

using namespace std;

class Solution
{
public:
    TreeNode *sortedArrayToBST(vector<int> &nums)
    {
        // Finding the root
        int mid = (nums.size() - 1) / 2;
        TreeNode *root = new TreeNode(nums[mid]);

        TreeNode *curr = root;

        // Left side of tree
        for (int i = mid - 1; i > -1; --i)
        {
            TreeNode *newNode = new TreeNode(nums[i]);
            curr->left = newNode;
            curr = curr->left;
        }

        curr = root; // Resetting current pointer

        // Right side of tree
        for (int j = mid + 1; j < nums.size(); ++j)
        {
            TreeNode *newNode = new TreeNode(nums[j]);
            curr->right = newNode;
            curr = curr->right;
        }

        return root;
    }
};

int main()
{
    Solution mySol;

    vector<int> arr = {-10, -3, 0, 5, 9};
    mySol.sortedArrayToBST(arr);
    return 0;
}
