class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = digits[::-1]

        carry = 1
        for i in range(len(new_digits)):
            value = new_digits[i] + carry
            if value == 10 and i == len(new_digits) - 1:
                new_digits[i] = 0
                new_digits.append(1)
            elif value == 10:
                new_digits[i] = 0
            else:
                new_digits[i] = value
                carry = 0
                break
        
        return new_digits[::-1]
