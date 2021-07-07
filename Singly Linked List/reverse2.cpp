// https://leetcode.com/problems/reverse-linked-list-ii/

#include <iostream>
#include <vector>
#include "SLL.hpp"

using namespace std;

ListNode *reverseBetween(ListNode *head, int left, int right);

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5};
    IntLinkedList myList;

    for (int i = 0; i < nums.size(); ++i)
    {
        myList.addToEnd(nums[i]);
    }

    cout << "BEFORE: ";
    myList.printAllElements();

    ListNode *it = reverseBetween(myList.getHead(), 2, 4);

    cout << "AFTER: ";
    while (it != nullptr)
    {
        cout << it->val << " ";
        it = it->next;
    }
    cout << endl;

    return 0;
}

ListNode *reverseBetween(ListNode *head, int left, int right)
{
    ListNode *dummy = new ListNode(0, head); // Dummy node at front of list

    ListNode *pre = nullptr;
    ListNode *curr = dummy;
    ListNode *post = dummy;

    bool between = false;

    // Finding left and right nodes

    ListNode *leftPtr = dummy;
    for (int i = 0; leftPtr != nullptr && i < left; ++i)
        leftPtr = leftPtr->next;

    ListNode *rightPtr = dummy;
    for (int i = 0; rightPtr != nullptr && i < right; ++i)
        rightPtr = rightPtr->next;

    if (rightPtr == nullptr || leftPtr == nullptr)
        return head;

    if (head == leftPtr)
        head = rightPtr;

    // Modifying where the pointers point to reverse the list
    while (pre != rightPtr)
    {
        post = post->next;

        if (curr->next == leftPtr) // Special case to mod pointer
            curr->next = rightPtr;

        else if (curr == leftPtr) // Special case to mod pointer
        {
            curr->next = rightPtr->next;
            between = true;
        }
        else if (between)
            curr->next = pre;

        pre = curr;
        curr = post;
    }

    return head;
}