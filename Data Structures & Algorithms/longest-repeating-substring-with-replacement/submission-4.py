class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        char_map = {}
        max_value = 1
        while l <= r and r < len(s):
            if s[r] in char_map:
                char_map[s[r]] += 1
            else:
                char_map[s[r]] = 1
            
            max_freq = max(char_map.values())
            if ((r-l+1 - max_freq) > k):
                char_map[s[l]] -= 1
                l += 1
                
            else:
                max_value = max(max_value, r-l+1)
            r+=1
                            
        return max_value
            

