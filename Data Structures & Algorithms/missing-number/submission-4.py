class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # curr = -1 
        # for num in range(len(nums)+1):
        #     if curr+1 not in nums:
        #         return num
        #     curr += 1
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
        actual_sum = len(nums)*(len(nums) + 1)
        actual_sum = int(actual_sum/2)
        return actual_sum - sum_so_far