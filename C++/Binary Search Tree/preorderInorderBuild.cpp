// Solution: https://www.youtube.com/watch?v=ihj4IQGZ2zc

#include <iostream>
#include <vector>
#include <algorithm>

#include "binarySearchTree.hpp"

using namespace std;

class Solution
{
private:
    TreeNode *helper(int preorder_begin, int preorder_end, int inorder_begin, int inorder_end, vector<int> &preorder, vector<int> &inorder)
    {
        if (preorder_begin >= preorder_end || inorder_begin >= inorder_end)
            return nullptr;

        TreeNode *root = new TreeNode(preorder[preorder_begin]); // it is ALWAYS guaranteed that the 1st element of preorder is 1st node
        int mid = 0;

        for (int i = inorder_begin; i < inorder_end; ++i) // Finding index of first node in inorder (Used to build left right subtrees)
        {
            if (preorder[preorder_begin] == inorder[i])
            {
                mid = i - inorder_begin;
                break;
            }
        }

        // Everything on the left of mid - left subtree
        root->left = helper(preorder_begin + 1, preorder_begin + mid + 1, inorder_begin, inorder_begin + mid + 1, preorder, inorder);

        // Everything on the left of mid - left subtree
        root->right = helper(preorder_begin + mid + 1, preorder_end, inorder_begin + mid + 1, inorder_end, preorder, inorder);

        return root;
    }

public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        return helper(0, preorder.size(), 0, inorder.size(), preorder, inorder);
    }
};

void inorder(TreeNode *root)
{
    if (root == nullptr)
        return;

    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

void preorder(TreeNode *root)
{
    if (root == nullptr)
        return;

    cout << root->val << " ";
    inorder(root->left);
    inorder(root->right);
}

int main()
{
    vector<int> pre = {3, 9, 20, 15, 7};
    vector<int> in = {9, 3, 15, 20, 7};

    Solution mySol;
    TreeNode *root = mySol.buildTree(pre, in);

    preorder(root);
    cout << endl;

    inorder(root);
    cout << endl;

    return 0;
}
