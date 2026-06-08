class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l = i + 1
            r = len(nums) - 1
            visited = set()
            while l < r:
                val = nums[l] + nums[r] + nums[i]
                if nums[l] in visited:
                    l += 1
                elif nums[r] in visited:
                    r -= 1
                else:
                    if (val) == 0:
                        output.append([nums[i], nums[l], nums[r]])
                        visited.add(nums[l])
                        visited.add(nums[r])
                        l += 1
                    elif val < 0:
                        visited.add(nums[l])
                        l += 1
                    else:
                        visited.add(nums[r])
                        r -= 1
        return output

