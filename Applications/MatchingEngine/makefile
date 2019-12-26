compile: MatchingEngine.cpp
	g++ SamePriceOrderChain.hpp SamePriceOrderChain.cpp OrderUnit.hpp Order.hpp OrderBook.hpp OrderBook.cpp MatchingEngine.cpp -o MatchingEngine

test:
	touch Testcases/ExpectedOutput/EmptyFile.txt

	./MatchingEngine < Testcases/SampleTest.txt > Testcases/Output/SampleTest_Output.txt
	diff Testcases/Output/SampleTest_Output.txt Testcases/ExpectedOutput/SampleTest_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/EmptyBuyBook.txt > Testcases/Output/EmptyBuyBook_Output.txt
	diff Testcases/Output/EmptyBuyBook_Output.txt Testcases/ExpectedOutput/EmptyBuyBook_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/EmptySellBook.txt > Testcases/Output/EmptySellBook_Output.txt
	diff Testcases/Output/EmptySellBook_Output.txt Testcases/ExpectedOutput/EmptySellBook_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/PassiveBuy.txt > Testcases/Output/PassiveBuy_Output.txt
	diff Testcases/Output/PassiveBuy_Output.txt Testcases/ExpectedOutput/EmptyFile.txt -w

	./MatchingEngine < Testcases/PassiveSell.txt > Testcases/Output/PassiveSell_Output.txt
	diff Testcases/Output/PassiveSell_Output.txt Testcases/ExpectedOutput/EmptyFile.txt -w

	./MatchingEngine < Testcases/CancelAfterFFill.txt > Testcases/Output/CancelAfterFFill_Output.txt
	diff Testcases/Output/CancelAfterFFill_Output.txt Testcases/ExpectedOutput/CancelAfterFFill_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/CancelAfterPFill.txt > Testcases/Output/CancelAfterPFill_Output.txt
	diff Testcases/Output/CancelAfterPFill_Output.txt Testcases/ExpectedOutput/CancelAfterPFill_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/AggressiveBuy_1.txt > Testcases/Output/AggressiveBuy_1_Output.txt
	diff Testcases/Output/AggressiveBuy_1_Output.txt Testcases/ExpectedOutput/AggressiveBuy_1_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/AggressiveBuy_2.txt > Testcases/Output/AggressiveBuy_2_Output.txt
	diff Testcases/Output/AggressiveBuy_2_Output.txt Testcases/ExpectedOutput/AggressiveBuy_2_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/AggressiveSell_1.txt > Testcases/Output/AggressiveSell_1_Output.txt
	diff Testcases/Output/AggressiveSell_1_Output.txt Testcases/ExpectedOutput/AggressiveSell_1_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/AggressiveSell_2.txt > Testcases/Output/AggressiveSell_2_Output.txt
	diff Testcases/Output/AggressiveSell_2_Output.txt Testcases/ExpectedOutput/AggressiveSell_2_ExpectedOutput.txt -w

	./MatchingEngine < Testcases/CancelAll.txt > Testcases/Output/CancelAll_Output.txt
	diff Testcases/Output/CancelAll_Output.txt Testcases/ExpectedOutput/CancelAll_ExpectedOutput.txt -w

	rm -rf Testcases/Output/*
	rm -rf Testcases/ExpectedOutput/EmptyFile.txt