"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if not node:
                return node
            if node in visited:
                return visited[node]
            root = Node(node.val)
            visited[node] = root
            for child in node.neighbors:
                n = dfs(child)
                root.neighbors.append(n)
            #visited.pop(node)
            return root
        return dfs(node)