class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_so_far = set()
        max_lenght_so_far = 0
        l = 0
        "abcabcbb"
        for r in range(0, len(s)):
            while s[r] in letters_so_far:
                letters_so_far.remove(s[l])
                l += 1
            letters_so_far.add(s[r])
            max_lenght_so_far = max(max_lenght_so_far, r-l+1)
        
        return max_lenght_so_far