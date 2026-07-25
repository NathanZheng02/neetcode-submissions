class MedianFinder:

    def __init__(self):
        # Small holds the smaller values as negatives for max heap
        # Large holds the larger values and keeps track of the smallest
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # Rebalance both halves
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        

    def findMedian(self) -> float:
        # Odd cases:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # Even cases:
        left = -self.small[0]
        right = self.large[0]
        return (left + right) / 2
        
        