import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        heap = []
        for point in points:
            distances[tuple(point)] = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
        for key in distances:
            if len(heap) < k:
                heapq.heappush(heap, [-distances[key], key])
            else:
                if heap[0][0] < -distances[key]:
                    print("HELLO")
                    heapq.heappop(heap)
                    heapq.heappush(heap,[-distances[key], key])
        print(distances)
        print(heap)

        return [list(point[1]) for point in heap]