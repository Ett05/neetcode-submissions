class Solution:
    def rob(self, nums: List[int]) -> int:
        # max amount of money so far 
        # dp_array = [0] *  

        # max_value_1 = 0
        # max_value_2 = 0
        # for i in range(0, len(nums), 2):
        #     max_value_1 += nums[i]
        # for i in range(1, len(nums), 2):
        #     max_value_2+= nums[i]

        # return max(max_value_1, max_value_2)
        if len(nums) == 1:
            return nums[0]
        dp_array = [0] * len(nums)
        dp_array[0] = nums[0]
        dp_array[1] = max(nums[1], dp_array[0])
        # dp_array[2] = nums[0] + nums[2]
        for i in range(2, len(nums)):
            dp_array[i] = max(dp_array[i-1], dp_array[i-2] + nums[i])
        print(dp_array)
        return dp_array[-1]