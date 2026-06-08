class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if n == 2 or n == 3 or n == 1:
            return n
        dp_array = [2, 3]
        for i in range(3, n):
            count = dp_array[0] + dp_array[1]
            dp_array[0] = dp_array[1]
            dp_array[1] = count
            print(i ,dp_array)
            print(count)

        return count