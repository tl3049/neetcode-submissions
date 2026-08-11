class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i, st in enumerate(strs):
            value = tuple(sorted(st))
            if value not in dic: 
                dic[value] = [st]
            else:
                dic[value].append(st)
        return list(dic.values())