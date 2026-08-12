# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if root:
            q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if i == 0:
                    res.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return res