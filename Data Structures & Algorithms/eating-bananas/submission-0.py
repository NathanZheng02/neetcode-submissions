class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for banana in piles:
                hours += math.ceil(banana / mid)
            
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
