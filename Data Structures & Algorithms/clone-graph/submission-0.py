"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned_map = {}

        def dfs(curr):
            # If we already have the node in the map, we return copy of the node 
            if curr in cloned_map:
                return cloned_map[curr]
            
            # Create copy of node and add to cloned map
            new_node = Node(curr.val)
            cloned_map[curr] = new_node

            # Recursively "link" nodes with edges by adding to neighbors
            for nei in curr.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            # Return cloned node to be linked
            return new_node

        return dfs(node) if node else None