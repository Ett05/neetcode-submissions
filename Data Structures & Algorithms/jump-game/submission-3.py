class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp_array = [False] * len(nums)
        dp_array[0] = True
        for i in range(1, len(nums)):
            dp_array[i] = any([dp_array[j] for j in range(i) if nums[j] >= i - j])
        return dp_array[-1]