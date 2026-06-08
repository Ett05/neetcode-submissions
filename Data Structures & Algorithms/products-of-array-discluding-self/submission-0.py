class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)    
        prefix_product = 1
        suffix_product = 1
        for i in range(len(nums)):
            prefix[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix_product
            suffix_product *= nums[i]
        return [prefix[i]*suffix[i] for i in range(len(nums))]