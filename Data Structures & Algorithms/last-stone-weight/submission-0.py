class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)
        if len(sorted_stones) == 1:
            return sorted_stones[0]
        while (len(sorted_stones)) > 1:
            last = sorted_stones[-1]
            second_last = sorted_stones[-2]
            sorted_stones.pop()
            sorted_stones.pop()
            print(sorted_stones)
            if (last > second_last):
                value = last - second_last
                sorted_stones.append(value)
                sorted_stones = sorted(sorted_stones)
        if sorted_stones:
            return sorted_stones[0]
        else:
            return 0