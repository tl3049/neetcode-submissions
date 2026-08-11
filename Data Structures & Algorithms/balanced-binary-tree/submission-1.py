# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]
            lB, lv = dfs(node.left)
            rB, rv = dfs(node.right)
            height = max(lv, rv) + 1
            if lB and rB and abs(lv - rv) <= 1:
                return [True, height]
            else:
                return [False, height]
        [res, val] = dfs(root)
        return res 