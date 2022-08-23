#include <iostream>

using namespace std;

class Node
{
public:
    int val;
    Node *prev;
    Node *next;
    Node *child;
};

class Solution
{
private:
    Node *flattenHelper(Node *head)
    {
        Node *curr = head;
        Node *tail; // Tail (Last Node) of current recursive iteration

        while (curr != nullptr)
        {
            if (curr->child != nullptr)
            {
                Node *tailReference = flattenHelper(curr->child); // Reference to 'tail' from iteration of lower level

                // Appending the lower level onto the DLL
                tailReference->next = curr->next;
                if (curr->next != nullptr)
                    curr->next->prev = tailReference;
                curr->next = child;
                child->prev = curr;
                curr->child = nullptr;
            }
            else
            {
                curr = curr->next;
                if (curr != nullptr)
                    tail = curr;
            }
        }

        return tail;
    }

public:
    Node *flatten(Node *head)
    {
        if (head == nullptr)
            flattenHelper(head);
        return head;
    }
};

int main()
{

    return 0;
}
