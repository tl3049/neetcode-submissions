class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        #ONE DIC 
        visit = {}#path:True; visited:False
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for d in adj[c]:
                if dfs(d):
                    return True
            visit[c] = False
            res.append(c)
            return False
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)






        #TWO SETS
        # visit, path = set(), set()
        # topSort = []
        # def dfs(c):
        #     if c in path:
        #         return False
        #     if c in visit:
        #         return True
        #     visit.add(c)
        #     path.add(c)
        #     for d in adj[c]:
        #         if not dfs(d):
        #             return False
        #     topSort.append(c)
        #     path.remove(c)
        #     return True
        # for c in adj:
        #     if not dfs(c):
        #         return ""
        # topSort.reverse()
        # return "".join(topSort)
