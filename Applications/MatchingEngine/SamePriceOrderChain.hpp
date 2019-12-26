#ifndef ORDERCHAIN_H_
#define ORDERCHAIN_H_

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
		Order* getHead() { return head; }
		void insertIntoChain(Order *o);
		void deleteFromChain(Order *o);
		void deleteChain();
		virtual ~SamePriceTimeOrderChain() { deleteChain(); }
};

#endif