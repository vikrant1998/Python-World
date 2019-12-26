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
    private:
        priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison> buyBook;
        priority_queue<OrderUnit*, vector<OrderUnit*>, SellComparison> sellBook;
        unordered_map<double, OrderUnit*> buyPriceMap;
        unordered_map<double, OrderUnit*> sellPriceMap;
        unordered_map<unsigned long int, Order*> idToOrderMap;

    public:
        void outputFillEvent(int side, Order *buyOrd, Order *sellOrd);
        void matchOrder(int side);
        void addToBook(int msgType, unsigned long int orderid, int side, unsigned long int quantity, double price);
        void deleteOrderUnit(int side, double price);
        void cancelOrder(int msgType, unsigned long int orderid);

        virtual ~OrderBook()
        {
            while (!buyBook.empty()) buyBook.pop();

            unordered_map<double, OrderUnit*>::iterator it;
            for(it = buyPriceMap.begin(); it != buyPriceMap.end(); it++) delete it->second;
            for(it = sellPriceMap.begin(); it != sellPriceMap.end(); it++) delete it->second;
        }
};

#endif