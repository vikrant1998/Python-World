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
	OrderBook orderBook;
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
			cout << "BAD MESSAGE: Invalid Input" << endl;
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
			cout << "BAD MESSAGE: Invalid Input" << endl;
			continue;
		}

		// New Order.
		if(result.size() == 5)
		{
			orderBook.addToBook(msgType, orderid, side, quantity, price);
		}
		else if(result.size() == 2)
		{
			orderBook.cancelOrder(msgType, orderid);
		}
		
	}
}

int main()
{
	ParseInput();
	return 0;
}
