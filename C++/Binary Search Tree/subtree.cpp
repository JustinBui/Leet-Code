#include <iostream>
#include "binarySearchTree.hpp"

using namespace std;

class Solution
{
private:
public:
    bool isSimilar(TreeNode *root, TreeNode *subRoot)
    {
        if (root == nullptr && subRoot == nullptr)
            return true;
        if (root == nullptr && subRoot != nullptr)
            return false;
        if (root != nullptr && subRoot == nullptr)
            return false;
        if (root->val != subRoot->val)
            return false;

        bool l = isSimilar(root->left, subRoot->left);
        bool r = isSimilar(root->right, subRoot->right);

        return l && r;
    }

    bool isSubtree(TreeNode *root, TreeNode *subRoot)
    {
        if (root == nullptr)
            return false;

        if (root->val == subRoot->val)
        {
            if (isSimilar(root, subRoot))
                return true;
        }

        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};

int main()
{
    BinarySearchTree first;
    first.insert(4);
    first.insert(2);
    first.insert(1);
    first.insert(3);
    first.insert(7);

    BinarySearchTree second;
    second.insert(2);
    second.insert(1);
    second.insert(3);

    Solution mySol;
    cout << mySol.isSubtree(first.getRoot(), second.getRoot()) << endl;

    return 0;
}