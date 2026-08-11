class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force
        n = len(s)
        longest = 0
        for i in range(n):
            m = 0
            dic = {}
            for j in range(i, n):
                if s[j] in dic:
                    break
                else:
                    dic[s[j]] = dic.get(s[j],0) + 1
                    m = m + 1
            longest = max(longest, m)
        return longest