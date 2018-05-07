def buy_and_sell_stock_once(prices):
	if len(prices) < 2:
		return 0
		
	smallest = prices[0]
	maxProfit = -float('inf')

	for i in range(1, len(prices)):
		maxProfit = max(maxProfit, prices[i] - smallest)
		smallest = min(smallest, prices[i])

	return maxProfit if maxProfit > 0 else 0


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
