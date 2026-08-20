class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search space from 0 to x / 2
        l, r = 0, int(x / 2) + 1
        
        while l <= r:
            mid = int(l + (r - l) / 2)
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            elif square < x:
                l = mid + 1

        # r is less than or equal to l if it exists, which is the smaller of the both        
        return r