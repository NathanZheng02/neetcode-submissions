class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node

            while res != parent[res]:
                # Path compression: set the parent of node to 
                # the grandparent if available to shorten path time
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            # Size of connected components
            if rank[p2] > rank[p1]:
                # Set parents and absorb remaining nodes
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for u, v in edges:
            res -= union(u, v)
        return res
        
