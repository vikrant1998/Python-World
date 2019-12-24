#ifndef ORDER_H_
#define ORDER_H_

#include <iostream>

using namespace std;

class Order
{
	private:
		int msgType = 0;
		unsigned long int orderid = 0;
		int side = 0;
		unsigned long int quantity = 0;
		double price = 0;

	public:
		Order* next = nullptr;
		Order* prev = nullptr;
		Order(int msgType, unsigned long int orderid, int side, unsigned long int quantity, double price)
		{
			this->msgType  = msgType;
			this->orderid  = orderid;
			this->side 	   = side;
			this->quantity = quantity;
			this->price    = price; 
		}
		Order* getNext() { return next; }
		Order* getPrev() { return prev; }
		void   setNext(Order *next) { this->next = next; }
		void   setPrev(Order *prev) { this->prev = prev; }

		double getPrice() { return price; }
};

#endif