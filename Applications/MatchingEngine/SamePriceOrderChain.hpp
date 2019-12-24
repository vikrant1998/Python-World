#include <iostream>
#include <stdio.h>
#include "Order.hpp"

using namespace std;

class SamePriceTimeOrderChain
{
	private:
		Order* head = nullptr;
		Order* tail = nullptr;

	public:
		void InsertIntoChain(Order *o)
		{
			// If the chain is empty.
			if(head == nullptr && tail == nullptr)
			{
				head = o;
				tail = o;
			}
			else
			{
				Order* prevTail = tail;
				tail->setNext(o);
				tail = o;
				tail->setPrev(prevTail);
			}
		}

		void PrintChain()
		{
			Order* nodePtr = head;
			while(nodePtr != nullptr)
			{
				cout << nodePtr->getPrice() << endl;
				nodePtr = nodePtr->next;
			}
		}

		void PrintChainRev()
		{
			Order* nodePtr = tail;
			while(nodePtr != nullptr)
			{
				cout << nodePtr->getPrice() << endl;
				nodePtr = nodePtr->prev;
			}
		}

		~SamePriceTimeOrderChain()
		{
			Order* nodePtr = head;
			while(nodePtr != nullptr)
			{
				Order* tempNode = nodePtr->next;
				delete nodePtr;
				nodePtr = tempNode;
			}
		}
};