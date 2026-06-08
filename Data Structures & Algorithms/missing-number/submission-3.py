class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = -1 
        for num in range(len(nums)+1):
            if curr+1 not in nums:
                return num
            curr += 1