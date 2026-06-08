class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = -1
        min_value = prices[0]
        for price in prices:
            min_value = min(min_value, price)
            max_profit_so_far = max((price - min_value), max_profit_so_far)
        
        return max_profit_so_far
