import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dis = x**2 + y**2
            heap.append([dis, x, y])
        heapq.heapify(heap)
        res = []
        while k > 0:
            dis, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        return res
                




        # def getDist(pt):
        #     return pt[0]**2 + pt[1]**2
        # def quickSort(st, end, r):
        #     if end - st + 1 <= 1:
        #         return
        #     pivot = getDist(points[end])
        #     left = st
        #     for i in range(st, end):
        #         if getDist(points[i]) < pivot:
        #             points[left], points[i] = points[i], points[left]
        #             left += 1
        #     points[left], points[end] = points[end], points[left]
        #     if left == r - 1:
        #         return
        #     elif left < r - 1:
        #         quickSort(left + 1, end, r)
        #     else:
        #         quickSort(st, left - 1, r)
        #     return 
        # quickSort(0, len(points) - 1, k)
        # return points[:k]        

