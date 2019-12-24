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
        vector<OrderUnit*> buyBookVector;

        priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison> buyBook;
        priority_queue<OrderUnit*, vector<OrderUnit*>, SellComparison> sellBook;
        unordered_map<double, OrderUnit*> buyPriceMap;
        unordered_map<double, OrderUnit*> sellPriceMap;

        void swap(int *a, int *b)
        {
            int temp = *b;
            *b = *a;
            *a = temp;
        }
        void heapify(vector<int> &hT, int i)
        {
            int size = hT.size();
            int largest = i;
            int l = 2 * i + 1;
            int r = 2 * i + 2;
            if (l < size && hT[l] > hT[largest])
                largest = l;
            if (r < size && hT[r] > hT[largest])
                largest = r;

            if (largest != i)
            {
                swap(&hT[i], &hT[largest]);
                heapify(hT, largest);
            }
        }
        void insert(int msgType, unsigned long int orderid, int side, unsigned long int quantity, double price)
        {
            int size = hT.size();
            if (size == 0)
            {
                hT.push_back(newNum);
            }
            else
            {
                hT.push_back(newNum);
                for (int i = size / 2 - 1; i >= 0; i--)
                {
                    heapify(hT, i);
                }
            }
        }
        void deleteNode(vector<int> &hT, int num)
        {
            int size = hT.size();
            int i;
            for (i = 0; i < size; i++)
            {
                if (num == hT[i])
                    break;
            }
            swap(&hT[i], &hT[size - 1]);

            hT.pop_back();
            for (int i = size / 2 - 1; i >= 0; i--)
            {
                heapify(hT, i);
            }
        }
        void printArray(vector<int> &hT)
        {
            for (int i = 0; i < hT.size(); ++i)
                cout << hT[i] << " ";
            cout << "\n";
        }

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