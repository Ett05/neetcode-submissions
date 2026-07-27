class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp array max(i-1, i-2+nums[i])
        dp_array = [0] * len(nums)
        dp_array_2 = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        dp_array[0] = nums[0]
        dp_array[1] = max(nums[0], nums[1])
        dp_array_2[1] = nums[1]
        dp_array_2[1] = nums[1]
        dp_array_2[2] = max(nums[1], nums[2])
        
        for i in range(2, len(nums)-1):
            dp_array[i] = max(dp_array[i-1], dp_array[i-2] + nums[i])

        for i in range(3, len(nums)):
            dp_array_2[i] = max(dp_array_2[i-1], dp_array_2[i-2] + nums[i])
        print(dp_array)
        print(dp_array_2)
        return max(dp_array[-2], dp_array_2[-1])