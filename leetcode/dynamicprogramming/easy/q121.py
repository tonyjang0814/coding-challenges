class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        _min = float('inf')
        profit = 0
        for price in prices:
            if price < _min:
                _min = price
            profit = max(profit,price-_min)
        return profit