class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Construct adj list
        n = numCourses
        adj = {i:[] for i in range(n)}
        for a, b in prerequisites:
            adj[a].append(b)
        #Topological sort by dfs
        path = set()
        visit = set()
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            visit.add(i)
            path.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            return True           
        for i in range(n):
            if not dfs(i):
                return False
        return True
        
        #Iteration for all courses
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not prerequisites:
        #     return True
        # dic = {}
        # for nxt, pre in prerequisites:
        #     if pre in dic:
        #         dic[pre].append(nxt)
        #     else:
        #         dic[pre] = [nxt]
        # visited = set()
        # path = set()
        # def dfs(num):
        #     if num not in dic:
        #         return True
        #     if num in path:
        #         return False
        #     if num in visited:
        #         return True
        #     visited.add(num)
        #     path.add(num)
        #     for child in dic[num]:
        #         val = dfs(child)
        #         if not val:
        #             return False
        #     path.remove(num)
        #     return True
        # for i in range(numCourses):
        #     if i not in visited:
        #         res = dfs(i)
        #         if not res:
        #             return False
        # return True
