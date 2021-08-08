#include <iostream>
#include <algorithm>

#include "binarySearchTree.hpp"

using namespace std;

class Solution
{
private:
    void swapPointers(TreeNode *it)
    {
        if (it == nullptr)
            return;

        // Swapping where left and right point
        TreeNode *temp = it->left;
        it->left = it->right;
        it->right = temp;

        swapPointers(it->left);
        swapPointers(it->right);
    }

public:
    TreeNode *invertTree(TreeNode *root)
    {
        swapPointers(root);

        return root;
    }
};

int main()
{

    BinarySearchTree tree;

    tree.insert(4);
    tree.insert(2);
    tree.insert(7);
    // tree.insert(1);
    // tree.insert(6);

    cout << "Before: ";
    tree.inorder();

    Solution mySol;
    mySol.invertTree(tree.getRoot());

    cout << "After: ";
    tree.inorder();

    return 0;
}