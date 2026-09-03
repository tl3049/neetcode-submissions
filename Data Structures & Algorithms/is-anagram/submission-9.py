from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = Counter(s)
        dic_t = Counter(t)
        return dic_s == dic_t
        # for key, value in dic_s.items():
        #     if key not in dic_t:
        #         return False
        #     if dic_t[key] != value:
        #         return False
        # return True if len(s) == len(t) else False