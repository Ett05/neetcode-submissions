class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp_array = [amount+1] * (amount+1)
        dp_array[0] = 0
        for i in range(1, amount+1):
           dp_array[i] = min(
                [dp_array[i - coin] for coin in coins if i - coin >= 0], 
                default=amount
            ) + 1
        print(dp_array)
        if dp_array[-1] > amount:
            return -1
        else:
            return dp_array[-1]