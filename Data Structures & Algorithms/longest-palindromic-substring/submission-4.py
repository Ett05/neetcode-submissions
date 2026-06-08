class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return 0
        longest_paildrome_so_far = (s[0], 1)
        for i in range(len(s)):
            for j in range(i, len(s)):
                val = s[i:j+1]
                print(s[i])
                print(s[j])
                print(val, val[::-1])
                if val == val[::-1] and len(val) > longest_paildrome_so_far[1]:
                    longest_paildrome_so_far = (val, len(val))
        return longest_paildrome_so_far[0]
                    