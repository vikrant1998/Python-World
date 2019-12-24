#include <iostream>
#include <vector>
#include <sstream>
#include <stdexcept>
#include <queue>

#include "SamePriceOrderChain.hpp"
#include "OrderUnit.hpp"
#include "Order.hpp"

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

int main()
{
	//ParseInput();
	OrderUnit *o1 = new OrderUnit(100);
	Order *ord1 = new Order(1,1,1,1,100);
	Order *ord2 = new Order(2,1,1,1,100);
	Order *ord3 = new Order(3,1,1,1,100);
	o1->insertIntoChain(ord1);
	o1->insertIntoChain(ord2);
	o1->insertIntoChain(ord3);
	o1->deleteFromChain(ord3);
	o1->orderChain.printChain();
	OrderUnit *o2 = new OrderUnit(999);
	OrderUnit *o3 = new OrderUnit(32);
	OrderUnit *o4 = new OrderUnit(1002);

	priority_queue<OrderUnit*, vector<OrderUnit*>, BuyComparison> Q; 
	Q.push(o1);
	Q.push(o2);
	while (!Q.empty()) 
	{ 
		OrderUnit *p = Q.top(); 
		Q.pop();
		cout << p->getPrice() << "\n"; 
	}

	delete o1;
	delete o2;
	delete o3;
	delete o4;
	return 0;
}
