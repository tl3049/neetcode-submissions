class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i, st in enumerate(strs):
            blk = [0]*26
            for s in st:
                blk[ord(s) - ord('a')] +=1 
            # value = str(sorted(st))
            value = tuple(blk)
            if value not in dic: 
                dic[value] = [st]
            else:
                dic[value].append(st)
        return list(dic.values())