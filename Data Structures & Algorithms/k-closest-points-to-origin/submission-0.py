class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist.append((math.sqrt(x ** 2 + y ** 2), i))
        heapq.heapify(dist)

        for i in range(k):
            distance, index = heapq.heappop(dist)
            res.append(points[index])
        return res

