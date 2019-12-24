#include <iostream>
#include <vector>
#include <sstream>
#include <stdexcept>
#include <queue>

#include "SamePriceOrderChain.hpp"
#include "OrderUnit.hpp"
#include "Order.hpp"
#include "OrderBook.hpp"

using namespace std;

void ParseInput();

void ParseInput()
{
	string str;
	while(getline(cin, str))
	{
		vector<string> result;
		stringstream s_stream(str);
		while(s_stream.good()) 
		{
			string substr;
			getline(s_stream, substr, ',');
			result.push_back(substr);
		}

		// Input is valid only if there are 2 or 5 elements.
		if(result.size() != 2 && result.size() != 5)
		{
			// Handle error case.
			continue;
		}

		int msgType = 0;
		unsigned long int orderid = 0;
		int side = 0;
		unsigned long int quantity = 0;
		double price = 0;
		// Check for erroneous input.
		try
		{
			msgType = std::stoi(result.at(0));
			orderid = std::stol(result.at(1));
			if(result.size() == 5)
			{
				side = std::stoi(result.at(2));
				quantity = std::stol(result.at(3));
				price = std::stod(result.at(4));
			}
		}
		catch(...)
		{
			// Handle error case.
			continue;
		}

		cout << "VIK: " << msgType << "," << orderid << "," << side << "," << quantity << "," << price << endl;
	}
} 

void printPriorityQueue(priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison>& Q)
{
	while (!Q.empty()) 
	{ 
		OrderUnit *p = Q.top(); 
		Q.pop();
		cout << "Price Level: " << p->getPrice() << endl;
		p->orderChain.printChain();
		cout << "---------------" << endl;
	}
}

int main()
{
	//ParseInput();
	// OrderBook orderBook;
	// orderBook.addToBook(0, 1, 0, 10, 10.0);
	// orderBook.addToBook(0, 1, 0, 10, 12.0);
	// orderBook.addToBook(0, 1, 0, 10, 12.0);
	// orderBook.addToBook(0, 1, 0, 10, 9.0);

	// orderBook.addToBook(0, 1, 1, 10, 10.0);
	// orderBook.addToBook(0, 1, 1, 10, 12.0);
	// orderBook.addToBook(0, 1, 1, 10, 12.0);
	// orderBook.addToBook(0, 1, 1, 10, 9.0);

	// orderBook.printBuyBook();
	// orderBook.deleteOrderUnit(0, 10.0);
	// orderBook.printBuyBook();

	vector<int> heapTree;

	insert(heapTree, 3);
	insert(heapTree, 4);
	insert(heapTree, 9);
	insert(heapTree, 5);
	insert(heapTree, 2);

	cout << "Max-Heap array: ";
	printArray(heapTree);

	deleteNode(heapTree, 4);

	cout << "After deleting an element: ";

	printArray(heapTree);

	return 0;
}
