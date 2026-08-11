class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force: O(n^2)
        # profit = 0
        # n = len(prices)
        # for l in range(n):
        #     for r in range(l+1, n):
        #         profit = max(profit, prices[r] - prices[l])    
        # return profit
        #sliding window: O(n)
        profit = 0
        n = len(prices)
        l, r = 0, 1
        while r < n:
            if prices[l] < prices[r]:
                profit = max(profit, prices[r]- prices[l])
            else:
                l = r
            r += 1
        return profit
