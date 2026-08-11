class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTime(rate):
            res = 0
            for pile in piles:
                res += pile // rate
                if pile % rate > 0:
                    res += 1
            return res
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            time = getTime(m)
            if time > h:
                l = m + 1
            else:
                r = m
        return r
        # return l if getTime(l) <= h else -1

        

            