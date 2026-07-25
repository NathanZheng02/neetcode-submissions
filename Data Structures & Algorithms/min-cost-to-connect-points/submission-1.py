class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visited = set()
        minHeap = [(0, 0)]

        # Repeat until all nodes are connected
        while len(visited) < n:
            cost, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            res += cost
            visited.add(n1)

            for wei, nei in adj[n1]:
                if nei not in visited:
                    heapq.heappush(minHeap, (wei, nei))

        return res

