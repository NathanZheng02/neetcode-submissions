class Solution:
    def myPow(self, x: float, n: int) -> float:
        def halfMultiply(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            # Keep multiplying until n becomes 0
            res = halfMultiply(x * x, n // 2)

            # Multiply by extra x if current n is odd
            return x * res if n % 2 == 1 else res


        sign = 1 if n >= 0 else -1
        res = halfMultiply(x, abs(n))

        if sign == 1:
            return res
        else:
            return 1 / res