#include<iostream>
#include<vector>

#include "SLL.hpp"

 


class Solution {
public:
    bool isPalindrome(ListNode* head) {
        std::vector<int> numList;
        ListNode* iterator = head;

        //Copying contents of linked list into vector 
        while(iterator != nullptr) {     
            numList.push_back(iterator->val);
            iterator = iterator->next; 
        } 

        //Setting iterators on both ends of the vector
        int startIndex = 0, endIndex = numList.size() - 1;
        while(startIndex < endIndex){
            if(numList[startIndex] != numList[endIndex]){
                return false;
            }
            startIndex++;
            endIndex--;
        }
        
        return true;
        
    }
};


int main(){
    IntLinkedList myList;
    myList.addToEnd(1);
    myList.addToEnd(2);
    // myList.addToEnd(2);
    // myList.addToEnd(1);
    myList.printAllElements();

    Solution mySol;
    std::cout << mySol.isPalindrome(myList.getHead()) << std::endl;

    return 0;
}