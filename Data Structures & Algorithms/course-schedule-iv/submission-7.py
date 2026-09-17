class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        adj = {i:[] for i in range(n)}
        for a, b in prerequisites:
            adj[a].append(b)
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for j in adj[i]:
                dfs(j)
            topSort.add(i)
            return 
        res = []
        for u, v in queries:
            topSort = set()
            visit = set()
            dfs(u)
            print(u)
            print(topSort)
            if v in topSort:
                res.append(True)
            else:
                res.append(False)
        return res