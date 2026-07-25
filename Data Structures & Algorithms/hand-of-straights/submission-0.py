class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {} # Key = Number, Val = Counter
        for val in hand:
            count[val] = count.get(val, 0) + 1

        heap = [] # Min Heap to find smallest value
        for num in count:
            heapq.heappush(heap, num)
        heapq.heapify(heap)

        while heap:
            min_val = heap[0]
            
            for i in range(min_val, min_val + groupSize):
                if i not in count:
                    return False

                count[i] -= 1

                # When counter runs out, pop from min heap
                if count[i] == 0:
                    # If i is not the minimum, that means
                    # there is a smaller value in the heap which
                    # causes a gap between future values
                    if i != heap[0]:
                        return False
                        
                    heapq.heappop(heap)
        return True
            
        
        
        



