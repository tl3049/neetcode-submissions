class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ##OPTIMAL PROCESS WHEN GENERATE
        ##Adj list
        adj = {i:[] for i in range(numCourses)}
        for ai, bi in prerequisites:
            adj[bi].append(ai)
        ##Topological sort
        visit = {}
        def dfs(i):
            if i in visit:
                return 
            visit[i] = set()
            for j in adj[i]:
                if j not in visit:
                    dfs(j)
                visit[i] |= visit[j]
            visit[i].add(i)
            return
        ##Iteration for all nodes
        for i in range(numCourses):
            dfs(i)
        res = []
        for uj, vj in queries:
            res.append(uj in visit[vj])
        return res

        #BRUTE FORCE; POST PROCESSING
        # adj = {i:[] for i in range(numCourses)}
        # for a, b in prerequisites:
        #     adj[b].append(a)
        # def dfs(i):
        #     if i in visit:
        #         return 
        #     visit.add(i)
        #     for j in adj[i]:
        #         dfs(j)
        #     topSort.add(i)
        #     return 
        # res = []
        # for u, v in queries:
        #     topSort = set()
        #     visit = set()
        #     dfs(v)
        #     if u in topSort:
        #         res.append(True)
        #     else:
        #         res.append(False)
        # return res