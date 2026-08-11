class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:#sorted part
                res = min(res, nums[l])
                break
            mid = (l + r)//2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            # print('l:',l)
            # print('r:',r)
            # print('mid',mid)
            # print('res',res)
        return res

