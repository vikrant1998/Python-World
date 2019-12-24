#include <iostream>
#include <vector>
#include <sstream>
#include <stdexcept>
#include <queue>

#include "SamePriceOrderChain.hpp"

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
	// OrderUnit o1 = OrderUnit(100);
	// OrderUnit o2 = OrderUnit(902);
	// OrderUnit o3 = OrderUnit(81);
	// OrderUnit o4 = OrderUnit(10002);

	// priority_queue<OrderUnit, vector<OrderUnit>, BuyComparison> Q; 
	// Q.push(o1);
	// Q.push(o2);
	// Q.push(o3);
	// Q.push(o4);

	// while (!Q.empty()) 
	// { 
	// 	OrderUnit p = Q.top(); 
	// 	Q.pop(); 
	// 	cout << p.getPrice() << "\n"; 
	// }

	SamePriceTimeOrderChain s;
	Order *order1 = new Order(1, 1, 1, 1, 1);
	Order *order2 = new Order(1, 1, 1, 1, 2);
	Order *order3 = new Order(1, 1, 1, 1, 3);
	Order *order4 = new Order(1, 1, 1, 1, 4);
	Order *order5 = new Order(1, 1, 1, 1, 5);
	s.InsertIntoChain(order1);
	s.InsertIntoChain(order2);
	s.InsertIntoChain(order3);
	s.InsertIntoChain(order4);
	s.InsertIntoChain(order5);
	s.PrintChain();
	cout << endl;
	s.PrintChainRev();
	return 0;
}
