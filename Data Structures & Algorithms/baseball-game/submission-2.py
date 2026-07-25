class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        val = 0
        for c in operations:
            if c == "+":
                temp = stack[-1] + stack[-2]
                stack.append(temp)
                val += temp
            elif c == "C":
                temp = stack.pop()
                val -= temp
            elif c == "D":
                temp = stack[-1] * 2
                stack.append(temp)
                val += temp
            else:
                temp = int(c)
                stack.append(temp)
                val += temp
        return val