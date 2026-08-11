class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(len(wordDict)):
                word = wordDict[j]
                L = len(word)
                if i - L >= 0:
                    if s[(i-L):i] == word:
                        dp[i] = dp[i] or (dp[i - L] and True)
            # print("i",i)
            # print("dp[i]",dp[i])
        return dp[n]