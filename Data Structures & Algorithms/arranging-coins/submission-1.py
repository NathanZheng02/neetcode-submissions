class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
            
        count = 1
        while n > count:
            n -= count
            count += 1
        return count - 1