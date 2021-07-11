#include <iostream>
#include "SLL.hpp"

using namespace std;

bool hasCycle(ListNode *);

int main()
{
    ListNode *node1 = new ListNode(0, nullptr);
    ListNode *node2 = new ListNode(1, nullptr);
    ListNode *node3 = new ListNode(2, nullptr);
    ListNode *node4 = new ListNode(3, nullptr);
    ListNode *node5 = new ListNode(4, nullptr);

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = node3;

    ListNode *head = node1;

    cout << hasCycle(head) << endl;

    return 0;
}

bool hasCycle(ListNode *head)
{
    ListNode *slow = head, *fast = head;
    bool cycle = false;

    while (true)
    {
        if (slow != nullptr)
            slow = slow->next;
        else
            break;

        for (int i = 0; i < 2; ++i)
        {
            if (fast != nullptr)
                fast = fast->next;
        }
        if (fast == nullptr)
            break;

        if (slow == fast)
        {
            cycle = true;
            break;
        }
    }

    return cycle;
}