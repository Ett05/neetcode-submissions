class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in dictionary:
                dictionary[key].append(string)
            else:
                dictionary[key] = [string]
        
        return list(dictionary.values())