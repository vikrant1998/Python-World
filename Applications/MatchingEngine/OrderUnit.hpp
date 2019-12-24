#ifndef ORDERUNIT_H_
#define ORDERUNIT_H_

#include <iostream>
#include "SamePriceOrderChain.hpp"

using namespace std;

class OrderUnit
{
	public:
		double price;
		SamePriceTimeOrderChain orderChain;
	public:
		OrderUnit(int price) { this->price = price; }
		double getPrice() { return price; }
		void insertIntoChain(Order *o) { orderChain.insertIntoChain(o); }
		void deleteFromChain(Order *o) { orderChain.deleteFromChain(o); }
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