#include <iostream>
#include <algorithm>
#include <cmath>
#include "binarySearchTree.hpp"

using namespace std;

// Solution: https://www.youtube.com/watch?v=LU4fGD-fgJQ

class Solution
{
private:
    int findHeight(TreeNode *it)
    {
        if (it == nullptr)
            return -1;

        int l = findHeight(it->left);
        int r = findHeight(it->right);

        return max(l, r) + 1;
    }

public:
    bool isBalanced(TreeNode *root)
    {
        if (root == nullptr)
            return true;

        if (abs(findHeight(root->left) - findHeight(root->right)) > 1)
            return false;

        bool l = isBalanced(root->left);
        bool r = isBalanced(root->right);

        return l && r;
    }
};

int main()
{

    return 0;
}