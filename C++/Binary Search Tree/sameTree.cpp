#include <iostream>
#include "binarySearchTree.hpp"
using namespace std;

class Solution
{
public:
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        if (p == nullptr)
        {
            if (q != nullptr)
                return false;
            else
                return true; // Both null
        }
        else if (p != nullptr)
        {
            if (q == nullptr)
                return false;
            else if (p->val != q->val)
                return false;
        }

        bool l = isSameTree(p->left, q->left);
        bool r = isSameTree(p->right, q->right);

        return l && r; // Comparing both right and left sides of node
    }
};

int main()
{
    // p tree
    BinarySearchTree p;
    p.insert(1);
    // p.insert(2);
    p.insert(3);

    cout << "p: ";
    p.preorder();

    // q tree
    BinarySearchTree q;
    q.insert(5);
    q.insert(2);
    q.insert(3);

    cout << "q: ";
    q.preorder();

    Solution mySol;

    cout << mySol.isSameTree(p.getRoot(), q.getRoot()) << endl;

    return 0;
}