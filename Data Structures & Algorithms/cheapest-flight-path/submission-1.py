class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Cost to get from source node to others
        prices = [float("inf")] * n
        prices[src] = 0

        # Adjacency List
        adj = [[] for _ in range(n)]
        for u, v, price in flights:
            adj[u].append((v, price))
        
        # k stops BFS
        q = deque([(0, src, 0)]) # (Cost, Node, Visited Count)
        while q:
            cost, n, count = q.popleft()

            # Stopping condition
            if count > k:
                continue
            
            for nei, wei in adj[n]:
                nextCost = cost + wei
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, count + 1))
        
        return prices[dst] if prices[dst] != float("inf") else -1
