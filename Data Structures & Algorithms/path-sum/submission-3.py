# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        path = []
        def dfs(node, cur_val):
            if not node:
                return
            path.append(node.val)
            val = cur_val + node.val
            if not node.left and not node.right:
                if val == targetSum:
                    self.res = True 
                return

            if not self.res:
                dfs(node.left, val)
            if not self.res:
                dfs(node.right, val)
            path.pop()
            return
        dfs(root, 0)
        print(path)
        return self.res