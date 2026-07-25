class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1 if n >= 0 else -1
        n = abs(n)

        res = 1
        for i in range(n):
            res *= x
        if sign == 1:
            return res
        else:
            return 1 / res