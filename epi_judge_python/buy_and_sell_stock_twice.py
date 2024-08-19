from typing import List

from test_framework import generic_test
import math


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    best_profit, cur_min = 0, math.inf
    first_pass_profits=[0]*len(prices)
    for i in range(len(prices)):
        if prices[i]<cur_min:
            cur_min=prices[i]
        best_profit=max(best_profit, prices[i]-cur_min)
        first_pass_profits[i]=best_profit

    best_profit, cur_max = 0, -math.inf
    second_pass_profits=[0]*len(prices)
    for i in range(len(prices)-1, -1, -1):
        if prices[i]>cur_max:
            cur_max=prices[i]
        best_profit=max(best_profit, cur_max-prices[i])
        second_pass_profits[i]=best_profit

    # Combine the two passes and identify the best profit when first selling by day i buying again on day i+1
    # Because of that we add one more day to `second_pass_profits` with 0 since you cannot buy again if we sell on the last day
    best_profit=0
    second_pass_profits.append(0)
    for i in range(len(prices)):
        best_profit=max(best_profit, first_pass_profits[i]+second_pass_profits[i+1])
    
    return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
