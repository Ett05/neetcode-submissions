class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp_array = [0] * (len(cost))
        dp_array[0] = cost[0]
        dp_array[1] = cost[1]
        dp_array[-1] = 0
        for i in range(2, len(cost)):
            dp_array[i] = min(dp_array[i-1], dp_array[i-2]) + cost[i]
        
        return dp_array[-1]
