import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        heap = []
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1
        for freq in freq_table:
            if len(heap) < k:
                heapq.heappush(heap, (freq_table[freq], freq))
            else:
                smallest = heap[0][0]
                print(smallest)
                print(freq_table[freq])
                if freq_table[freq] > smallest:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq_table[freq], freq))

        print(heap)
        return [element[1] for element in heap]
