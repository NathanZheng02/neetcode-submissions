class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda pair : pair[0])

        minHeap = [] # (length, end)
        res = {} # Map eaach query to the result
        i = 0 # Make sure we are only moving once through intervals

        # O(qlog(q) + nlog(n))
        for q in sorted(queries):
            # O(n)
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                length = end - start + 1

                # O(log(n))
                heapq.heappush(minHeap, (length, end))
                i += 1
            
            # Remove intervals past query val
            while minHeap and minHeap[0][1] < q:
                # O(log(q))
                heapq.heappop(minHeap)
            
            # Adding to result
            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1
            
        return [res[q] for q in queries]


