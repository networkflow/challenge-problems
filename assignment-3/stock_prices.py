from itertools import accumulate


# Given a list of stock prices, returns the maximum profit that could've been
# made by buying the stock at one point and selling it later (or 0 if no profit
# could've been made)
#
# Runs in O(n) time (if parallelized still runs in O(n)):
def maximumStockProfitImperative(prices: list[int]) -> int:
    # We want to set minPriceSoFar to the first price, so we'll handle the
    # empty list case specially:
    if len(prices) == 0:
        return 0

    # Algorithm:
    # * We will iterate over all the prices, and calculate the maximum profit
    #   that could be made if we sold the stock at that price
    #   * The maximum profit that can be made by selling a stock at a given
    #     price is by buying the stock at the minimum possible previous price
    #     and then selling it at this given price
    #   * If we keep track of the minimum price seen so far (minPriceSoFar), 
    #     then the maximum profit we can make selling it at the current price
    #     (price) is
    #       price - minPriceSoFar
    # * If we take the maximum of all these values, then we'll calculate the
    #   maximum possible profit selling at any point
    # * Even if the prices are all decreasing (e.g. [3, 2, 1]), we'll handle
    #   that by setting minPriceSoFar to include the current price, so you're
    #   allowed to buy and sell at the same time, resulting in a profit of 0
    minPriceSoFar = prices[0]
    maxProfitSoFar = 0
    for price in prices:
        minPriceSoFar = min(minPriceSoFar, price)
        maxProfitSoFar = max(maxProfitSoFar, price - minPriceSoFar)
    return maxProfitSoFar


# Given a list of stock prices, returns the maximum profit that could've been
# made by buying the stock at one point and selling it later (or 0 if no profit
# could've been made)
#
# Runs in O(n) time (if parallelized runs in O(log n), which is better than the
# imperative version):
def maximumStockProfitFunctional(prices: list[int]) -> int:
    # We can't take the max of an empty sequence (in the code later), so we'll
    # consider the profit of an empty sequence to be 0:
    if len(prices) == 0:
        return 0
    
    # Algorithm: same algorithm as in the imperative version, except that we'll
    # use functional-programming functions (accmulate, map, reduce) which can
    # be parallelized to run in O(log n) time.

    # `accumulate` is kind of like reduce, except that it keeps track of all the
    # partial results. For example, 
    #   accumulate([1, 1, 1, 1], lambda x, y: x + y)
    #     = [1, 2, 3, 4]
    #   accumulate([2, 3, 1, 4], lambda x, y: min(x, y))
    #     = [2, 2, 1, 1]
    #
    # Surprisingly, the `accumulate` function can be parallelized to run in
    # O(log n) time (runs in O(n) time normally):
    runningMinimums = accumulate(prices, min)
    return max(
        price - minPriceSoFar
        for price, minPriceSoFar in zip(prices, runningMinimums)
    )
