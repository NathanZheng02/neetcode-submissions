class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Prices to go from src node to each one
        prices = [float("inf")] * n
        prices[src] = 0
        
        # Adjacency List to map each edge and cost for each one
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append([v, cost])
        
        # BFS k times approach
        queue = deque([(0, src, 0)]) # Curr cost, curr node, nodes in path
        while queue:
            cost, node, stops = queue.popleft()

            # Skip if depth > k
            if stops > k:
                continue
            
            for nei, dist in adj[node]:
                nextCost = cost + dist
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    queue.append((nextCost, nei, stops + 1))
        
        return prices[dst] if prices[dst] != float("inf") else -1
