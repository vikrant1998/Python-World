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

int main()
{
	//ParseInput();
	OrderBook orderBook;
	orderBook.addToBook(0, 1, 0, 10, 10.0);
	orderBook.addToBook(0, 2, 0, 10, 10.0);
	orderBook.addToBook(0, 3, 0, 10, 10.0);
	orderBook.addToBook(0, 4, 0, 10, 12.0);
	orderBook.addToBook(0, 5, 0, 10, 12.0);
	orderBook.addToBook(0, 6, 0, 10, 9.0);
	orderBook.addToBook(0, 7, 0, 10, 102.0);

	orderBook.printBuyBook();
	orderBook.cancelOrder(1, 1);
	orderBook.cancelOrder(1, 2);
	orderBook.cancelOrder(1, 3);
	orderBook.cancelOrder(1, 4);
	orderBook.cancelOrder(1, 5);
	orderBook.cancelOrder(1, 6);
	orderBook.printBuyBook();

	return 0;
}
