#include <iostream>
#include <unordered_map>
#include "SLL.hpp"

using namespace std;

ListNode *detectCycle(ListNode *);

int main()
{
    ListNode *firstNode(3, nullptr);
    ListNode *secondNode(3, nullptr);

    return 0;
}

ListNode *detectCycle(ListNode *head)
{
    ListNode *it = head;
    unordered_map<ListNode *, ListNode *> myMap;
    ListNode *result = nullptr;

    while (it != nullptr)
    {
        unordered_map<ListNode *, ListNode *>::const_iterator got = myMap.find(it->next);
        if (got == myMap.end() && it->next != head) // Not found
        {
            pair<ListNode *, ListNode *> item(it->next, it); // Key: Node being pointed
            myMap.insert(item);                              // Value: Node that points
        }
        else // Found
        {
            result = it->next;
            break;
        }
        it = it->next;
    }

    return result;
}