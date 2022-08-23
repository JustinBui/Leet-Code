#include<iostream>
#include "SLL.hpp"
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* newPtr = new ListNode(0);  
        ListNode* sumList = newPtr;     //This is what is being returned
        int first, second;
        bool carry = false;

        
        //Bringing each pointer to the end of the list
        while(l1 != nullptr || l2 != nullptr){
            if (l1 != nullptr) first = l1->val;
            else first = 0;
        
            if (l2 != nullptr) second = l2->val;
            else second = 0; 
            
            newPtr->val += first + second;
            if (newPtr->val >= 10){
                newPtr->val %= 10;
                carry = true;
            }

            //Onwards to the next nodes if possible
            if(l1 != nullptr) l1 = l1->next;
            if(l2 != nullptr) l2 = l2->next;
            
            //Shifting to the more significant digits node
            if (!carry && (l1 != nullptr || l2 != nullptr)){
                newPtr->next = new ListNode(0);
                newPtr = newPtr->next;
            }
            else if (carry){
                newPtr->next = new ListNode(1);
                newPtr = newPtr->next;
            }
                
            carry = false;      //Reset the carry to 0

        }
        return sumList;
    }
};

int main(){
    ListNode* printIterator;

    //9999999
    ListNode* l1 = new ListNode(9);
    printIterator = l1;
    
    for(int i = 0; i < 6; ++i){
        printIterator->next = new ListNode(9);
        printIterator = printIterator->next;
    }

    printIterator = l1;
    while (printIterator != nullptr){
        std::cout << printIterator->val;
        printIterator = printIterator->next;
    }
    std::cout << std::endl;

    //9999
    ListNode* l2 = new ListNode(9);
    printIterator = l2;

    for(int i = 0; i < 3; ++i){
        printIterator->next = new ListNode(9);
        printIterator = printIterator->next;
    }
    
    printIterator = l2;
    while (printIterator != nullptr){
        std::cout << printIterator->val;
        printIterator = printIterator->next;
    }
    std::cout << std::endl;

    /************************************SOLUTIONS**********************************************/
    Solution answerObj;
    ListNode* sum = answerObj.addTwoNumbers(l1, l2);

    while(sum != nullptr){
        std::cout << sum->val <<" ";
        sum = sum->next;
    }
    std::cout << std::endl; 

    return 0;
}