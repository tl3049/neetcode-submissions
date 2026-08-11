class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        count = {}#record the frequencies of chars in the window
        maxlen = 0
        for r in range(n):
            count[s[r]] = count.get(s[r],0) + 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen
              