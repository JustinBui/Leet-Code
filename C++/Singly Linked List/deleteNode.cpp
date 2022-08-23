#include "SLL.hpp"
#include <iostream>

void deleteNode(ListNode*);

int main() {
    IntLinkedList myList;

    myList.addToEnd(1);
    myList.addToEnd(2);
    myList.addToEnd(3);
    myList.addToEnd(4);
    myList.addToEnd(5);
    myList.addToEnd(6);


    myList.printAllElements();

    deleteNode(myList.getHead());

    myList.printAllElements();


    return 0;
}

void deleteNode(ListNode* node) {
    // Referece to the next node to assign it's value 
    // to the current node
    ListNode* after = node->next;

    while (after->next != nullptr) {
        node->val = after->val;

        // Traversing both pointers forward
        node = node->next;
        after = after->next;
    }
    node->val = after->val; // Update node before the very last node
    
    delete node->next;  // Deleting the very last node

    // To prevent dangling pointers
    node->next = nullptr;
    after = nullptr;
}