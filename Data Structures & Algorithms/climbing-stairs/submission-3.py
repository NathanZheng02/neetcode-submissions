class Solution:
    def climbStairs(self, n: int) -> int:
        # Simplify to 2 pointers
        # minus2 represents taking 2 steps while minus1 represents taking 1 step
        minus2, minus1 = 1, 1

        for i in range(2, n + 1):
            curr = minus2 + minus1
            minus2 = minus1
            minus1 = curr
        
        # minus1 started at 1 and goes till n
        return minus1