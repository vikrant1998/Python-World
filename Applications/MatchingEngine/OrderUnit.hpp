#ifndef ORDERUNIT_H_
#define ORDERUNIT_H_

#include <iostream>
#include "SamePriceOrderChain.hpp"
#include "Order.hpp"

using namespace std;

class OrderUnit
{
	public:
		double price;
		int side;
		SamePriceTimeOrderChain orderChain;
	public:
		OrderUnit(int price, int side) 
		{ 
			this->price = price; 
			this->side = side;
		}
		double getPrice() { return price; }
		double getSide()  { return side; }
		void insertIntoChain(Order *o) { orderChain.insertIntoChain(o); }
		void deleteFromChain(Order *o) { orderChain.deleteFromChain(o); }
		void deleteChain() { orderChain.deleteChain(); }
		Order* getHead() { orderChain.getHead(); }
};

struct BuyComparison 
{ 
    bool operator()(OrderUnit *o1, OrderUnit *o2) 
    { 
        return o1->getPrice() < o2->getPrice(); 
    } 
};

struct SellComparison 
{ 
    bool operator()(OrderUnit *o1, OrderUnit *o2) 
    { 
        return o1->getPrice() > o2->getPrice(); 
    } 
};

#endif