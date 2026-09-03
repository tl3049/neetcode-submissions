class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        dic = {}
        for nxt, pre in prerequisites:
            if pre in dic:
                dic[pre].append(nxt)
            else:
                dic[pre] = [nxt]
        visited = set()
        path = set()
        def dfs(num):
            if num not in dic:
                return True
            if num in path:
                return False
            if num in visited:
                return True
            visited.add(num)
            path.add(num)
            for child in dic[num]:
                val = dfs(child)
                if not val:
                    return False
            path.remove(num)
            return True
        for i in range(numCourses):
            if i not in visited:
                res = dfs(i)
                if not res:
                    return False
        return True
