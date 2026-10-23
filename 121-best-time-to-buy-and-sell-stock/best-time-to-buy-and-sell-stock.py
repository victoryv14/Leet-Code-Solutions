class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_cost = float('inf')
        profit = -float('inf')
        for price in prices :
            min_cost = min(min_cost,price)
            profit = max(profit,price - min_cost)
        return profit