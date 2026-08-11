class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in range(len(strs)):
            cstr = strs[i]
            clen = len(cstr)
            output = ''.join([output, str(clen) + '#' + cstr])
        return output
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            clen = ''
            while s[i] != '#':
                clen = ''.join([clen, s[i]])
                i += 1
            str_len = int(clen)
            strs.append(s[i+1: i+str_len+1])
            i = i + str_len + 1
        return strs
        
        