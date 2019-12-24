#ifndef ORDERBOOK_H_
#define ORDERBOOK_H_

#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include "OrderUnit.hpp"

using namespace std;

class OrderBook
{
    public:
        priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison> buyBook;
        priority_queue<OrderUnit*, vector<OrderUnit*>, SellComparison> sellBook;
        unordered_map<double, OrderUnit*> buyPriceMap;
        unordered_map<double, OrderUnit*> sellPriceMap;

        void addToBook(int msgType, unsigned long int orderid, int side, unsigned long int quantity, double price)
        {
            Order* newOrder = new Order(msgType, orderid, side, quantity, price);

            // Buy Book.
            if(side == 0)
            {
                unordered_map<double, OrderUnit*>::iterator it = buyPriceMap.find(price);
                // No order unit.
                if(it == buyPriceMap.end())
                {
                    OrderUnit *ordUnit = new OrderUnit(price);
                    ordUnit->insertIntoChain(newOrder);
                    buyBook.push(ordUnit);
                    buyPriceMap.insert(pair<double, OrderUnit*>(price, ordUnit));
                }
                // Order unit exists, add to chain.
                else
                {
                    it->second->insertIntoChain(newOrder);
                }
                
            }
            // Sell Book.
            else if(side == 1)
            {
                unordered_map<double, OrderUnit*>::iterator it = sellPriceMap.find(price);
                // No order unit.
                if(it == sellPriceMap.end())
                {
                    OrderUnit *ordUnit = new OrderUnit(price);
                    ordUnit->insertIntoChain(newOrder);
                    sellBook.push(ordUnit);
                    sellPriceMap.insert(pair<double, OrderUnit*>(price, ordUnit));
                }
                // Order unit exists, add to chain.
                else
                {
                    it->second->insertIntoChain(newOrder);
                }
            }
        }

        void removeOrderUnit(int side, double price)
        {
            // Buy Book.
            if(side == 0)
            {
                unordered_map<double, OrderUnit*>::iterator it = buyPriceMap.find(price);
                if(it == buyPriceMap.end()) return;
                it->second->orderChain.deleteChain();
                buyPriceMap.erase(it);
            }
            // Sell Book.
            else if(side == 1)
            {

            }
        }

        void printBuyBook()
        {
            priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison> buyBookCopy = buyBook;
            cout << "====================" << endl;
            cout << "===== BUY BOOK =====" << endl;
            while (!buyBookCopy.empty()) 
            { 
                OrderUnit *p = buyBookCopy.top(); 
                buyBookCopy.pop();
                cout << "Price Level: " << p->getPrice() << endl;
                p->orderChain.printChain();
                cout << "---------------" << endl;
            }
            cout << "====================" << endl << endl;
        }

        void printSellBook()
        {
            priority_queue<OrderUnit*, vector<OrderUnit*>, SellComparison> sellBookCopy = sellBook;
            cout << "====================" << endl;
            cout << "===== SELL BOOK ====" << endl;
            while (!sellBookCopy.empty()) 
            { 
                OrderUnit *p = sellBookCopy.top(); 
                sellBookCopy.pop();
                cout << "Price Level: " << p->getPrice() << endl;
                p->orderChain.printChain();
                cout << "---------------" << endl;
            }
            cout << "====================" << endl << endl;
        }

        virtual ~OrderBook()
        {
            while (!buyBook.empty()) buyBook.pop();

            unordered_map<double, OrderUnit*>::iterator it;
            for(it = buyPriceMap.begin(); it != buyPriceMap.end(); it++) delete it->second;
            for(it = sellPriceMap.begin(); it != sellPriceMap.end(); it++) delete it->second;
        }
};

#endif