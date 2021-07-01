#include<iostream>
#include "SLL.hpp"


ListNode* oddEvenList(ListNode*);

int main() {
    IntLinkedList myList;

    myList.addToEnd(1);
    myList.addToEnd(2);
    myList.addToEnd(3);
    myList.addToEnd(4);
    myList.addToEnd(5);
    myList.addToEnd(6);


    myList.printAllElements();

    oddEvenList(myList.getHead());

    myList.printAllElements();


    return 0;
}

ListNode* oddEvenList(ListNode* head) {
    // If there are no nodes
    if (head == nullptr) {
        return nullptr;
    }
    // If there are 1 or 2 nodes, then it is good 
    else if (head->next == nullptr || head->next->next == nullptr) {
        return head;
    }

    else {
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenOrigin = even;

            while(even != nullptr && even->next != nullptr && odd->next != nullptr) {
            odd->next = even->next;
            odd = even->next;

            even->next = odd->next;
            even = odd->next;
        }
        
        odd->next = evenOrigin;

        return head;
    }
    
}
