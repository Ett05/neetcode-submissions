class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = -1
        for i in range(len(prices)):
            max_profit_so_far = max(max(prices[i:])-prices[i], max_profit_so_far)
        
        return max_profit_so_far
