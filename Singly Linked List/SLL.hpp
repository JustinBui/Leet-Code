#pragma once
#include<iostream>

//Definition for singly-linked list.
 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class IntLinkedList{
private:    
    ListNode* head;
    ListNode* tail;
    
public:
    IntLinkedList(): head(nullptr), tail(nullptr) {}
    bool empty();
    void addToEnd(int);
    void printAllElements();
    ListNode* getHead() { return head; }        //Pause...
};

bool IntLinkedList::empty(){
    if(head == nullptr && tail == nullptr) return true;
    else return false;
}

void IntLinkedList::addToEnd(int v){
    if(empty()){
        head = new ListNode(v);
        tail = head;
    } 
    else{
        tail->next = new ListNode(v);
        tail = tail->next;
    }
}

void IntLinkedList::printAllElements() {
    ListNode* iterator = head;
    while(iterator != nullptr) {
        std::cout << iterator->val << " ";
        iterator = iterator->next;
    }
    std::cout << std::endl; 
}
