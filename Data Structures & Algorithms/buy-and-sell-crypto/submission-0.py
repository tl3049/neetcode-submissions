class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        profit = 0
        n = len(prices)
        for l in range(n):
            for r in range(l+1, n):
                profit = max(profit, prices[r] - prices[l])    
        return profit