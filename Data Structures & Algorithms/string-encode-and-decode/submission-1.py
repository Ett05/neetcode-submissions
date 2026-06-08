class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for string in strs:
            return_string += string[::-1]
            return_string+="`"
        return return_string

    def decode(self, s: str) -> List[str]:
        list_of_strings = []
        word_string = ""
        for char in s:
            if char != "`":
                word_string += char
            else:
                list_of_strings.append(word_string[::-1])
                word_string = ""
        return list_of_strings