import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        # value = self.nums[1]
        heapq.heappush(self.nums, val)
        print(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
            print(self.nums)
        return self.nums[0]
        # if self.k >= len(self.nums) - 1:
        #     heapq.heappush(self.nums,val)
        #     while self.k >= len(self.nums) - 1:
        #         heapq.heappop(self.nums)
        # print(self.nums)
        # return self.nums[-1]
        
