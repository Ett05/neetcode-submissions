class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # largest sum 
        # dp_array = [0] * len(nums)
        # for i in range(len(nums)):
        #     dp_array[i] = max(dp_array[i-1], )
        # if len(nums) == 1:
        #     return nums[0]
        # nums.sort()
        # l, r = 0, len(nums) - 1
        # max_sum = -1000
        # while l < r:
        #     print(nums[l:r])
        #     max_sum = max(max_sum, sum(nums[l:r]))
        #     l += 1
        # return max_sum
        dp_array = [-1000] * len(nums)
        dp_array[0] = nums[0]
        for i in range(1, len(nums)):
            dp_array[i] = max(dp_array[i-1] + nums[i], nums[i])
        return max(dp_array)
