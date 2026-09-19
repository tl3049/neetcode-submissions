class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dic = {}
        for i in range(len(strs)):
            dic[i] = [0, 0]
            for c in strs[i]:
                if c == "0":
                    dic[i][0] += 1
                if c == "1":
                    dic[i][1] += 1
        memo = {}
        def dfs(i, cnt_zero, cnt_one):
            if i >= len(strs):
                if cnt_zero <= m and cnt_one <= n:
                    return (True, 0)
                return (False, 0)
            if cnt_zero > m or cnt_one > n:
                return (False, 0)
            if (i, cnt_zero, cnt_one) in memo:
                return memo[(i, cnt_zero, cnt_one)]
            skip = dfs(i + 1, cnt_zero, cnt_one)
            choose = dfs(i + 1, cnt_zero + dic[i][0], cnt_one + dic[i][1])
            if skip[0] and choose[0]:
                res = (True, max(skip[1], 1 + choose[1]))
            elif skip[0] and not choose[0]:
                res = (True, skip[1])
            elif not skip[0] and choose[0]:
                res = (True, 1 + choose[1])
            else:
                res = (False, 0)
            memo[(i, cnt_zero, cnt_one)] = res
            return  res
        res = dfs(0, 0, 0)
        return res[1]
