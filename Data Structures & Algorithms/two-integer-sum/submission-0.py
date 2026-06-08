class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicataionary = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dicataionary:
                return [dicataionary[target - nums[i]], i]
            else:
                dicataionary[nums[i]] = i
        