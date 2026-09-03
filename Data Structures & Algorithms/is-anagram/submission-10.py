from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        #array as hash map
        if len(s) != len(t):
            return False
        dic = [0] * 26
        for i in range(len(s)):
            dic[ord(s[i]) - ord('a')] += 1
            dic[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if dic[i] != 0:
                return False
        return True        
        
        # dic_s = Counter(s)
        # dic_t = Counter(t)
        # for key, value in dic_s.items():
        #     if key not in dic_t:
        #         return False
        #     if dic_t[key] != value:
        #         return False
        # return True if len(s) == len(t) else False
        ## return dic_s == dic_t