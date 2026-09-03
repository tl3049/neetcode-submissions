class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window = set()
        # L = 0
        # res = 0
        # length = 0
        # for R in range(len(s)):
        #     c = s[R]
        #     if c not in window:
        #         window.add(c)
        #         length += 1
        #         res = max(res, length)
        #     else:
        #         while c in window:
        #             window.remove(s[L])
        #             length -= 1
        #             L += 1
        #         window.add(c)
        #         length += 1
        # return res

        #OPTIMIZATION REMOVE LENGTH VARIABLE
        window = set()
        L = 0
        res = 0
        for R in range(len(s)):
            c = s[R]
            if c not in window:
                window.add(c)
                res = max(res, R - L + 1)
            else:
                while c in window:
                    window.remove(s[L])
                    L += 1
                window.add(c)
        return res



