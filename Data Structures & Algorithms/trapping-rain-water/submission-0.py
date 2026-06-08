class Solution:
    def trap(self, height: List[int]) -> int:
        water_heights = [0 for i in range(len(height))]
        water_heights[0] = 0
        water_heights[-1] = 0
        left_max = [ 0 for i in range(len(height))]
        left_max[0] = 0
        right_max = [ 0 for i in range(len(height))]
        right_max[-1] = 0

        for i in range(1, len(height)):
            left_max[i] = max(height[:i])
        for i in range(len(height)-1):
            right_max[i] = max(height[i+1:])
        print(left_max)
        print(right_max)
        for i in range(len(height)):
            water_heights[i] = max((min(left_max[i], right_max[i]) - height[i]), 0)
        # return sum([(min(left_max[i], right_max[i]) - height[i]) for i in range(len(height))])
        # for i in range(1, len(heights)-1):
        print(water_heights)
        return sum(water_heights)

        