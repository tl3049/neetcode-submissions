class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        #Set adj list
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
        #DFS for topological sort
        def dfs(i, topSort, visit, path):
            if i in path:
                return False
            if i in visit:
                return True
            visit.add(i)
            path.add(i)
            for j in adj[i]:
                if not dfs(j, topSort, visit, path):
                    return False
            topSort.append(i)
            path.remove(i)
            return True
        #Iteration for all possible nodes
        topSort = []
        visit = set()
        path = set()
        for i in range(n):
            if not dfs(i, topSort, visit, path):
                return []
        topSort.reverse()
        return topSort