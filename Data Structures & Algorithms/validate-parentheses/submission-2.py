class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")" : "(", "}" : "{", "]": "["}
        for ch in s:
            if ch in brackets:
                if not stack : return False
                if stack.pop() != brackets[ch]: return False
            else:
                stack.append(ch)
        
        if len(stack) == 0:
            return True
        else:
            return False

        