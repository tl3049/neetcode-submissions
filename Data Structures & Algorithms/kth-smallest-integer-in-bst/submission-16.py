# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        self.i = k
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if self.i == 0:
                return
            self.i -= 1
            if self.i == 0:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res


        # res = []
        # def dfs(node):
        #     if not node:
        #         return 
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return res[k - 1]