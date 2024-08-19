from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    best_profit=0
    cur_min=prices[0]
    for i in range(1, len(prices)):
        if prices[i]<cur_min:
            cur_min=prices[i]
        else:
            best_profit=max(best_profit, prices[i]-cur_min)
    
    return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
