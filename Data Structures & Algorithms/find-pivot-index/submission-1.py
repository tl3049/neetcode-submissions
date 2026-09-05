class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # n = len(nums)
        # prefix = [0] * n
        # posfix = [0] * n
        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] + nums[i - 1]
        # for i in range(n - 2, -1, -1):
        #     posfix[i] = posfix[i + 1] + nums[i + 1]
        # for i in range(n):
        #     if prefix[i] == posfix[i]:
        #         return i
        # return -1

        #OPTIMAL SPACE COMPLEXITY
        n = len(nums)
        total = sum(nums)
        preSum = 0
        for i in range(n):
            postSum = total - preSum - nums[i]
            if preSum == postSum:
                return i
            preSum += nums[i]
        return -1
