class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(pt):
            return pt[0]**2 + pt[1]**2
        def quickSort(st, end, i):
            if end - st + 1 <= 1:
                return
            if i == 0:
                return
            pivot = getDist(points[end])
            left = st
            for i in range(st, end):
                if getDist(points[i]) < pivot:
                    points[left], points[i] = points[i], points[left]
                    left += 1
            points[left], points[end] = points[end], points[left]
            quickSort(st, left - 1, i - 1)
            quickSort(left + 1, end, i - 1)
            return 
        quickSort(0, len(points) - 1, k)
        return points[:k]        

