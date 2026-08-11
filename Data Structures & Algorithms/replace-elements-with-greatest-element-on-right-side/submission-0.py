class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = right_max
                right_max = max(right_max, temp)
        return arr