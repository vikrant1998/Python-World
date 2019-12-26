#include <iostream>
#include <stdio.h>

#include "Order.hpp"
#include "SamePriceOrderChain.hpp"

using namespace std;

void SamePriceTimeOrderChain::insertIntoChain(Order *o)
{
    // If the chain is empty.
    if(head == nullptr && tail == nullptr)
    {
        head = o;
        tail = o;
        head->setPrev(nullptr);
        head->setNext(nullptr);
    }
    else
    {
        Order* prevTail = tail;
        tail->setNext(o);
        tail = o;
        tail->setPrev(prevTail);
    }
}

void SamePriceTimeOrderChain::deleteFromChain(Order *o)
{
    if(o == nullptr || head == nullptr || tail == nullptr) return;
    
    // Only one element
    if(o == head && o == tail)
    {
        delete o;
        head = nullptr;
        tail = nullptr;
    }
    // Order @ head.
    else if(o == head)
    {
        head = o->getNext();
        head->setPrev(nullptr);
        o->setNext(nullptr);
        delete o;
    }
    // Order @ tail.
    else if(o == tail)
    {
        tail = o->getPrev();
        tail->setNext(nullptr);
        o->setPrev(nullptr);
        delete o;
    }
    // Order in the middle.
    else
    {
        Order* prevNode = o->getPrev();
        Order* nextNode = o->getNext();
        prevNode->setNext(nextNode);
        nextNode->setPrev(prevNode);
        delete o;
    }
}

void SamePriceTimeOrderChain::deleteChain()
{
    Order* nodePtr = head;
    while(nodePtr != nullptr)
    {
        Order* tempNode = nodePtr->next;
        if(tempNode != nullptr) tempNode->setPrev(nullptr);
        nodePtr->setNext(nullptr);
        delete nodePtr;
        nodePtr = tempNode;
    }
    head = nullptr;
    tail = nullptr;
}