import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        min_so_far = right
        while left <= right:
            mid = (right + left)//2
            if self.calc_hours(mid, piles) > h:
                left = mid + 1
            else:
                min_so_far = mid
                right = mid - 1
        return min_so_far
        
    def calc_hours(self, k_value, piles):
        hours = 0
        for p in piles:
            hours += math.ceil(p/k_value)
        return hours
