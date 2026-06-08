class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = [[]]
        
        for num in nums:
            new_subsets = [curr + [num] for curr in solution]
            solution.extend(new_subsets)
            
        return solution
        