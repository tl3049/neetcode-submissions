# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        i = k
        def dfs(node):
            nonlocal i, res
            if not node:
                return 
            dfs(node.left)
            i = i - 1
            if i == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res


        # res = []
        # def dfs(node):
        #     if not node:
        #         return 
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return res[k - 1]