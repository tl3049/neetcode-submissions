class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = {i:[] for i in range(n)}
        for a, b in prerequisites:
            adj[a].append(b)
        topSort = []
        path = set()
        visit = set()
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            path.add(i)
            visit.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            topSort.append(i)
            path.remove(i)
            return True
        for i in range(n):
            if not dfs(i):
                return []
        return topSort        