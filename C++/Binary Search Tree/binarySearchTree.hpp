#include <iostream>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class BinarySearchTree
{
private:
    TreeNode *root;

    // Helper functions
    void preorder_(TreeNode *);
    void inorder_(TreeNode *);
    void postorder_(TreeNode *);

public:
    BinarySearchTree() : root(nullptr){};

    // Modifiers
    void insert(int);
    // void remove();

    // Traversals
    void preorder();
    void inorder();
    void postorder();

    bool empty();
    TreeNode *getRoot();
};

bool BinarySearchTree::empty()
{
    if (root == nullptr)
        return true;
    else
        return false;
}

void BinarySearchTree::insert(int val)
{
    TreeNode *newNode = new TreeNode(val);
    if (empty())
        root = newNode;
    else
    {
        TreeNode *it = root; // Iterator
        TreeNode *upper;

        // Finding the spot for new node
        while (it != nullptr)
        {
            upper = it;
            if (newNode->val < it->val)
                it = it->left;
            else
                it = it->right;
        }

        if (upper->val > val)
            upper->left = newNode;
        else if (upper->val < val)
            upper->right = newNode;
    }
}

TreeNode *BinarySearchTree::getRoot()
{
    return root;
}

// ================================================== TRAVERSALS ==================================================

//   PREORDER
void BinarySearchTree::preorder()
{
    preorder_(root);
    cout << endl;
}

void BinarySearchTree::preorder_(TreeNode *curr) // VLR
{
    if (curr == nullptr)
        return;

    cout << curr->val << " ";
    preorder_(curr->left);
    preorder_(curr->right);
}

// INORDER

void BinarySearchTree::inorder()
{
    inorder_(root);
    cout << endl;
}

void BinarySearchTree::inorder_(TreeNode *curr) // VLR
{
    if (curr == nullptr)
        return;

    inorder_(curr->left);
    cout << curr->val << " ";
    inorder_(curr->right);
}

// POSTORDER

void BinarySearchTree::postorder()
{
    postorder_(root);
    cout << endl;
}

void BinarySearchTree::postorder_(TreeNode *curr) // VLR
{
    if (curr == nullptr)
        return;

    postorder_(curr->left);
    postorder_(curr->right);
    cout << curr->val << " ";
}