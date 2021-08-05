#include <iostream>
#include <algorithm>
#include "binarySearchTree.hpp"
using namespace std;

class Solution
{
    int maxDepthHelper(TreeNode *it)
    {
        if (it == nullptr)
            return 0;

        int left = maxDepthHelper(it->left);
        int right = maxDepthHelper(it->right);

        return 1 + max(left, right);
    }

public:
    int maxDepth(TreeNode *root)
    {
        return maxDepthHelper(root);
    }
};

int main()
{
    BinarySearchTree oakTree;

    oakTree.insert(4);
    // oakTree.insert(1);
    // oakTree.insert(2);
    // oakTree.insert(6);
    //oakTree.insert(3);

    cout << "Preorder: ";
    oakTree.preorder();

    Solution entity;
    cout << entity.maxDepth(oakTree.getRoot()) << endl;

    return 0;
}
