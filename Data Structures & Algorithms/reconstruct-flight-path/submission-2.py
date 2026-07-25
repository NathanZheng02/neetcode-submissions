class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euclidean Path
        adj = defaultdict(list)

        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)
        
        res = []
        def dfs(port):
            # Post order traversal (Add last before curr node)
            while adj[port]:
                dest = adj[port].pop()
                dfs(dest)
            res.append(port)
        dfs("JFK")
        # Flip because of post-order
        return res[::-1]