class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force
        # n = len(s)
        # longest = 0
        # for i in range(n):
        #     m = 0
        #     dic = {}
        #     for j in range(i, n):
        #         if s[j] in dic:
        #             break
        #         else:
        #             dic[s[j]] = dic.get(s[j],0) + 1
        #             m = m + 1
        #     longest = max(longest, m)
        # return longest
        #sliding window
        n = len(s)
        l, r = 0,0
        charSet = set()#compare the new char with the database
        longest = 0
        while r < n:
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
            longest = max(longest, r - l + 1)
            # print('charset',charSet)
            # print('longest', longest)
            # print('l',l)
            # print('r',r)
            r += 1
        return longest


