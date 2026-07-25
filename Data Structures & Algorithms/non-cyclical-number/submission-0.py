class Solution:
    def isHappy(self, n: int) -> bool:
        # Cycle detection
        slow, fast = n, self.sumSquares(n)

        while slow != fast:
            fast = self.sumSquares(self.sumSquares(fast))
            slow = self.sumSquares(slow)
        return True if fast == 1 else False

    def sumSquares(self, n):
        res = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            res += digit ** 2
        return res