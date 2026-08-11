class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ##处理n不等于value情况
        # k = 0
        # for n in nums:
        #     if n != val:
        #         nums[k] = n
        #         k += 1
        # return k
        ##对应双指针 处理n等于value情况
        k = 0
        r = len(nums) - 1
        while k <= r:
            if nums[k] == val:
                nums[k] = nums[r]
                r -= 1
            else:
                k += 1
        return k