class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Not a valid tree if there are cycles
        # If |E| > |V - 1|, then it isn't a tree (too many edges)
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node, prev):
            # Cycle detection
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                # Pass along False returns from recursive calls
                if dfs(nei, node) == False:
                    return False
            return True  
        
        # Start at node 0 and previous node at -1
        return dfs(0, -1) and len(visited) == n