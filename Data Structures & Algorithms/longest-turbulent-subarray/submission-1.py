class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        res = 1
        sign = 0
        for r in range(1, len(arr)):
            nsign = arr[r] - arr[r - 1]
            if nsign * sign > 0:
                l = r - 1
            if nsign == 0:
                l = r
            sign = nsign
            res = max(res, r - l + 1)
        return res