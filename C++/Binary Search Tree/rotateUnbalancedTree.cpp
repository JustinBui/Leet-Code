// Solutions: https://www.youtube.com/watch?v=uFsLlmMz9Yg
// AVL Trees and Rotations: https://www.youtube.com/watch?v=-JbqJ9oqMXc

#include <iostream>
#include <cmath>
#include <vector>
#include "binarySearchTree.hpp"

using namespace std;

class Solution
{
private:
    vector<int> numbers;

    // --------------------- HELPER FUNCTIONS ---------------------

    // Making sorted array from our BST
    void inOrder(TreeNode *n)
    {
        if (n == nullptr)
            return;

        inOrder(n->left);
        numbers.push_back(n->val);
        inOrder(n->right);
    }

    // Using sorted array from inOrder() to build our own balanced
    // tree then returning it
    TreeNode *makeBalancedTree(vector<int> nums, int l, int r)
    {
        if (l > r)
            return nullptr;

        int mid = (l + r) / 2;

        TreeNode *newNode = new TreeNode(nums[mid]);

        newNode->left = makeBalancedTree(nums, l, mid - 1);
        newNode->right = makeBalancedTree(nums, mid + 1, r);

        return newNode;
    }

public:
    TreeNode *balanceBST(TreeNode *root)
    {
        inOrder(root);
        return makeBalancedTree(numbers, 0, numbers.size() - 1);
    }
};

int main()
{
    Solution mySol;

    return 0;
}