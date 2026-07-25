class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack:
                return False
            elif brackets[stack.pop()] != char:
                return False
        if stack:
            return False
        else:
            return True