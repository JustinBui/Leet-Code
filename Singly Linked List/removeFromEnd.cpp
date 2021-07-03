#include <iostream>
#include <vector>
#include "SLL.hpp"

using namespace std;

ListNode *removeNthFromEnd(ListNode *head, int n)
{
    ListNode *it = head, *target_node = head;
    int length = 0, target_index;

    // Count number of nodes
    while (it != nullptr)
    {
        length++;
        it = it->next;
    }

    target_index = length - n;

    // Traversing target_node pointer to the desired node to delete
    for (int i = 0; i < target_index; ++i)
    {
        target_node = target_node->next;
    }

    if (target_node == head)
    { // Special case: deleting head node
        head = head->next;
    }
    else
    {
        ListNode *pre_node = head;

        while (pre_node->next != target_node)
        {
            pre_node = pre_node->next;
        }
        pre_node->next = pre_node->next->next;
    }

    return head;
}

int main()
{
    IntLinkedList myList;
    vector<int> nums = {1, 2};

    for (int i = 0; i < nums.size(); ++i)
    {
        myList.addToEnd(nums[i]);
    }

    removeNthFromEnd(myList.getHead(), 1);
    myList.printAllElements();
    return 0;
}