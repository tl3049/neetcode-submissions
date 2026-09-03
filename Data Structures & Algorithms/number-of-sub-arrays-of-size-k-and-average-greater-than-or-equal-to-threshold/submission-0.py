from collections import deque
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = deque()
        L = 0
        count = 0
        curSum = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                window.popleft()
                curSum -= arr[L]
                L += 1
            window.append(arr[R])
            curSum += arr[R]
            if (curSum / len(window) >= threshold) and len(window) == k:
                # print(window) 
                # print(curSum)
                count += 1
        return count