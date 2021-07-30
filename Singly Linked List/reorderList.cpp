// Source: https://leetcode.com/problems/reorder-list/
// Solution: https://www.youtube.com/watch?v=S5bfdUTrKLM (Not like the code below)
// THIS IS MY OWN SOLUTION!!

#include <iostream>
#include <vector>
#include "SLL.hpp"
using namespace std;

class Solution
{
public:
    void reorderList(ListNode *head)
    {
        if (head->next != nullptr) // More than one head
        {
            ListNode *placeHolder = head;
            ListNode *tail = head;
            int loops = 0;

            while (placeHolder->next != nullptr)
            {
                // Traversing tail to last node
                while (tail->next != nullptr)
                    tail = tail->next;

                if (loops % 2 == 0)
                { // Makes sure this happens every 2 iterations
                    tail->next = placeHolder->next;
                    placeHolder->next = tail;

                    // Second to last serves as the next 'tail'
                    ListNode *secondToLast = tail->next;
                    while (secondToLast->next != tail)
                        secondToLast = secondToLast->next;
                    secondToLast->next = nullptr;
                }
                placeHolder = placeHolder->next;
                loops++;
            }
        }
    }
};

int main()
{
    Solution sol;
    IntLinkedList linked;

    vector<int> nums = {1, 2, 3, 4};
    for (vector<int>::iterator it = nums.begin(); it != nums.end(); ++it)
    {
        linked.addToEnd(*it);
    }

    cout << "Before: ";
    linked.printAllElements();

    sol.reorderList(linked.getHead());
    cout << "After: ";
    linked.printAllElements();

    return 0;
}