class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Adjacency List
        n = len(points)

        adj = {i : [] for i in range(n)} # [cost, node]
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim
        res = 0
        visited = set()
        frontier = [[0, 0]] # [cost, point]
        print(adj)
        while len(visited) < n:
            cost, point = heapq.heappop(frontier)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            for neiCost, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(frontier, [neiCost, nei])
        return res
