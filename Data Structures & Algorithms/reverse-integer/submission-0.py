class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = sign * int(str(x)[::-1])
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res
