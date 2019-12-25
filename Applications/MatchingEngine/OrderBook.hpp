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
        unordered_map<unsigned long int, Order*> idToOrderMap;

    public:

        void outputFillEvent(int side, Order *buyOrd, Order *sellOrd)
        {
            // Print fully fill event for aggressive orders.
            if(side == 0 && buyOrd->getQuantity() == 0) cout << "3," << buyOrd->getOrderid() << endl;
            else if(side == 1 && sellOrd->getQuantity() == 0) cout << "3," << sellOrd->getOrderid() << endl;

            // Print partially fill event for aggressive orders.
            if(side == 0 && buyOrd->getQuantity() != 0) cout << "4," << buyOrd->getOrderid() << "," << buyOrd->getQuantity() << endl;
            else if(side == 1 && sellOrd->getQuantity() != 0) cout << "4," << sellOrd->getOrderid() << "," << sellOrd->getQuantity() << endl;

            // Print fully fill event for resting orders.
            if(side == 1 && buyOrd->getQuantity() == 0) cout << "3," << buyOrd->getOrderid() << endl;
            else if(side == 0 && sellOrd->getQuantity() == 0) cout << "3," << sellOrd->getOrderid() << endl;

            // Print partially fill event for resting orders.
            if(side == 1 && buyOrd->getQuantity() != 0) cout << "4," << buyOrd->getOrderid() << "," << buyOrd->getQuantity() << endl;
            else if(side == 0 && sellOrd->getQuantity() != 0) cout << "4," << sellOrd->getOrderid() << "," << sellOrd->getQuantity() << endl;
        }

        void matchOrder(int side)
        {
            while(true)
            {
                // Both the books have to have data to match.
                if(buyBook.empty() || sellBook.empty()) return;
                OrderUnit *sellUnit = sellBook.top();
                OrderUnit *buyUnit  =  buyBook.top();

                // Check for price match.
                if(buyUnit == nullptr || sellUnit == nullptr) return;
                if(buyUnit->getPrice() < sellUnit->getPrice()) return;

                Order* buyOrd  = buyUnit->getHead();
                Order* sellOrd = sellUnit->getHead(); 
                while(buyOrd != nullptr && sellOrd != nullptr)
                {
                    unsigned long int buyQty  = buyOrd->getQuantity();
                    unsigned long int sellQty = sellOrd->getQuantity();
                    unsigned long int dispQty = 0;
                    
                    // Generate Trade Event.
                    if(side == 0) 
                    {
                        if(buyQty >= sellQty) dispQty = sellQty;
                        else dispQty = buyQty;
                        cout << "2," << dispQty << "," << sellOrd->getPrice() << endl;
                    }
                    else
                    {
                        if(sellQty >= buyQty) dispQty = buyQty;
                        else dispQty = sellQty;
                        cout << "2," << dispQty << "," << buyOrd->getPrice() << endl;
                    }
                    
                    buyOrd->setQuantity(buyQty - min(buyQty, sellQty));
                    sellOrd->setQuantity(sellQty - min(buyQty, sellQty));

                    outputFillEvent(side, buyOrd, sellOrd);

                    // Fully Fill.
                    if(buyOrd->getQuantity() == 0)
                    {
                        idToOrderMap.erase(buyOrd->getOrderid());
                        buyUnit->deleteFromChain(buyOrd);
                    }

                    // Fully Fill.
                    if(sellOrd->getQuantity() == 0)
                    {
                        idToOrderMap.erase(sellOrd->getOrderid());
                        sellUnit->deleteFromChain(sellOrd);
                    }

                    buyOrd  = buyUnit->getHead();
                    sellOrd = sellUnit->getHead(); 
                    if(buyOrd == nullptr)  deleteOrderUnit(0, buyUnit->getPrice());
                    if(sellOrd == nullptr) deleteOrderUnit(1, sellUnit->getPrice());
                }
            }
        }

        void addToBook(int msgType, unsigned long int orderid, int side, unsigned long int quantity, double price)
        {
            unordered_map<unsigned long int, Order*>::iterator it = idToOrderMap.find(orderid);
            if(it != idToOrderMap.end())
            {
                cout << "BAD MESSAGE" << endl;
                return;
            }
            Order* newOrder = new Order(msgType, orderid, side, quantity, price);

            // Buy Book.
            if(side == 0)
            {
                unordered_map<double, OrderUnit*>::iterator it = buyPriceMap.find(price);
                // No order unit.
                if(it == buyPriceMap.end())
                {
                    OrderUnit *ordUnit = new OrderUnit(price, side);
                    newOrder->setOrderUnitPtr(ordUnit);
                    ordUnit->insertIntoChain(newOrder);
                    buyBook.push(ordUnit);
                    buyPriceMap.insert(pair<double, OrderUnit*>(price, ordUnit));
                }
                // Order unit exists, add to chain.
                else
                {
                    newOrder->setOrderUnitPtr(it->second);
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
                    OrderUnit *ordUnit = new OrderUnit(price, side);
                    newOrder->setOrderUnitPtr(ordUnit);
                    ordUnit->insertIntoChain(newOrder);
                    sellBook.push(ordUnit);
                    sellPriceMap.insert(pair<double, OrderUnit*>(price, ordUnit));
                }
                // Order unit exists, add to chain.
                else
                {
                    newOrder->setOrderUnitPtr(it->second);
                    it->second->insertIntoChain(newOrder);
                }
            }

            unordered_map<unsigned long int, Order*>::iterator idIterator = idToOrderMap.find(orderid);
            if(idIterator == idToOrderMap.end()) idToOrderMap.insert(pair<unsigned long int, Order*>(orderid, newOrder));

            matchOrder(side);
        }

        void deleteOrderUnit(int side, double price)
        {
            // Buy Book.
            if(side == 0)
            {
                unordered_map<double, OrderUnit*>::iterator it = buyPriceMap.find(price);
                if(it == buyPriceMap.end()) return;
                it->second->orderChain.deleteChain();
                buyPriceMap.erase(it);
                priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison> buyBookCopy;
                while (!buyBook.empty()) 
                { 
                    OrderUnit *ordUnit = buyBook.top(); 
                    buyBook.pop();
                    // If price matches remove the order unit.
                    if(ordUnit->getPrice() != price) buyBookCopy.push(ordUnit);
                    else delete ordUnit;
                }
                buyBook = buyBookCopy;
            }
            // Sell Book.
            else if(side == 1)
            {
                unordered_map<double, OrderUnit*>::iterator it = sellPriceMap.find(price);
                if(it == sellPriceMap.end()) return;
                it->second->orderChain.deleteChain();
                sellPriceMap.erase(it);
                priority_queue<OrderUnit*, vector<OrderUnit*>, SellComparison> sellBookCopy;
                while (!sellBook.empty()) 
                { 
                    OrderUnit *ordUnit = sellBook.top(); 
                    sellBook.pop();
                    // If price matches remove the order unit.
                    if(ordUnit->getPrice() != price) sellBookCopy.push(ordUnit);
                    else delete ordUnit;
                }
                sellBook = sellBookCopy;
            }
        }

        void cancelOrder(int msgType, unsigned long int orderid)
        {
            unordered_map<unsigned long int, Order*>::iterator idIterator = idToOrderMap.find(orderid);
            if(idIterator == idToOrderMap.end()) return;
            OrderUnit *ordUnit = idIterator->second->getOrderUnitPtr();
            ordUnit->deleteFromChain(idIterator->second);
            idToOrderMap.erase(idIterator);
            if(ordUnit->getHead() == nullptr) deleteOrderUnit(ordUnit->getSide(), ordUnit->getPrice());
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