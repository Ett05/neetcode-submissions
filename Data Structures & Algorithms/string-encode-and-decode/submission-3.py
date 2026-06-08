class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for string in strs:
            return_string += str(len(string))
            return_string += "#"
            return_string += string
        return return_string

    def decode(self, s: str) -> List[str]:
        list_of_strings = []
        counting = ""
        word = ""
        i=0
        while i < len(s):
            if s[i] == "#":
                print(counting)
                word = (s[i+1: i+int(counting)+1])
                i += int(counting) + 1
                list_of_strings.append(word)
                word = ""
                counting = ""
            else:
                counting += s[i]
                i += 1
        return list_of_strings
