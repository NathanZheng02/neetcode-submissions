class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "+":
                sec = stack[-1]
                first = stack[-2]
                third = first + sec
                stack.append(third)
            elif c == "C":
                stack.pop()
            elif c == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(c))
        
        # Sum and return
        val = 0
        for i in stack:
            val += i
        return val