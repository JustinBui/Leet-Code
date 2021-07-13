// https://leetcode.com/problems/merge-two-sorted-lists/

#include <iostream>
#include "SLL.hpp"

using namespace std;

ListNode *mergeTwoLists(ListNode *, ListNode *);

int main()
{
    IntLinkedList myList1;
    IntLinkedList myList2;

    return 0;
}

ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
{
    ListNode *it1 = l1;
    ListNode *it2 = l2;
    ListNode *start;

    if (it1 == nullptr)
        return it2;
    else if (it2 == nullptr)
        return it1;
    else
    { // FInding the starting value (head)
        if (it1->val <= it2->val)
        {
            start = it1;
            it1 = it1->next;
        }
        else
        {
            start = it2;
            it2 = it2->next;
        }
    }
    ListNode *nextSmallest = start; // This node will point to the next smallest node

    while (it1 != nullptr && it2 != nullptr)
    {
        if (it1->val < it2->val)
        {
            nextSmallest->next = it1;
            it1 = it1->next;
        }
        else
        {
            nextSmallest->next = it2;
            it2 = it2->next;
        }
        nextSmallest = nextSmallest->next;
    }

    if (it1 == nullptr)
        nextSmallest->next = it2;
    else
        nextSmallest->next = it1;

    return start;
}
