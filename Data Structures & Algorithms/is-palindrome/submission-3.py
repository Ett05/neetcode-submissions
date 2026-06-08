class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.strip()
        new_string = ""
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for char in string:
            if char not in alphabet:
                print(char)
                continue
            else:
                new_string += char.lower()
        print(new_string)
        return new_string == new_string[::-1]