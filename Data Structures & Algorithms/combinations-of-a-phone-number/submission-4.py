class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno",
            "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        res = []
        path = []
        def dfs(i, digits):
            if i >= len(digits):
                if i > 0:
                    res.append("".join(path[:]))
                return 
            digit = digits[i]
            for c in dic[digit]:
                path.append(c)
                dfs(i + 1, digits)
                path.pop()
        dfs(0, digits)
        return res