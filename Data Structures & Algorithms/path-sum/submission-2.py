# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        def dfs(node, cur_val):
            if not node:
                return
            val = cur_val + node.val
            if not node.left and not node.right:
                if val == targetSum:
                    self.res = True 
                return

            if not self.res:
                dfs(node.left, val)
            if not self.res:
                dfs(node.right, val)
            return
        dfs(root, 0)
        return self.res