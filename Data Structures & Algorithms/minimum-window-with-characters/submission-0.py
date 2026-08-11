class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substr = ""
        #sliding windows
        n = len(s)
        m = len(t)
        if n < m:
            return substr
        l, r = 0, 0
        dic_t = Counter(t)#to compare with the dic
        n_char = len(dic_t)#total number of distict keys
        dic_c = {}
        count = 0
        wmin = float('inf')
        lmin = 0
        for r in range(n):
            if s[r] in t:
                dic_c[s[r]] = dic_c.get(s[r], 0) + 1
            if s[r] in t and dic_c[s[r]] == dic_t[s[r]]:
                count += 1
            while count == n_char:  
                if r - l + 1 < wmin:
                    wmin = r - l + 1
                    lmin = l
                if s[l] in t:
                    dic_c[s[l]] -= 1
                if s[l] in t and dic_c[s[l]] < dic_t[s[l]]:
                    count -= 1
                l += 1
            # print('l',l)
            # print('r',r)
            # print('wmin',wmin)
            # print('lmin',lmin)
        return s[lmin:lmin + wmin] if wmin != float('inf') else substr