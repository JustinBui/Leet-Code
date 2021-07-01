#include<iostream>
#include<algorithm>
#include "SLL.hpp"

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* result = head;
        ListNode* end = head;       // Iterator makes its way toward middle.
        ListNode* endHelper;        // 'end' needs 'endHelper' to navigate to address
                                    // to node behind current node.

        while(end->next != nullptr){    // Traversing to the end of list
            end = end->next;            // of list
        }

        while (head != end && head->next != end) {
            std::swap(head->val, end->val);

            // Updating end
            endHelper = head;
            while (endHelper->next != end) {    // Traversing endHelper to node behind end
              endHelper = endHelper->next;   
            } 
            end = endHelper;

            // Updating head
            head = head->next;            
        }
        return result;
    }
};

int main(){
    IntLinkedList myList;
    for(int i = 0 ; i < 10; ++i){
        myList.addToEnd(i);
    }

    myList.addToEnd(23);


    myList.printAllElements();

    Solution mySolution;
    ListNode* myListReversed = mySolution.reverseList(myList.getHead());

    while (myListReversed != nullptr) {
        std::cout << myListReversed->val << " ";
        myListReversed = myListReversed->next;
    }
    std::cout << std::endl;

    return 0;
}