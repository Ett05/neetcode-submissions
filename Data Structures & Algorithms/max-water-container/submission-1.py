class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_so_far = 0
        l, r = 0, len(heights) - 1
        while l < r:
            max_water_so_far = max(max_water_so_far, (r-l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water_so_far