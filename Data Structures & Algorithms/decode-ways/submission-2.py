class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
             return 0 
        n = len(s)
        if n == 1:
            return 1
        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1
        prepre = pre = 1
        for i in range(2, n+1):
            prenum = int(s[i-2])
            num = int(s[i-1])
            val = prenum * 10 + num
            c1 = 0
            if val > 0 and val < 27 and prenum is not 0:
                c1 = prepre
                #c1 = dp[i - 2]
            c2 = 0
            if num > 0 and num < 10:
                c2 = pre
                #c2 = dp[i - 1]
            now = c1 + c2
            prepre = pre
            pre = now
            #dp[i] = c1 + c2
        return pre#dp[n]
