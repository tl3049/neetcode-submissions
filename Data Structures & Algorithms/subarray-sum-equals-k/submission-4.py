class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #OPTIMAL SOLUTION WITH O(N) COMPLEXITY
        res = 0
        count = {0 : 1}
        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            res += count.get(diff, 0)
            count[curSum] = 1 + count.get(curSum, 0)
        return res
        
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total == k:
        #             res += 1
        # return res